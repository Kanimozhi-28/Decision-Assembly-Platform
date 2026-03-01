import os

SITE_DIR = "test-sites/ecommerce"
os.makedirs(SITE_DIR, exist_ok=True)

CATEGORIES = ["Mobiles", "Laptops", "Accessories", "Appliances", "Fashion"]
PRODUCTS = {
    "Mobiles": [
        ("Phox 8 Pro", "Rs. 74,999", "The ultimate flagship with AI camera.", ["50MP Camera", "120Hz LTPO Display", "Titanium Frame"]),
        ("Galax S24 Ultra", "Rs. 1,24,999", "Unleash your creativity with the S-Pen.", ["200MP Main Camera", "Snapdragon 8 Gen 3", "5000mAh Battery"]),
        ("Ipone 15", "Rs. 69,999", "Experience the power of the A16 chip.", ["Dynamic Island", "48MP Main Camera", "All-day Battery"]),
        ("Redmi Note 13", "Rs. 17,999", "SuperNote for every Indian.", ["108MP Camera", "5000mAh Battery", "6.67 inch AMOLED"]),
        ("OnePlus 12R", "Rs. 39,999", "Smooth Beyond Belief.", ["Snapdragon 8 Gen 2", "5500mAh Battery", "OxygenOS 14"]),
        ("Realme GT 5", "Rs. 34,999", "The speed demon in your hands.", ["240W Charging", "144Hz Display", "RGB Lights"]),
        ("Vivo V30 Pro", "Rs. 41,999", "Studio-level portraits in your pocket.", ["Zeiss Optics", "Aura Light", "3D Curved Display"]),
        ("Pixel 7a", "Rs. 37,999", "The helpful Google phone at a great price.", ["Tensor G2", "Wireless Charging", "IP67 Protection"]),
    ],
    "Laptops": [
        ("MacBok Air M2", "Rs. 99,900", "Strikingly thin and fast.", ["Apple M2 Chip", "18-hr Battery", "Liquid Retina Display"]),
        ("Dell XPS 13", "Rs. 1,14,000", "The world's most compact 13-inch laptop.", ["InfinityEdge Display", "Intel Core i7", "Aluminum Build"]),
        ("HP Spectre x360", "Rs. 1,35,000", "Crafted for versatility and power.", ["360 Degree Hinge", "4K OLED Display", "Stylus Included"]),
        ("Lenovo Legion 5", "Rs. 85,000", "Play as hard as you work.", ["RTX 4060", "Ryzen 7 Processor", "165Hz Screen"]),
        ("Asus Vivobook 16", "Rs. 45,000", "Expansive view, smooth performance.", ["16-inch IPS Display", "Intel Core i5", "Military-grade Durability"]),
        ("Asus ROG Strix G16", "Rs. 1,55,000", "Dominate the battlefield.", ["RTX 4070", "Intel Core i9", "RGB Keyboard"]),
        ("Acer Swift Go 14", "Rs. 62,000", "Fast, light, and AI-ready.", ["OLED Display", "Intel Evo Platform", "Thin Design"]),
        ("Microsoft Surface Laptop 5", "Rs. 1,02,000", "Sleek and portable for every day.", ["Touch Screen", "Dolby Vision IQ", "Thunderbolt 4"]),
    ],
    "Accessories": [
        ("Sony WH-1000XM5", "Rs. 29,990", "Industry-leading noise cancellation.", ["30-hr Battery", "Clear Hands-free Calling", "Speak-to-Chat"]),
        ("AirPads Pro Gen 2", "Rs. 24,900", "The best in-ear audio experience.", ["H2 Chip", "Active Noise Cancellation", "Spatial Audio"]),
        ("Bose QuietComfort", "Rs. 25,000", "Legendary quiet. Comfort for all day.", ["CustomTune Technology", "Adjustable EQ", "Quiet Mode"]),
        ("Logitech MX Master 3S", "Rs. 10,000", "Precision and silence for creators.", ["8K DPI Tracking", "MagSpeed Scroll Wheel", "Quiet Clicks"]),
        ("Keychron K2 V2", "Rs. 8,500", "Wireless mechanical keyboard.", ["Gateron G Pro Switches", "RGB Backlight", "MacOS/Win Support"]),
        ("Samsung Galaxy Buds 2 Pro", "Rs. 15,000", "Seamless audio for Galaxy users.", ["24-bit Hi-Fi Audio", "Intelligent ANC", "360 Audio"]),
        ("Anker 737 Power Bank", "Rs. 12,000", "Ultra-powerful two-way charging.", ["140W Output", "24,000mAh", "Smart Digital Display"]),
        ("Razer DeathAdder V3", "Rs. 11,000", "The lightweight pro gaming mouse.", ["63g Weight", "30K DPI Optical Sensor", "HyperPolling"]),
    ],
    "Appliances": [
        ("Samsung 8kg Front Load", "Rs. 32,499", "EcoBubble technology for deep cleaning.", ["AI Control", "Hygiene Steam", "Digital Inverter"]),
        ("LG 43-inch 4K UHD", "Rs. 38,990", "Vivid colors and immersive sound.", ["WebOS", "Magic Remote", "HDR 10 Pro"]),
        ("Dyson V11 Absolute", "Rs. 54,900", "Powerful cordless vacuum for all floors.", ["LCD Display", "Hyperdymium Motor", "HEPA Filtration"]),
        ("IFB 30L Microwave", "Rs. 15,500", "Convection microwave with rotisserie.", ["101 Auto-cook Menus", "Steam Clean", "Multi-stage Cooking"]),
        ("Whirlpool 265L Refrigerator", "Rs. 28,000", "IntelliFresh with convertible freezer.", ["6th Sense Nutrilock", "Zeolite Technology", "Deep Freeze"]),
        ("Panasonic 1.5 Ton AC", "Rs. 36,000", "Smart WiFi Inverter AC.", ["MirAie App", "7 in 1 Convertible", "PM 0.1 Filter"]),
        ("Philips Air Fryer XL", "Rs. 12,500", "Healthy frying with Rapid Air technology.", ["Digital Touch Screen", "7 Presets", "Easy Clean"]),
        ("Eureka Forbes AquaGuard", "Rs. 14,000", "RO+UV+MTDS Water Purifier.", ["Active Copper Technology", "Mineral Guard", "UV e-boiling"]),
    ],
    "Fashion": [
        ("Nike Air Force 1", "Rs. 9,695", "The legend lives on in this classic.", ["Genuine Leather", "Air-Sole Cushioning", "Pivot-point Outsole"]),
        ("Levi's 511 Slim Fit", "Rs. 3,599", "Classic slim jeans for everyday wear.", ["Stretch Denim", "Five-pocket Styling", "Zip Fly"]),
        ("Titan Edge Ceramic", "Rs. 15,999", "World's slimmest ceramic watch.", ["Sapphire Crystal", "Italian Design", "Water Resistant"]),
        ("Ray-Ban Aviator", "Rs. 10,500", "The timeless icon of cool.", ["Polarized Lenses", "UV Protection", "Classic Gold Frame"]),
        ("Adidas Ultraboost Light", "Rs. 18,999", "The lightest Ultraboost ever.", ["Boost Midsole", "Continental Rubber", "Primeknit Upper"]),
        ("Tommy Hilfiger Polo", "Rs. 4,500", "Premium cotton piqué polo shirt.", ["Slim Fit", "Signature Branding", "Breathable Fabric"]),
        ("Fossil Gen 6 Smartwatch", "Rs. 22,000", "Faster performance with Wear OS.", ["SpO2 Sensor", "Fast Charging", "Customizable Dials"]),
        ("Zara Oversized Trench", "Rs. 8,000", "Classic autumn layer for style.", ["Water Repellent", "Belted Waist", "Epaulettes"]),
    ]
}

