import httpx
import asyncio

async def test():
    async with httpx.AsyncClient() as client:
        resp = await client.post("http://localhost:8000/behavior/analyze", json={
            "site_id": "88888888-8888-4888-8888-888888888888",
            "type": "hover",
            "metadata": "$129.99",
            "url": "http://localhost:8081/ecommerce/index.html"
        }, timeout=10.0)
        print(resp.json())

if __name__ == "__main__":
    asyncio.run(test())
