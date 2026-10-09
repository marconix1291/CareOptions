import os

index_file = r"z:\Marco\WebProjects\CareOptions\index.html"
css_file = r"z:\Marco\WebProjects\CareOptions\css\style.css"
services_dir = r"z:\Marco\WebProjects\CareOptions\services"

with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace the sections
import re
new_services_section = """    <section class="services section" id="services">
        <div class="section-header">
            <h2>Our Services</h2>
            <p>Individualized health care and specialized therapies designed around your specific needs.</p>
        </div>
        <div class="services-grid">
            <a href="services/integrative-medicine.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">🌱</div>
                    <h3>Integrative Medicine</h3>
                    <p>Blending Western and functional measures for a holistic approach to your health.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
            <a href="services/chronic-condition-management.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">🩺</div>
                    <h3>Chronic Condition Management</h3>
                    <p>Expert, long-term management of chronic conditions to improve your quality of life.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
            <a href="services/wellness-and-nutrition.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">🥗</div>
                    <h3>Wellness & Nutrition Support</h3>
                    <p>Guidance and support to achieve optimal health through proper nutrition.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
            <a href="services/red-light-therapy.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">🔴</div>
                    <h3>Red Light Therapy</h3>
                    <p>Innovative light therapy treatments to promote healing and reduce inflammation.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
            <a href="services/lab-work.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">🔬</div>
                    <h3>Lab Work</h3>
                    <p>Comprehensive laboratory testing and diagnostics for precise treatment plans.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
            <a href="services/nutraceuticals.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">💊</div>
                    <h3>Nutraceuticals & Supplements</h3>
                    <p>High-quality nutritional, herbal, and vitamin/mineral support.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
            <a href="services/well-woman-exams.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">🌸</div>
                    <h3>Well Woman Exams</h3>
                    <p>Comprehensive preventative care and exams tailored for women's health.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
            <a href="services/hormone-replacement-therapy.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">⚖️</div>
                    <h3>Hormone Replacement Therapy</h3>
                    <p>Restoring hormonal balance to improve energy, mood, and overall vitality.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
            <a href="services/bioidentical-hormone-pellets.html" class="service-card-link">
                <div class="service-card">
                    <div class="service-icon">💉</div>
                    <h3>Bioidentical Hormone Pellets</h3>
                    <p>Steady, consistent symptom relief through advanced pellet therapy.</p>
                    <span class="learn-more">Learn More &rarr;</span>
                </div>
            </a>
        </div>
    </section>"""

# We can find the start of <section class="services section" id="services"> and the end of </section> for therapies
start_idx = index_content.find('<section class="services section" id="services">')
end_idx = index_content.find('</section>', index_content.find('<section class="therapies section" id="therapies"')) + 10

if start_idx != -1 and end_idx != -1 + 10:
    index_content = index_content[:start_idx] + new_services_section + index_content[end_idx:]
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_content)
    print("Updated index.html")
else:
    print("Could not find sections in index.html")

# Update CSS
with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

new_css = """/* --- Services Grid --- */
.service-card-link {
    display: block;
    text-decoration: none;
    color: inherit;
}
.learn-more {
    display: inline-block;
    margin-top: 1.5rem;
    color: var(--clr-secondary-3);
    font-weight: 600;
    font-size: 0.95rem;
    transition: var(--transition-smooth);
}
.service-card:hover .learn-more {
    color: var(--clr-primary);
    transform: translateX(5px);
}
.services-grid {"""

css_content = css_content.replace("/* --- Services Grid --- */\n.services-grid {", new_css)
with open(css_file, "w", encoding="utf-8") as f:
    f.write(css_content)
print("Updated style.css")

# Generate the 9 pages
services = [
    {"slug": "integrative-medicine", "title": "Integrative Medicine", "icon": "🌱", "desc": "Blending Western and functional measures for a holistic approach to your health."},
    {"slug": "chronic-condition-management", "title": "Chronic Condition Management", "icon": "🩺", "desc": "Expert, long-term management of chronic conditions to improve your quality of life."},
    {"slug": "wellness-and-nutrition", "title": "Wellness & Nutrition Support", "icon": "🥗", "desc": "Guidance and support to achieve optimal health through proper nutrition."},
    {"slug": "red-light-therapy", "title": "Red Light Therapy", "icon": "🔴", "desc": "Innovative light therapy treatments to promote healing and reduce inflammation."},
    {"slug": "lab-work", "title": "Lab Work", "icon": "🔬", "desc": "Comprehensive laboratory testing and diagnostics for precise treatment plans."},
    {"slug": "nutraceuticals", "title": "Nutraceuticals & Supplements", "icon": "💊", "desc": "High-quality nutritional, herbal, and vitamin/mineral support."},
    {"slug": "well-woman-exams", "title": "Well Woman Exams", "icon": "🌸", "desc": "Comprehensive preventative care and exams tailored for women's health."},
    {"slug": "hormone-replacement-therapy", "title": "Hormone Replacement Therapy", "icon": "⚖️", "desc": "Restoring hormonal balance to improve energy, mood, and overall vitality."},
    {"slug": "bioidentical-hormone-pellets", "title": "Bioidentical Hormone Pellets", "icon": "💉", "desc": "Steady, consistent symptom relief through advanced pellet therapy."},
]

