import httpx
from bs4 import BeautifulSoup
import re
from typing import Optional

class CrawlerService:
    def __init__(self):
        self.headers = {
            "User-Agent": "DAP-Crawler/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }

    async def fetch_page(self, url: str) -> Optional[str]:
        """
        Fetches the HTML content of a page.
        """
        async with httpx.AsyncClient(follow_redirects=True, timeout=10.0) as client:
            try:
                response = await client.get(url, headers=self.headers)
                response.raise_for_status()
                return response.text
            except httpx.HTTPError as e:
                print(f"Error fetching {url}: {e}")
                return None

    def extract_content(self, html: str) -> dict:
        """
        Extracts title, text, and other metadata from HTML.
        """
        soup = BeautifulSoup(html, "html.parser")

        # Kill all script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()

        title = soup.title.string if soup.title else ""
        
        # Get text
        text = soup.get_text()
        
        # Breaking multi-headlines into a line each
        lines = (line.strip() for line in text.splitlines())
        # Drop blank lines
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(chunk for chunk in chunks if chunk)

        return {
            "title": title,
            "text": clean_text
        }

    def clean_text(self, text: str) -> str:
        """
        Further cleaning if necessary.
        """
        # Remove extra whitespace
        return re.sub(r'\s+', ' ', text).strip()
