import os

SITE_DIR = "test-sites/banking"
os.makedirs(SITE_DIR, exist_ok=True)

CATEGORIES = ["CreditCards", "Loans", "Savings", "Insurance"]
PRODUCTS = {
    "CreditCards": [
        ("Platinum Rewards Card", "Rs. 2,500 / year", "Maximize your lifestyle with exclusive rewards.", ["5X points on dining", "Concierge Service", "Airport Lounge Access"]),
        ("Cashback Pro", "Rs. 999 / year", "Unlimited cashback on every spend.", ["5% on E-commerce", "1% on all other spends", "Fuel Surcharge Waiver"]),
        ("Travel Nomad Card", "Rs. 3,500 / year", "The perfect companion for international travels.", ["Zero Forex Markup", "Complimentary Flight Insurance", "Travel Points"]),
        ("Student Genesis", "Rs. 0 (Lifetime Free)", "Start your credit journey today.", ["Low Interest Rate", "Instant Approval", "Reward Points on Books"]),
        ("Signature Wealth", "Rs. 10,000 / year", "Curated for the ultra-high net worth individuals.", ["Dedicated Wealth Manager", "Golf Course Access", "Personalized Insights"]),
        ("Infinite Shopping", "Rs. 1,500 / year", "Exclusive deals on world-class brands.", ["Buy 1 Get 1 on Movies", "10% off at Mall partners", "High Limit"]),
        ("Eco Green Card", "Rs. 500 / year", "Support sustainability with every swipe.", ["Tree planted on first spend", "Biodegradable material", "Green rewards"]),
        ("Corporate Edge", "Variable", "Optimized expenses for your business.", ["Detailed Reports", "Expense Management Tools", "Corporate Discounts"]),
    ],
    "Loans": [
        ("Home Loan Prime", "8.4% p.a.", "Fulfill your dream of owning a home.", ["Tenure up to 30 years", "No prepayment charges", "Quick Disbursement"]),
        ("Personal Loan Instant", "10.5% p.a.", "Unsecured funds for your immediate needs.", ["No Collateral Needed", "Funds in 24 hours", "Minimal Documentation"]),
        ("Auto Loan Swift", "9.2% p.a.", "Get behind the wheel of your new car.", ["Up to 100% on-road funding", "Special rates for EV", "Flexible Tenure"]),
        ("Education Loan Global", "11.0% p.a.", "Invest in your future education abroad.", ["Covers Tuition & Living", "Moratorium Period", "Tax Benefits under 80E"]),
        ("Business Growth Loan", "12.0% p.a.", "Scale your business to new heights.", ["Working Capital Support", "Machinery Financing", "SME Specialized"]),
        ("Gold Loan Flexi", "9.0% p.a.", "Instant liquidity against your gold jewelry.", ["On-the-spot valuation", "Interest-only payment", "Secure Storage"]),
        ("Property LAP", "9.5% p.a.", "Unlock value from your residential property.", ["Higher Loan Amount", "Longer Tenure", "Lower EMI"]),
        ("Two Wheeler Express", "13.0% p.a.", "Easy EMIs for your favorite bike.", ["Instant Verification", "Low Down Payment", "Pan-India Service"]),
    ],
    "Savings": [
        ("Max Saver Account", "7.0% p.a.", "High interest for your idle cash.", ["Auto-sweep to TD", "Zero Transaction Fee", "Free Platinum Debit Card"]),
        ("Basic Savings", "3.5% p.a.", "Perfect entry-level bank account.", ["Low Minimum Balance", "Mobile Banking", "Free Bill Pay"]),
        ("Salary Premium", "4.0% p.a.", "Exclusive benefits for salaried professionals.", ["Zero Balance Account", "Unlimited ATM Swipes", "Personal Accident Cover"]),
        ("Senior Citizen Savings", "7.5% p.a.", "Secure your retirement with higher yields.", ["Priority Service", "Quarterly Interest Payout", "Health Card Access"]),
        ("Kids Junior Account", "4.0% p.a.", "Teach your children the value of saving.", ["Customized Debit Card", "Educational Content", "Small Monthly Deposit"]),
        ("Women Empowerment Savings", "4.5% p.a.", "Designed for the modern woman.", ["Investment Advisory", "Discounts on Locker", "Home Loan Rebate"]),
        ("NRI NRE Account", "Repo + 2%", "Manage your offshore earnings effortlessly.", ["Tax Free Interest", "Repatriable Funds", "Relationship Manager"]),
        ("Digital Only Account", "6.0% p.a.", "Bank on the go with our 100% digital account.", ["No Paperwork", "Higher Interest", "Virtual Debit Card"]),
    ],
    "Insurance": [
        ("Term Life Guard", "Starting Rs. 500/mo", "Secure your family's financial future.", ["High Sum Assured", "Critical Illness Cover", "Terminal Illness Rider"]),
        ("Health Plus Family", "Starting Rs. 1,200/mo", "Comprehensive health cover for your loved ones.", ["Cashless Hospitalization", "No Claim Bonus", "OPD Coverage"]),
        ("Motor Shield Pro", "Market Rate", "Complete protection for your vehicle.", ["Zero Depreciation Cover", "RSA Support", "Quick Claim Settlement"]),
        ("Travel Safe Global", "Rs. 250 / trip", "Worry-free travel across the world.", ["Medical Emergency Cover", "Loss of Baggage", "Trip Cancellation"]),
        ("Home Secure", "Rs. 1,000 / year", "Protect your home and belongings.", ["Fire & Earthquake Cover", "Theft Protection", "Tenant Legal Liability"]),
        ("Cancer Care Plus", "Rs. 300 / mo", "Dedicated cover for cancer diagnosis.", ["Lump sum payout", "Multiple stages covered", "Premium waiver"]),
        ("Retirement Pension Plan", "Investment based", "Build a corpus for a stress-free retirement.", ["Guaranteed Income", "Tax Savings", "Vesting Options"]),
        ("Cyber Security Personal", "Rs. 150 / mo", "Stay protected from digital identity theft.", ["Phishing Cover", "Wallet Protection", "Legal Fee Reimbrusement"]),
    ]
}

