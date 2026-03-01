import asyncio
import asyncpg
import argparse
import os
import uuid
import json
import subprocess
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

async def register_site(name, domain, start_url, ngrok_url=None):
    site_id = str(uuid.uuid4())
    print(f"🚀 Registering Site: {name} ({domain})")
    
    # Origins to allow
    allowed_origins = [
        f"http://{domain}", 
        f"https://{domain}",
        "http://localhost:5173", 
        "http://127.0.0.1:5500", # User testing origin
        "http://localhost:5500"
    ]
    if ngrok_url:
        allowed_origins.append(ngrok_url.rstrip('/'))

    try:
        conn = await asyncpg.connect(DATABASE_URL)
        
        # 1. Insert into sites
        await conn.execute("""
            INSERT INTO sites (site_id, name, domain, allowed_origins)
            VALUES ($1::uuid, $2, $3, $4)
        """, site_id, name, domain, json.dumps(allowed_origins))
        
        # 2. Insert default site_config
        # We use a generic trigger and intent map that works across products
        triggers = {
            "multipleProductViews": {"threshold": 2, "timeWindow": 300},
            "sessionHesitation": {"dwellTime": 30, "scrollDepth": 0.5},
            "ctaHover": {"hoverCount": 1, "noClick": True},
            "navigationLoops": {"threshold": 2}
        }
        
        intents = [
            {"id": "compare", "label": "Compare options", "description": "See products side-by-side"},
            {"id": "help_choose", "label": "Help me choose", "description": "Get personalized recommendations"}
        ]
        
        intent_map = {
            "default": {
                "compare": ["Feature Comparison", "Rewards & Benefits", "Fees & APR"],
                "help_choose": ["Feature Comparison", "Rewards & Benefits"]
            }
        }
        
        commentary = {
            "welcome": f"Welcome to {name}! I'm here to help you find the best solution.",
            "hesitation": "Taking your time? I can simplify the details for you.",
            "multi_view": "You've viewed {n} products - want a side-by-side comparison?",
            "revisit": "Welcome back! Let's pick up where you left off."
        }

        await conn.execute("""
            INSERT INTO site_config (site_id, triggers, intents, intent_map, commentary_templates)
            VALUES ($1::uuid, $2, $3, $4, $5)
        """, site_id, json.dumps(triggers), json.dumps(intents), json.dumps(intent_map), json.dumps(commentary))
        
        print(f"✅ Database record created. Site ID: {site_id}")
        await conn.close()
        
        # 3. Run Onboarding (Crawl & Index)
        print(f"\n📡 Starting Onboarding Pipe for {start_url}...")
        onboard_cmd = ["python", "backend/onboard_site.py", "--site_id", site_id, "--url", start_url, "--max", "15"]
        subprocess.run(onboard_cmd)
        
        print("\n" + "="*60)
        print(f"🎉 COMPLETION SUMMARY")
        print(f"Site Name: {name}")
        print(f"Site ID:   {site_id}")
        print(f"JS Snippet for {domain}:")
        print(f"--------------------------------------------------")
        snippet_url = ngrok_url if ngrok_url else "http://localhost:8000"
        print(f'<script src=\"{snippet_url}/sdk/dap.js\" data-site-id=\"{site_id}\" data-api-base=\"{snippet_url}\"></script>')
        print(f"--------------------------------------------------")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Registration Failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Live Site Onboarder")
    parser.add_argument("--name", required=True)
    parser.add_argument("--domain", required=True, help="e.g. hdfcbank.com")
    parser.add_argument("--url", required=True, help="Start crawling from here")
    parser.add_argument("--ngrok", help="Your ngrok or public backend URL")
    
    args = parser.parse_args()
    asyncio.run(register_site(args.name, args.domain, args.url, args.ngrok))
