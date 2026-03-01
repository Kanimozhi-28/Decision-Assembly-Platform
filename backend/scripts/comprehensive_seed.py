import asyncio
import uuid
import sys
import os
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

from app.services.embeddings import EmbeddingService
from app.services.qdrant_store import QdrantStore
from app.db.database import get_pool
from qdrant_client.models import PointStruct

async def comprehensive_seed():
    print("Initializing Comprehensive Seed for Qdrant...")
    embeddings = EmbeddingService()
    qdrant = QdrantStore()
    collection_name = "dap_products"
    
    # Ensure collection exists
    qdrant.create_collection_if_not_exists(collection_name)
    
    base_url = "http://localhost:8000/test-sites"
    
    demo_data = [
        # 1. Nexus Digital Bank (99999999-9999-4999-9999-999999999999)
        {
            "site_id": "99999999-9999-4999-9999-999999999999",
            "products": [
                # Savings
                {"title": "Max Saver Account", "category": "savings", "price": "7.0% p.a.", "text": "High interest for your idle cash. Maximize your savings with competitive rates.", "slug": "max-saver-account"},
                {"title": "Basic Savings", "category": "savings", "price": "3.5% p.a.", "text": "Perfect entry-level bank account for your daily needs.", "slug": "basic-savings"},
                {"title": "Salary Premium", "category": "savings", "price": "4.0% p.a.", "text": "Exclusive benefits for salaried professionals including higher limits.", "slug": "salary-premium"},
                {"title": "Senior Citizen Savings", "category": "savings", "price": "7.5% p.a.", "text": "Secure your retirement with higher yields. Special rates for seniors.", "slug": "senior-citizen-savings"},
                {"title": "Digital Only Account", "category": "savings", "price": "6.0% p.a.", "text": "Bank on the go with our 100% digital account. No physical branch needed.", "slug": "digital-only-account"},
                
                # Loans
                {"title": "Home Loan Prime", "category": "loans", "price": "8.4% p.a.", "text": "Fulfill your dream of owning a home with low interest rates.", "slug": "home-loan-prime"},
                {"title": "Personal Loan Instant", "category": "loans", "price": "10.5% p.a.", "text": "Unsecured funds for your immediate needs with quick approval.", "slug": "personal-loan-instant"},
                {"title": "Auto Loan Swift", "category": "loans", "price": "9.2% p.a.", "text": "Get behind the wheel of your new car with flexible EMI options.", "slug": "auto-loan-swift"},
                {"title": "Gold Loan Flexi", "category": "loans", "price": "9.0% p.a.", "text": "Instant liquidity against your gold jewelry with minimal paperwork.", "slug": "gold-loan-flexi"},
                
                # Cards
                {"title": "Platinum Rewards Card", "category": "cards", "price": "Rs. 2,500 / year", "text": "Maximize your lifestyle with exclusive rewards and lounge access.", "slug": "platinum-rewards-card"},
                {"title": "Cashback Pro", "category": "cards", "price": "Rs. 999 / year", "text": "Unlimited cashback on every spend. Get rewarded for your daily purchases.", "slug": "cashback-pro"},
                {"title": "Travel Nomad Card", "category": "cards", "price": "Rs. 3,500 / year", "text": "The perfect companion for international travels with zero FX markup.", "slug": "travel-nomad-card"},
                {"title": "Student Genesis", "category": "cards", "price": "Rs. 0 (Lifetime Free)", "text": "Start your credit journey today with our student-friendly credit card.", "slug": "student-genesis"},
                
                # Insurance
                {"title": "Term Life Guard", "category": "insurance", "price": "Rs. 500/mo", "text": "Secure your family's financial future with comprehensive life cover.", "slug": "term-life-guard"},
                {"title": "Health Plus Family", "category": "insurance", "price": "Rs. 1,200/mo", "text": "Comprehensive health cover for your loved ones including pre-existing diseases.", "slug": "health-plus-family"},
                {"title": "Home Secure", "category": "insurance", "price": "Rs. 1,000 / year", "text": "Protect your home and belongings against theft and natural disasters.", "slug": "home-secure"}
            ]
        },
        # 2. E-Life Store (88888888-8888-4888-8888-888888888888)
        {
            "site_id": "88888888-8888-4888-8888-888888888888",
            "products": [
                # Mobiles
                {"title": "Phox 8 Pro", "category": "mobiles", "price": "Rs. 74,999", "text": "The ultimate flagship with AI camera and professional photography features.", "slug": "phox-8-pro"},
                {"title": "Galax S24 Ultra", "category": "mobiles", "price": "Rs. 1,24,999", "text": "Unleash your creativity with the S-Pen and high-performance chip.", "slug": "galax-s24-ultra"},
                {"title": "Ipone 15", "category": "mobiles", "price": "Rs. 69,999", "text": "Experience the power of the A16 chip and brilliant display.", "slug": "ipone-15"},
                {"title": "OnePlus 12R", "category": "mobiles", "price": "Rs. 39,999", "text": "Smooth beyond belief with fast charging and premium design.", "slug": "oneplus-12r"},
                
                # Laptops
                {"title": "MacBok Air M2", "category": "laptops", "price": "Rs. 99,900", "text": "Strikingly thin and fast with long battery life.", "slug": "macbok-air-m2"},
                {"title": "Dell XPS 13", "category": "laptops", "price": "Rs. 1,14,000", "text": "The world's most compact 13-inch laptop with infinity display.", "slug": "dell-xps-13"},
                {"title": "Asus ROG Strix G16", "category": "laptops", "price": "Rs. 1,55,000", "text": "Dominate the battlefield with high-end gaming performance.", "slug": "asus-rog-strix-g16"},
                
                # Appliances
                {"title": "Samsung 8kg Front Load", "category": "appliances", "price": "Rs. 32,499", "text": "EcoBubble technology for deep cleaning and fabric care.", "slug": "samsung-8kg-front-load"},
                {"title": "Dyson V11 Absolute", "category": "appliances", "price": "Rs. 54,900", "text": "Powerful cordless vacuum for all floors with smart suction.", "slug": "dyson-v11-absolute"},
                
                # Accessories
                {"title": "Sony WH-1000XM5", "category": "accessories", "price": "Rs. 29,990", "text": "Industry-leading noise cancellation and crystal clear audio.", "slug": "sony-wh-1000xm5"},
                {"title": "AirPads Pro Gen 2", "category": "accessories", "price": "Rs. 24,900", "text": "The best in-ear audio experience with active noise cancellation.", "slug": "airpads-pro-gen-2"},
                
                # Fashion
                {"title": "Nike Air Force 1", "category": "fashion", "price": "Rs. 9,695", "text": "The legend lives on in this classic and stylish sneaker.", "slug": "nike-air-force-1"},
                {"title": "Titan Edge Ceramic", "category": "fashion", "price": "Rs. 15,999", "text": "World's slimmest ceramic watch with premium design.", "slug": "titan-edge-ceramic"}
            ]
        },
        # 3. CarePoint Healthcare (77777777-7777-4777-7777-777777777777)
        {
            "site_id": "77777777-7777-4777-7777-777777777777",
            "products": [
                # Cardiology
                {"title": "Heart Bypass Surgery", "category": "cardiology", "price": "Rs. 3.5L - 6L", "text": "Highly advanced CABG for heart health. Expert surgeons and care.", "slug": "heart-bypass-surgery"},
                {"title": "Angioplasty", "category": "cardiology", "price": "Rs. 1.2L - 2.5L", "text": "Minimally invasive blocked artery treatment for quick recovery.", "slug": "angioplasty"},
                {"title": "ECG & Stress Test", "category": "cardiology", "price": "Rs. 500 - 3,000", "text": "Routine heart health evaluation with professional interpretation.", "slug": "ecg-&-stress-test"},
                
                # Neurology
                {"title": "Brain Tumor Surgery", "category": "neurology", "price": "Rs. 4L - 10L", "text": "Precision removal of neurological growths using latest technology.", "slug": "brain-tumor-surgery"},
                {"title": "Stroke Rehabilitation", "category": "neurology", "price": "Rs. 50k - 2L", "text": "Recovering motor skills post-stroke with dedicated therapists.", "slug": "stroke-rehabilitation"},
                
                # Orthopedics
                {"title": "Knee Replacement", "category": "orthopedics", "price": "Rs. 1.8L - 3.5L", "text": "Total or partial robotic knee arthroplasty for better mobility.", "slug": "knee-replacement"},
                {"title": "Hip Replacement", "category": "orthopedics", "price": "Rs. 2L - 4L", "text": "Restoring mobility with advanced implants and care.", "slug": "hip-replacement"},
                
                # Pediatrics
                {"title": "Newborn Care", "category": "pediatrics", "price": "Consultation", "text": "Comprehensive checkups for infants by expert pediatricians.", "slug": "newborn-care"},
                {"title": "Pediatric Vaccination", "category": "pediatrics", "price": "Per Kit", "text": "Shielding child from common diseases with timely vaccinations.", "slug": "pediatric-vaccination"},
                
                # Diagnostics
                {"title": "Full Body Checkup", "category": "diagnostics", "price": "Rs. 5,000", "text": "Comprehensive 60+ parameter test for overall health monitoring.", "slug": "full-body-checkup"},
                {"title": "MRI Scan 3 Tesla", "category": "diagnostics", "price": "Rs. 8,000 - 15,000", "text": "High resolution imaging of internal organs for accurate diagnosis.", "slug": "mri-scan-3-tesla"}
            ]
        }
    ]
    
    all_points = []
    for entry in demo_data:
        site_id = entry["site_id"]
        sub_path = "banking/banking" if site_id == "99999999-9999-4999-9999-999999999999" else \
                   "ecommerce/product" if site_id == "88888888-8888-4888-8888-888888888888" else \
                   "healthcare/service"
        
        print(f"Generating points for site: {site_id}")
        for p in entry["products"]:
            # Standardized URL matching what's in the HTML
            url = f"{base_url}/{sub_path}-{p['slug']}.html"
            
            p_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{site_id}:{p['title']}"))
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
                    "url": url,
                    "is_product": True
                }
            ))
            
    if all_points:
        print(f"Upserting {len(all_points)} total products to Qdrant...")
        qdrant.upsert_points(collection_name, all_points)
        
        # Sync to SQL
        print("Syncing to PostgreSQL indexed_pages...")
        pool = await get_pool()
        async with pool.acquire() as conn:
            records = []
            for pt in all_points:
                pl = pt.payload
                records.append((
                    uuid.UUID(pl["site_id"]),
                    pl["url"],
                    "product",
                    pt.id,
                    pl["title"],
                    pl["text"][:200]
                ))
            
            await conn.executemany("""
                INSERT INTO dap.indexed_pages (site_id, url, page_type, product_id, title, snippet)
                VALUES ($1, $2, $3, $4, $5, $6)
                ON CONFLICT (site_id, url) DO UPDATE
                SET product_id = EXCLUDED.product_id, title = EXCLUDED.title, snippet = EXCLUDED.snippet, indexed_at = now()
            """, records)
            
        print("Comprehensive Seeding Complete!")
    else:
        print("No products found to seed.")

if __name__ == "__main__":
    asyncio.run(comprehensive_seed())
