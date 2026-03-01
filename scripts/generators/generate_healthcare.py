import os

SITE_DIR = "test-sites/healthcare"
os.makedirs(SITE_DIR, exist_ok=True)

CATEGORIES = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Diagnostics"]
SERVICES = {
    "Cardiology": [
        ("Heart Bypass Surgery", "Rs. 3.5L - 6L", "Highly advanced CABG for heart health.", ["24/7 Monitoring", "Expert Surgeons", "Post-op Care"]),
        ("Angioplasty", "Rs. 1.2L - 2.5L", "Minimally invasive blocked artery treatment.", ["Instant Recovery", "Zero Stitiching", "Same-day Discharge"]),
        ("Heart Valve Repair", "Rs. 2L - 4L", "Replacement or repair of heart valves.", ["robotic assisted", "minimally invasive", "long term relief"]),
        ("ECG & Stress Test", "Rs. 500 - 3,000", "Routine heart health evaluation.", ["Expert Analysis", "Zero Risk", "Pre-admission Mandatory"]),
        ("Pacemaker Installation", "Rs. 1.5L onwards", "Regulate heart rhythm automatically.", ["Imported Devices", "Minimal Scare", "Life-long Support"]),
        ("Heart Failure Program", "Consultation-based", "Ongoing management for chronic failure.", ["Dietary Guidance", "Tele-monitoring", "Medication Management"]),
        ("Pediatric Cardiology", "Consultation-based", "Specialized care for children's hearts.", ["Child-friendly environment", "Expert Pediatricians", "Early Diagnosis"]),
        ("TAVI Procedure", "Rs. 15L onwards", "Non-surgical valve replacement.", ["High Tech", "Safe for Seniors", "Advanced Lab"]),
    ],
    "Neurology": [
        ("Brain Tumor Surgery", "Rs. 4L - 10L", "Precision removal of neurological growths.", ["Neuro-navigation", "ICU Support", "Cognitive Rehab"]),
        ("Epilepsy Management", "Rs. 1k - 5k/mo", "Long term management of seizures.", ["EEG Monitoring", "Advanced Medication", "Support Groups"]),
        ("Stroke Rehabilitation", "Rs. 50k - 2L", "Recovering motor skills post-stroke.", ["Physiotherapy", "Speech Therapy", "Occupational Support"]),
        ("Migraine Clinic", "Rs. 1,500/session", "Finding the root cause of chronic pain.", ["Botox Therapy", "Trigger Identification", "Long-term Relief"]),
        ("Sleep Study", "Rs. 10,000", "Diagnosing apnea and insomnia.", ["Overnight Monitoring", "Comfortable Suites", "Full Analysis"]),
        ("Dementia Care", "Consultation-based", "Compassionate care for elderly memory loss.", ["Memory Training", "Family Counseling", "Safety Audits"]),
        ("Spine Surgery", "Rs. 2.5L - 5L", "Treatment for disc herniation.", ["Laser Treatment", "Microscopic Surgery", "Recovery Focus"]),
        ("Neuropathy Program", "Rs. 2,000/mo", "Managing nerve pain and damage.", ["Pain Management", "Exercise Therapy", "NCS/EMG Diagnostics"]),
    ],
    "Orthopedics": [
        ("Knee Replacement", "Rs. 1.8L - 3.5L", "Total or partial robotic knee arthroplasty.", ["High Mobility", "Robotic Accuracy", "Physio Included"]),
        ("Hip Replacement", "Rs. 2L - 4L", "Restoring mobility with advanced implants.", ["Ceramic Implants", "Minimal Blood Loss", "Life-long Durability"]),
        ("Arthroscopy", "Rs. 80k - 1.5L", "Keyhole surgery for joint injuries.", ["Sports Medicine", "Day Care Setup", "Rapid Recovery"]),
        ("Fracture Casting", "Rs. 2,000 - 15,000", "Basic to advanced stabilization of bones.", ["Lightweight Fiber Casts", "Pain Management", "X-ray Monitoring"]),
        ("Physiotherapy Hub", "Rs. 800/session", "Recovery from sports or lifestyle injuries.", ["Certified Therapists", "Modern Equipment", "Home Visits"]),
        ("Scoliosis Correction", "Rs. 5L onwards", "Spinal alignment for structural health.", ["Complex Surgery", "ICU Support", "Supportive Bracing"]),
        ("Shoulder Dislocation", "Rs. 60k - 1L", "Tendon and ligament stabilization.", ["Sling Support", "Strengthening Focus", "Surgical Repair"]),
        ("Geriatric Ortho", "Consultation", "Specialized care for aging joints.", ["Fall Prevention", "Osteoporosis Treatment", "Comfort Priority"]),
    ],
    "Pediatrics": [
        ("Newborn Care", "Consultation", "Comprehensive checkups for infants.", ["Vaccination Schedule", "Growth Tracking", "Nutrition Guide"]),
        ("Pediatric Vaccination", "Per Kit Price", "Shielding child from common diseases.", ["Painless Vaccines", "Cold Chain Maintained", "Expert Admin"]),
        ("Asthma Care Child", "Consultation", "Management of pediatric respiratory issues.", ["Inhaler Training", "Allergy Test", "Ongoing Support"]),
        ("Developmental Clinic", "Consultation", "Tracking milestones and behavior.", ["Learning Support", "Speech Delay", "Behavioral Therapy"]),
        ("Childhood Obesity", "Program-based", "Guiding healthy eating and activity.", ["Dietary Chart", "Exercise Plan", "Psychological Support"]),
        ("Pediatric Surgery", "Condition-based", "Specialized surgery for young ones.", ["NICU/PICU Support", "Kid-sized Tools", "Expert Surgeons"]),
        ("Adolescent Health", "Consultation", "Counseling and health for teenagers.", ["Mental Health", "Hormonal Support", "Privacy Focus"]),
        ("Pediatric Dentistry", "Rs. 1k onwards", "Root canals and hygiene for kids.", ["Sedation Option", "Gently Cleaning", "Cavity Check"]),
    ],
    "Diagnostics": [
        ("Full Body Checkup", "Rs. 5,000", "Comprehensive 60+ parameter test.", ["Fast Results", "Consultation Included", "Home Sample"]),
        ("MRI Scan 3 Tesla", "Rs. 8,000 - 15,000", "High resolution imaging of internal organs.", ["Silent MRI", "Clear Images", "Specialist Report"]),
        ("CT Scan MultiSlice", "Rs. 4,000 - 10,000", "Cross-sectional imaging for diagnosis.", ["Low Radiation", "Fast Scan", "Detailed Report"]),
        ("Ultrasound Abdomen", "Rs. 1,500 - 3,500", "Non-invasive sound wave imaging.", ["No Prep Needed", "Live Preview", "Instant Results"]),
        ("Biopsy Service", "Rs. 5,000 onwards", "Tissue analysis for cellular diagnosis.", ["Local Anesthesia", "Cancer Screening", "Expert Pathologists"]),
        ("Allergy Panel", "Rs. 4,500", "Testing for 100+ common allergens.", ["Blood Test", "Dietary Advice", "Long Term Management"]),
        ("Blood Culture", "Rs. 1,200", "Identifying infections in blood.", ["48hr Results", "Sensitivity Test", "Accuracy Focus"]),
        ("X-Ray Digital", "Rs. 500 - 2,500", "Quick bone and chest imaging.", ["Immediate Film", "Low Dose", "Universal Access"]),
    ]
}

