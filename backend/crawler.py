import json
import os
import argparse
from crawl4ai import WebCrawler
from pathlib import Path
from urllib.parse import urljoin, urlparse

def get_links(markdown, base_url, exclusions=None):
    """Simple helper to extract internal links from markdown with exclusion support"""
    import re
    links = re.findall(r'\[.*?\]\((/.*?)\)', markdown)
    full_links = [urljoin(base_url, l) for l in links]
    # Filter to same domain and unique
    domain = urlparse(base_url).netloc
    internal_links = sorted(list(set([l for l in full_links if urlparse(l).netloc == domain])))
    
    # Apply exclusions (PRD §8.2 Alignment)
    if exclusions:
        filtered = []
        for link in internal_links:
            path = urlparse(link).path
            if any(re.search(pattern.replace('*', '.*'), path) for pattern in exclusions):
                continue
            filtered.append(link)
        return filtered
        
    return internal_links

def extract_structured_data(result):
    """Attempt to extract structured data from the page"""
    data = {}
    
    # 1. Extract JSON-LD
    if result.metadata and "json_ld" in result.metadata:
        # Crawl4AI might provide this directly in session metadata
        data["schema"] = result.metadata.get("json_ld")
    
    # 2. Heuristic extraction from Markdown (Price, Features)
    # This is a fallback if Schema.org is missing
    markdown = result.markdown
    import re
    
    # Pricing patterns: $123, Currency symbols, etc.
    price_match = re.search(r'(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)', markdown)
    if price_match:
        data["price"] = price_match.group(1)
        
    # Feature list pattern: Look for bullet points near headers
    feature_matches = re.findall(r'^\s*[\*\-]\s+(.*)$', markdown, re.MULTILINE)
    if feature_matches:
        data["features"] = feature_matches[:5] # Top 5 features
        
    return data

def crawl_site(site_id, base_url, max_pages=20, exclusions=None):
    """Crawl a site dynamically starting from base_url, respecting exclusions"""
    
    print(f"Starting ENRICHED crawl of {base_url} for Site: {site_id}...")
    
    results = []
    visited = set()
    to_visit = [base_url]
    
    crawler = WebCrawler()
    crawler.warmup()

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue
            
        print(f"📄 [{len(visited)+1}/{max_pages}] Crawling {url}...")
        visited.add(url)
        
        try:
            result = crawler.run(url=url)
            
            if result.success:
                path = urlparse(url).path or "/"
                
                # ENRICHMENT: Extract structured data
                structured = extract_structured_data(result)
                
                extracted_data = {
                    "url": url,
                    "title": result.metadata.get("title", ""),
                    "content": result.markdown,
                    "path": path,
                    "site_id": site_id,
                    "metadata": structured
                }
                results.append(extracted_data)
                
                # Discovery (with exclusions)
                new_links = get_links(result.markdown, base_url, exclusions)
                for link in new_links:
                    if link not in visited and link not in to_visit:
                        to_visit.append(link)
                
                print(f"   ✅ Extracted {len(result.markdown)} chars. Features found: {len(structured.get('features', []))}")
            else:
                print(f"   ❌ Failed to crawl {url}: {result.error_message}")
        except Exception as e:
            print(f"   ⚠️ Error crawling {url}: {e}")

    # Save to a site-specific JSON file
    output_path = Path(f"crawled_{site_id}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
        
    print(f"\nCrawl complete! Saved {len(results)} pages to {output_path}")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generic Web Crawler for DAP")
    parser.add_argument("--site_id", type=str, required=True, help="Site ID (UUID)")
    parser.add_argument("--url", type=str, required=True, help="Base URL to start crawling")
    parser.add_argument("--exclude", type=str, help="Comma-separated exclusion patterns")
    parser.add_argument("--max", type=int, default=10, help="Max pages to crawl")
    
    args = parser.parse_args()
    exclusions = args.exclude.split(',') if args.exclude else []
    crawl_site(args.site_id, args.url, args.max, exclusions)