CSS = """
body { font-family: 'Outfit', sans-serif; margin: 0; padding: 0; background: #fdfdfd; color: #1a1a1a; }
header { background: #111; color: #fff; padding: 15px 60px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 100; }
nav ul { list-style: none; display: flex; gap: 30px; margin: 0; padding: 0; }
nav a { text-decoration: none; color: #f0f0f0; font-weight: 500; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
nav a:hover { color: #d4af37; }
.logo { font-size: 26px; font-weight: 800; color: #d4af37; text-decoration: none; display: flex; align-items: center; gap: 10px; }
.container { max-width: 1100px; margin: 60px auto; padding: 0 20px; }
.hero { background: #1a1a1a; color: #fff; padding: 120px 60px; border-radius: 0; text-align: left; margin-bottom: 60px; border-left: 8px solid #d4af37; }
.hero h1 { font-size: 48px; margin-bottom: 20px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 40px; }
.card { background: #fff; border-radius: 0; border: 1px solid #eee; padding: 40px; transition: box-shadow 0.3s; }
.card:hover { box-shadow: 0 20px 40px rgba(0,0,0,0.05); }
.card-title { font-size: 20px; font-weight: 700; margin-bottom: 12px; color: #111; }
.fees { color: #d4af37; font-size: 18px; font-weight: 600; margin-bottom: 15px; }
.btn { display: inline-block; background: #d4af37; color: #111; padding: 12px 30px; font-weight: 700; text-decoration: none; border-radius: 0; transition: background 0.2s; }
.btn:hover { background: #b8860b; }
.pdp-box { border: 1px solid #eee; padding: 50px; background: #fff; }
.benefit-list { list-style: none; padding: 0; margin: 30px 0; }
.benefit-list li { padding-left: 30px; position: relative; margin-bottom: 15px; font-size: 16px; }
.benefit-list li::before { content: '✔'; position: absolute; left: 0; color: #d4af37; }
.terms { margin-top: 60px; font-size: 12px; color: #999; line-height: 1.6; }
footer { background: #111; color: #888; padding: 60px 40px; text-align: center; }
"""

