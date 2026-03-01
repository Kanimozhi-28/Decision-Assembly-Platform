import asyncio
import uuid
from app.services.embeddings import EmbeddingService
from app.services.qdrant_store import QdrantStore
from app.db.database import get_pool
from qdrant_client.models import PointStruct
import uuid as uuid_lib

async def seed_master_qdrant():
    print("Initializing Master Seed for Qdrant...")
    embeddings = EmbeddingService()
    qdrant = QdrantStore()
    collection_name = "dap_products"
    qdrant.create_collection_if_not_exists(collection_name)
    
    demo_data = [
        # 1. Nexus Digital Bank (99999999-9999-4999-9999-999999999999)
        {
            "site_id": "99999999-9999-4999-9999-999999999999",
            "products": [
                {"title": "Nexus High-Yield Savings", "category": "savings", "price": "4.5% APY", "features": ["No monthly fees", "Daily compounding", "FDIC Insured"], "text": "Start growing your wealth today with our market-leading interest rates and zero monthly fees."},
                {"title": "Nexus Elite Credit Card", "category": "cards", "price": "$0 Joining Fee", "features": ["5% Cashback", "Lounge Access", "No FX Fees"], "text": "Earn 5% cashback on travel and dining. Includes complimentary airport lounge access worldwide."},
                {"title": "Nexus Personal Loan", "category": "loans", "price": "8.99% APR", "features": ["Instant Approval", "Flexible Tenure", "No Prepayment Penalty"], "text": "Flexible repayment options up to 60 months. Instant approval for existing Nexus customers."},
                {"title": "Nexus Home Insurance", "category": "insurance", "price": "Starting $50/mo", "features": ["Fire & Theft", "Natural Disasters", "24/7 Support"], "text": "Comprehensive protection for your home and assets against natural disasters and theft."}
            ]
        },
        # 2. E-Life Store (88888888-8888-4888-8888-888888888888)
        {
            "site_id": "88888888-8888-4888-8888-888888888888",
            "products": [
                {"title": "E-Life Flagship Smartphone", "category": "mobiles", "price": "$999", "features": ["OLED Display", "5G Ready", "Triple Camera"], "text": "Stunning OLED display, triple-lens camera system, and ultra-fast 5G connectivity."},
                {"title": "E-Life Pro Ultrabook", "category": "laptops", "price": "$1,499", "features": ["4K Display", "15h Battery", "Aluminum Body"], "text": "Powerful performance in a sleek aluminum chassis. 15-hour battery life and 4K display."},
                {"title": "E-Life Smart Appliance Hub", "category": "appliances", "price": "$299", "features": ["Voice Control", "Energy Monitoring", "Easy Setup"], "text": "Control your entire home from one intuitive touch interface. Compatible with all major smart brands."},
                {"title": "E-Life Fitness Smartwatch", "category": "accessories", "price": "$249", "features": ["Heart Rate", "GPS", "Sleep Tracking"], "text": "Track your health with precision. Heart rate monitoring, GPS, and advanced sleep analysis."}
            ]
        },
        # 3. CarePoint Healthcare (77777777-7777-4777-7777-777777777777)
        {
            "site_id": "77777777-7777-4777-7777-777777777777",
            "products": [
                {"title": "Comprehensive Cardiac Screening", "category": "cardiology", "price": "$150", "features": ["ECG", "Stress Test", "Dr Consultation"], "text": "Full heart health evaluation including ECG, stress test, and specialist consultation."},
                {"title": "Advanced Neurological Assessment", "category": "neurology", "price": "$200", "features": ["Brain Scan", "Memory Test", "Motor Function"], "text": "Expert evaluation of brain health, memory, and motor functions using latest diagnostic tools."},
                {"title": "Pediatric Wellness Program", "category": "pediatrics", "price": "$120", "features": ["Vaccinations", "Growth Chart", "Diet Plan"], "text": "Regular health checkups and vaccination plans tailored for newborns to adolescents."},
                {"title": "Full-Body MRI Diagnostics", "category": "diagnostics", "price": "$600", "features": ["High Res Imaging", "Full Report", "Radiologist Review"], "text": "High-resolution imaging for early detection of potential health issues in all major systems."}
            ]
        }
    ]
    
    all_points = []
    for entry in demo_data:
        site_id = entry["site_id"]
        print(f"Generating embeddings for site: {site_id}")
        for p in entry["products"]:
            # Create a unique ID for the product based on title and site_id to avoid dupes
            p_id = str(uuid_lib.uuid5(uuid_lib.NAMESPACE_URL, f"{site_id}:{p['title']}"))
            vector = await embeddings.generate_embedding(f"{p['title']} {p['text']}")
            all_points.append(PointStruct(
                id=p_id,
                vector=vector,
                payload={
                    "site_id": site_id,
                    "title": p["title"],
                    "text": p["text"],
                    "category": p["category"],
                    "price": p["price"],
                    "features": p.get("features", []),
                    "url": f"http://localhost:8000/products/{p['category']}/{p['title'].lower().replace(' ', '-')}"
                }
            ))
            
    if all_points:
        qdrant.upsert_points(collection_name, all_points)
        print(f"Successfully seeded {len(all_points)} products across 3 sites in Qdrant.")
        
        # NEW: Persist to PostgreSQL indexed_pages
        try:
            pool = await get_pool()
            async with pool.acquire() as conn:
                records = []
                for p_point in all_points:
                    payload = p_point.payload
                    records.append((
                        uuid.UUID(payload["site_id"]),
                        payload["url"],
                        "product",
                        p_point.id, # Using the uuid5 we generated
                        payload["title"],
                        (payload["text"][:200] + "...") if len(payload["text"]) > 200 else payload["text"]
                    ))
                
                await conn.executemany(
                    """
                    INSERT INTO dap.indexed_pages (site_id, url, page_type, product_id, title, snippet)
                    VALUES ($1, $2, $3, $4, $5, $6)
                    ON CONFLICT (site_id, url) DO UPDATE 
                    SET product_id = $4, title = $5, snippet = $6, indexed_at = now()
                    """,
                    records
                )
            print(f"Successfully recorded {len(records)} pages in PostgreSQL indexed_pages.")
        except Exception as e:
            print(f"[SEED-SQL ERROR] Failed to record indexed pages: {e}")
    else:
        print("No products were generated.")

if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    asyncio.run(seed_master_qdrant())