CSS = """
body { font-family: 'Poppins', sans-serif; margin: 0; padding: 0; background: #f0f7f4; color: #2c3e50; }
header { background: #fff; padding: 20px 50px; display: flex; justify-content: space-between; align-items: center; border-bottom: 5px solid #27ae60; position: sticky; top: 0; z-index: 1000; }
nav ul { list-style: none; display: flex; gap: 20px; }
nav a { text-decoration: none; color: #34495e; font-weight: 600; font-size: 15px; }
nav a:hover { color: #27ae60; }
.logo { font-size: 24px; font-weight: 800; color: #27ae60; text-decoration: none; }
.container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
.hero { background: #2ecc71; color: #fff; padding: 80px 40px; border-radius: 40px 0 40px 0; text-align: center; margin-bottom: 50px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }
.card { background: #fff; border-radius: 20px; padding: 30px; border: 1px solid #e0e0e0; transition: all 0.3s; }
.card:hover { transform: scale(1.02); box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
.card-title { color: #27ae60; font-size: 20px; font-weight: 700; margin-bottom: 10px; }
.cost { background: #f1f8e9; display: inline-block; padding: 5px 15px; border-radius: 20px; color: #2ecc71; font-weight: 700; margin-bottom: 15px; }
.btn { background: #27ae60; color: #fff; padding: 12px 25px; border-radius: 30px; text-decoration: none; font-weight: 600; display: inline-block; }
.service-header { display: flex; gap: 40px; background: #fff; padding: 40px; border-radius: 30px; margin-bottom: 40px; align-items: center; }
.info-section { margin-top: 40px; background: #fff; padding: 40px; border-radius: 30px; }
footer { background: #2c3e50; color: #ecf0f1; padding: 50px 40px; text-align: center; }
"""