def generate_header(active_cat=None):
    links = ""
    for cat in CATEGORIES:
        active = "style='color:#d4af37'" if cat == active_cat else ""
        links += f"<li><a href='{cat.lower()}.html' {active}>{cat.replace('CreditCards', 'Cards')}</a></li>"
    
    return f"""
    <header>
        <a href="index.html" class="logo">Nexus Digital Bank</a>
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
        <meta charset="UTF-8"><title>Nexus Bank | Banking Redefined</title>
        <style>{CSS}</style>
        <script src="http://localhost:8000/sdk/loader.js" data-site-id="99999999-9999-4999-9999-999999999999"></script>
    </head>
    <body>
        {generate_header()}
        <div class="container">
            <div class="hero">
                <h1>Financial Freedom <br>Starts Here.</h1>
                <p>Digital-first banking for the next generation of global citizens.</p>
                <a href="#services" class="btn">Explore Products</a>
            </div>
            <h2 id="services">Our Solutions</h2>
            <div class="grid">
                {"".join([f'<a href="{c.lower()}.html" class="card" style="text-decoration:none; color:inherit"><h3 class="card-title">{c}</h3><p>Innovative {c.lower()} solutions tailored for your growth.</p><span style="color:#d4af37; font-weight:700">Explore &rarr;</span></a>' for c in CATEGORIES])}
            </div>
        </div>
        <footer><p>&copy; 2026 Nexus Digital Bank. Member FDIC. Equal Housing Lender.</p></footer>
    </body>
    </html>
    """)

# 2. Create Category Pages
for cat in CATEGORIES:
    products_html = ""
    for p_name, p_fees, p_desc, p_benefits in PRODUCTS[cat]:
        file_name = f"banking-{p_name.lower().replace(' ', '-')}.html"
        products_html += f"""
        <div class="card">
            <h3 class="card-title">{p_name}</h3>
            <p class="fees">{p_fees}</p>
            <p>{p_desc}</p>
            <a href="{file_name}" class="btn">Learn More</a>
        </div>
        """
    
    with open(f"{SITE_DIR}/{cat.lower()}.html", "w", encoding="utf-8") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8"><title>{cat} | Nexus Bank</title>
            <style>{CSS}</style>
            <script src="http://localhost:8000/sdk/loader.js" data-site-id="99999999-9999-4999-9999-999999999999"></script>
        </head>
        <body>
            {generate_header(cat)}
            <div class="container">
                <h1>{cat} Solutions</h1>
                <div class="grid">{products_html}</div>
            </div>
        </body>
        </html>
        """)

# 3. Create Product Pages
for cat in CATEGORIES:
    for p_name, p_fees, p_desc, p_benefits in PRODUCTS[cat]:
        file_name = f"banking-{p_name.lower().replace(' ', '-')}.html"
        benefits_html = "".join([f"<li>{b}</li>" for b in p_benefits])
        
        with open(f"{SITE_DIR}/{file_name}", "w", encoding="utf-8") as f:
            f.write(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8"><title>{p_name} | Nexus Bank</title>
                <style>{CSS}</style>
                <script src="http://localhost:8000/sdk/loader.js" data-site-id="99999999-9999-4999-9999-999999999999"></script>
            </head>
            <body>
                {generate_header(cat)}
                <div class="container">
                    <div class="pdp-box">
                        <span style="text-transform:uppercase; color:#d4af37; font-weight:700; font-size:12px;">{cat}</span>
                        <h1 style="font-size:40px; margin:10px 0;">{p_name}</h1>
                        <p class="fees" style="font-size:24px;">{p_fees}</p>
                        <p style="font-size:18px; line-height:1.8; color:#444;">{p_desc}</p>
                        
                        <h3>Exclusive Benefits</h3>
                        <ul class="benefit-list">{benefits_html}</ul>
                        
                        <div style="background:#f9f9f9; padding:30px; margin-top:40px;">
                            <h3>Eligibility Criteria</h3>
                            <p>Applicants must be over 18 years of age with a valid government ID and proof of stable income. Subject to internal credit checks.</p>
                            <button class="btn" style="width:100%; margin-top:20px; font-size:18px;">APPLY NOW</button>
                        </div>
                        
                        <div class="terms">
                            <p><strong>Terms & Conditions:</strong> Interest rates are subject to change. Fees listed above are based on regular usage. Please read the offer document carefully before applying.nexus Digital Bank reserves the right to approve or reject any application at its sole discretion.</p>
                        </div>
                    </div>
                </div>
                <footer><p>&copy; 2026 Nexus Digital Bank. Member FDIC. Equal Housing Lender.</p></footer>
            </body>
            </html>
            """)

print("Successfully generated Banking site with 42 pages.")