CSS = """
body { font-family: 'Inter', sans-serif; margin: 0; padding: 0; background: #f8f9fa; color: #333; }
header { background: #fff; border-bottom: 2px solid #e9ecef; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 100; }
nav ul { list-style: none; display: flex; gap: 20px; margin: 0; padding: 0; }
nav a { text-decoration: none; color: #495057; font-weight: 600; font-size: 15px; }
nav a:hover { color: #007bff; }
.logo { font-size: 24px; font-weight: 800; color: #007bff; text-decoration: none; }
.container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
.hero { background: linear-gradient(135deg, #007bff 0%, #0056b3 100%); color: #fff; padding: 100px 40px; border-radius: 20px; text-align: center; margin-bottom: 50px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px; }
.card { background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.2s; border: 1px solid #e9ecef; }
.card:hover { transform: translateY(-5px); }
.card-body { padding: 20px; }
.card-title { font-size: 18px; font-weight: 700; margin-bottom: 10px; }
.price { color: #28a745; font-size: 20px; font-weight: 800; margin-bottom: 15px; }
.btn { display: inline-block; background: #007bff; color: #fff; padding: 10px 24px; border-radius: 8px; text-decoration: none; font-weight: 600; text-align: center; border: none; cursor: pointer; }
.pdp-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; }
.spec-list { list-style: none; padding: 0; }
.spec-list li { padding: 10px 0; border-bottom: 1px solid #e9ecef; font-size: 14px; }
.reviews { margin-top: 50px; padding-top: 30px; border-top: 1px solid #dee2e6; }
footer { background: #343a40; color: #fff; padding: 40px; text-align: center; margin-top: 100px; }
"""

