import asyncio
from crawl4ai import AsyncWebCrawler

async def test_crawl():
    print("Testing Crawl4AI...")
    url = "https://www.google.com" # Using a reliable site for basic test
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url)
            if result.success:
                print(f"✅ Success! Scraped {len(result.markdown)} characters of markdown.")
                print(f"Title: {result.metadata.get('title') if result.metadata else 'N/A'}")
            else:
                print(f"❌ Crawl Failed: {result.error_message}")
    except Exception as e:
        print(f"💥 Exception: {e}")

if __name__ == "__main__":
    asyncio.run(test_crawl())