def generate_header(active_cat=None):
    links = ""
    for cat in CATEGORIES:
        active = "style='color:#27ae60'" if cat == active_cat else ""
        links += f"<li><a href='{cat.lower()}.html' {active}>{cat}</a></li>"
    
    return f"""
    <header>
        <a href="index.html" class="logo">CarePoint Multispecialty</a>
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
        <meta charset="UTF-8"><title>CarePoint Hospital | Patient First Healthcare</title>
        <style>{CSS}</style>
        <script src="http://localhost:8000/sdk/loader.js" data-site-id="77777777-7777-4777-7777-777777777777"></script>
    </head>
    <body>
        {generate_header()}
        <div class="container">
            <div class="hero">
                <h1>Compassion & Clinical Excellence.</h1>
                <p>World class treatment from top doctors across 50+ specialities.</p>
                <a href="#departments" class="btn" style="background:#fff; color:#27ae60">View Departments</a>
            </div>
            <h2 id="departments">Speciality Departments</h2>
            <div class="grid">
                {"".join([f'<a href="{c.lower()}.html" class="card" style="text-decoration:none; color:inherit"><h3 class="card-title">{c}</h3><p>Leading the way in advanced {c.lower()} care.</p></a>' for c in CATEGORIES])}
            </div>
        </div>
        <footer><p>&copy; 2026 CarePoint Multispecialty Hospital. Accredited by NABH.</p></footer>
    </body>
    </html>
    """)

# 2. Create Category Pages
for cat in CATEGORIES:
    services_html = ""
    for s_name, s_cost, s_desc, s_info in SERVICES[cat]:
        file_name = f"service-{s_name.lower().replace(' ', '-')}.html"
        services_html += f"""
        <div class="card">
            <h3 class="card-title">{s_name}</h3>
            <p class="cost">{s_cost}</p>
            <p>{s_desc}</p>
            <a href="{file_name}" class="btn">Learn More</a>
        </div>
        """
    
    with open(f"{SITE_DIR}/{cat.lower()}.html", "w", encoding="utf-8") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8"><title>{cat} Services | CarePoint</title>
            <style>{CSS}</style>
            <script src="http://localhost:8000/sdk/loader.js" data-site-id="77777777-7777-4777-7777-777777777777"></script>
        </head>
        <body>
            {generate_header(cat)}
            <div class="container">
                <h1>{cat} Speciality Services</h1>
                <div class="grid">{services_html}</div>
            </div>
        </body>
        </html>
        """)

# 3. Create Service Pages
for cat in CATEGORIES:
    for s_name, s_cost, s_desc, s_info in SERVICES[cat]:
        file_name = f"service-{s_name.lower().replace(' ', '-')}.html"
        info_html = "".join([f"<li>{item}</li>" for item in s_info])
        
        with open(f"{SITE_DIR}/{file_name}", "w", encoding="utf-8") as f:
            f.write(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8"><title>{s_name} | CarePoint</title>
                <style>{CSS}</style>
                <script src="http://localhost:8000/sdk/loader.js" data-site-id="77777777-7777-4777-7777-777777777777"></script>
            </head>
            <body>
                {generate_header(cat)}
                <div class="container">
                    <div class="service-header">
                        <div style="flex:1; padding:40px; background:#f9f9f9; border-radius:30px; text-align:center; font-size:18px; color:#aaa;">Department: {cat}</div>
                        <div style="flex:2;">
                            <h1 style="font-size:36px; margin:0 0 20px 0;">{s_name}</h1>
                            <div class="cost">{s_cost}</div>
                            <p style="font-size:18px; line-height:1.7;">{s_desc}</p>
                            <button class="btn" style="padding:15px 40px; font-size:18px;">BOOK APPOINTMENT</button>
                        </div>
                    </div>
                    <div class="info-section">
                        <h3>Key Features of Treatment</h3>
                        <ul style="font-size:16px; line-height:2;">{info_html}</ul>
                        
                        <div style="margin-top:40px; padding:30px; border-top:1px solid #eee;">
                            <h3>Symptoms Treated</h3>
                            <p>This procedure is recommended for patients experiencing chronic discomfort, functional impairment, or as suggested by a primary specialist.</p>
                        </div>
                    </div>
                </div>
                <footer><p>&copy; 2026 CarePoint Multispecialty Hospital. Accredited by NABH.</p></footer>
            </body>
            </html>
            """)

print("Successfully generated Healthcare site with 41 pages.")
