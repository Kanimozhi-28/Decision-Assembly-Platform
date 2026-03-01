import sys
import argparse
import subprocess
import os

def run_command(command):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, capture_output=False, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {result.returncode}")
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="DAP Master Site Onboarder")
    parser.add_argument("--site_id", type=str, required=True, help="Site ID (UUID)")
    parser.add_argument("--url", type=str, required=True, help="Base URL to start crawling")
    parser.add_argument("--max", type=int, default=10, help="Max pages to crawl")
    
    args = parser.parse_args()
    
    print("="*60)
    print(f"ONBOARDING SITE: {args.site_id}")
    print(f"START URL: {args.url}")
    print("="*60)
    
    # 1. Crawl
    print("\n[STEP 1/2] Crawling...")
    crawl_cmd = ["python", "backend/crawler.py", "--site_id", args.site_id, "--url", args.url, "--max", str(args.max)]
    if not run_command(crawl_cmd):
        sys.exit(1)
        
    # 2. Index
    print("\n[STEP 2/2] Indexing...")
    index_cmd = ["python", "backend/index_content.py", "--site_id", args.site_id]
    if not run_command(index_cmd):
        sys.exit(1)
        
    print("\n" + "="*60)
    print(f"SUCCESS: Site {args.site_id} is now onboarded and indexed!")
    print("="*60)

if __name__ == "__main__":
    main()