def generate_header(active_cat=None):
    links = ""
    for cat in CATEGORIES:
        active = "style='color:#007bff'" if cat == active_cat else ""
        links += f"<li><a href='{cat.lower()}.html' {active}>{cat}</a></li>"
    
    return f"""
    <header>
        <a href="index.html" class="logo">E-Life Store</a>
        <nav>
            <ul>
                {links}
            </ul>
        </nav>
    </header>
    """

# 1. Create Index
with open(f"{SITE_DIR}/index.html", "w", encoding="utf-8") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><title>E-Life Store | Premium Electronics & Lifestyle</title>
        <style>{CSS}</style>
        <script src="http://localhost:8000/sdk/loader.js" data-site-id="88888888-8888-4888-8888-888888888888"></script>
    </head>
    <body>
        {generate_header()}
        <div class="container">
            <div class="hero">
                <h1>The Future of Lifestyle is Here.</h1>
                <p>Exclusive deals on Mobiles, Laptops, and Smart Appliances.</p>
                <a href="#featured" class="btn" style="background:#fff; color:#007bff">Shop Now</a>
            </div>
            <h2 id="featured">Top Categories</h2>
            <div class="grid">
                {"".join([f'<a href="{c.lower()}.html" class="card" style="text-decoration:none; color:inherit"><div class="card-body"><h3 class="card-title">{c}</h3><p>Explore latest {c.lower()} products.</p></div></a>' for c in CATEGORIES])}
            </div>
        </div>
        <footer><p>&copy; 2026 E-Life Store. All rights reserved.</p></footer>
    </body>
    </html>
    """)

# 2. Create Category Pages
for cat in CATEGORIES:
    products_html = ""
    for p_name, p_price, p_desc, p_specs in PRODUCTS[cat]:
        file_name = f"product-{p_name.lower().replace(' ', '-')}.html"
        products_html += f"""
        <div class="card">
            <div class="card-body">
                <h3 class="card-title">{p_name}</h3>
                <p class="price">{p_price}</p>
                <p>{p_desc}</p>
                <a href="{file_name}" class="btn">View Details</a>
            </div>
        </div>
        """
    
    with open(f"{SITE_DIR}/{cat.lower()}.html", "w", encoding="utf-8") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8"><title>{cat} | E-Life Store</title>
            <style>{CSS}</style>
            <script src="http://localhost:8000/sdk/loader.js" data-site-id="88888888-8888-4888-8888-888888888888"></script>
        </head>
        <body>
            {generate_header(cat)}
            <div class="container">
                <h1>Latest in {cat}</h1>
                <div class="grid">{products_html}</div>
            </div>
        </body>
        </html>
        """)

# 3. Create Product Pages
for cat in CATEGORIES:
    for p_name, p_price, p_desc, p_specs in PRODUCTS[cat]:
        file_name = f"product-{p_name.lower().replace(' ', '-')}.html"
        specs_html = "".join([f"<li>{s}</li>" for s in p_specs])
        
        with open(f"{SITE_DIR}/{file_name}", "w", encoding="utf-8") as f:
            f.write(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8"><title>{p_name} | E-Life Store</title>
                <style>{CSS}</style>
                <script src="http://localhost:8000/sdk/loader.js" data-site-id="88888888-8888-4888-8888-888888888888"></script>
            </head>
            <body>
                {generate_header(cat)}
                <div class="container">
                    <div class="pdp-grid">
                        <div style="background:#ddd; border-radius:12px; height:400px; display:flex; align-items:center; justify-content:center; font-size:24px; color:#666;">Image Placeholder</div>
                        <div>
                            <h1>{p_name}</h1>
                            <p class="price">{p_price}</p>
                            <p style="font-size:18px; line-height:1.6; color:#555;">{p_desc}</p>
                            <h3>Key Specifications</h3>
                            <ul class="spec-list">{specs_html}</ul>
                            <button class="btn" style="width:100%; padding:20px; font-size:18px; margin-top:30px;">BUY NOW</button>
                        </div>
                    </div>
                    <div class="reviews">
                        <h2>Verified Customer Reviews</h2>
                        <div style="margin-bottom:20px;">
                            <p><strong>Aakash V.</strong> - ⭐⭐⭐⭐⭐</p>
                            <p>Absolutely love the {p_name}! The performance is top notch and the delivery was fast.</p>
                        </div>
                        <div>
                            <p><strong>Sneha R.</strong> - ⭐⭐⭐⭐</p>
                            <p>Great product for the price. The {p_specs[0].split()[0]} is very impressive.</p>
                        </div>
                    </div>
                </div>
                <footer><p>&copy; 2026 E-Life Store. All rights reserved.</p></footer>
            </body>
            </html>
            """)

print("Successfully generated eCommerce site with 46 pages.")