template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Care Options LLC</title>
    <meta name="description" content="{desc}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
    <style>
        .service-hero {
            min-height: 50vh;
            padding-top: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background: var(--grad-primary);
            color: var(--white);
            position: relative;
            overflow: hidden;
        }
        .service-hero::before {
            content: '{icon}';
            position: absolute;
            font-size: 20rem;
            opacity: 0.05;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }
        .service-hero h1 {
            font-size: 3.5rem;
            color: var(--white);
            margin-bottom: 1rem;
            position: relative;
            z-index: 1;
        }
        .service-hero p {
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }
        .service-content {
            max-width: 900px;
            margin: 0 auto;
            padding: 6rem 2rem;
            background: var(--white);
            border-radius: 20px;
            margin-top: -50px;
            position: relative;
            z-index: 10;
            box-shadow: var(--shadow-lg);
            margin-bottom: 6rem;
        }
        .service-content h2 {
            color: var(--clr-primary);
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }
        .service-content p {
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
            color: var(--text-dark);
            line-height: 1.8;
        }
        .service-content ul {
            margin-bottom: 2rem;
            padding-left: 1.5rem;
        }
        .service-content ul li {
            margin-bottom: 1rem;
            font-size: 1.1rem;
            color: var(--text-dark);
        }
        .back-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 2rem;
            color: var(--clr-primary);
            font-weight: 600;
            transition: var(--transition-smooth);
        }
        .back-link:hover {
            color: var(--clr-secondary-1);
            transform: translateX(-5px);
        }
    </style>
</head>

<body>
    <nav class="navbar scrolled" id="navbar">
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <div class="logo-icon"></div>
                Care Options<span>LLC</span>
            </a>
            <div class="nav-links">
                <a href="../index.html#home">Home</a>
                <a href="../index.html#about">About</a>
                <a href="../index.html#services">Services</a>
                <a href="../index.html#contact">Contact</a>
                <a href="http://www.docpay.com/careoptions" target="_blank">Pay Bill</a>
            </div>
            <a href="tel:8068771474" class="btn btn-primary">806.877.1474</a>
        </div>
    </nav>

    <header class="service-hero">
        <div>
            <h1>{title}</h1>
            <p>{desc}</p>
        </div>
    </header>

    <main class="service-content">
        <a href="../index.html#services" class="back-link">&larr; Back to all Services</a>
        
        <h2>About {title}</h2>
        <p>At Care Options LLC, we are committed to providing you with the highest quality {title}. Our approach is patient-centered, meaning we listen to your concerns, understand your unique health profile, and develop a customized plan.</p>
        <p>{desc}</p>
        
        <h2>Key Benefits</h2>
        <ul>
            <li>Personalized care plans tailored to your specific needs.</li>
            <li>Comprehensive evaluation and ongoing support.</li>
            <li>Focus on long-term wellness and improved quality of life.</li>
            <li>Expert guidance from our experienced provider, Deni Berry, FNP.</li>
        </ul>

        <div style="text-align: center; margin-top: 4rem;">
            <h3 style="color: var(--clr-primary); margin-bottom: 1rem; font-size: 1.8rem;">Ready to get started?</h3>
            <a href="../index.html#contact" class="btn btn-primary" style="padding: 1rem 3rem; font-size: 1.2rem;">Book an Appointment</a>
        </div>
    </main>

    <footer id="contact">
        <div class="footer-content">
            <div class="footer-contact">
                <h3>Drop us a line!</h3>
                <p style="color: var(--clr-secondary-5); margin-bottom: 1rem;">Phone: <a href="tel:8068771474" style="color: white;">806.877.1474</a></p>
            </div>
            <div class="footer-hours">
                <a href="../index.html" class="logo footer-logo">
                    Care Options<span>LLC</span>
                </a>
                <p>Deni Berry, FNP Primary Care Services.</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Care Options LLC. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""

os.makedirs(services_dir, exist_ok=True)
for s in services:
    filepath = os.path.join(services_dir, s['slug'] + '.html')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template.format(**s))
    print(f"Created {filepath}")

print("All done!")
