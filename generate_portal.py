#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portal V3 Master Generator for Eng. Mostafa Abdelghany
Generates all 9 interconnected, bilingual HTML files cleanly.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_head(title):
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Eng. Mostafa Abdelghany — MEP Procurement Section Head & Engineering Consultant | SAR 2.63B+ Mega-Projects Experience">
    <meta name="keywords" content="MEP Procurement, Construction, Saudi Arabia, Egypt, Portfolio, Freelance Consultant, Engineering">
    <meta name="author" content="Eng. Mostafa Abdelghany">
    <title>{title}</title>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cairo:wght@300;400;600;700;800;900&family=Playfair+Display:wght@400;600;700;800&display=swap" rel="stylesheet">

    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

    <!-- Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />

    <!-- Core Stylesheets -->
    <link rel="stylesheet" href="styles/main.css">
    <link rel="stylesheet" href="styles/pages.css">
    <link rel="stylesheet" href="styles/animations.css">
    <link rel="stylesheet" href="styles/responsive.css">
</head>
<body>
    <div id="scroll-progress"></div>
"""

def get_navbar(active_page="index.html"):
    return f"""
    <!-- ============ GLOBAL NAVBAR ============ -->
    <nav id="navbar" class="navbar">
        <div class="nav-container">
            <a href="index.html" class="nav-logo">
                <span class="logo-text">M</span><span class="logo-dot">.</span><span class="logo-text">A</span>
            </a>
            <ul class="nav-links" id="nav-links">
                <li><a href="index.html" class="nav-link {'active' if active_page=='index.html' else ''}" data-en="Home" data-ar="الرئيسية">Home</a></li>
                <li><a href="about.html" class="nav-link {'active' if active_page=='about.html' else ''}" data-en="About" data-ar="نبذة عني">About</a></li>
                <li><a href="services.html" class="nav-link {'active' if active_page=='services.html' else ''}" data-en="Services & Freelance" data-ar="الخدمات والفريلانس">Services & Freelance</a></li>
                <li><a href="projects.html" class="nav-link {'active' if active_page=='projects.html' or active_page=='project-detail.html' else ''}" data-en="Projects" data-ar="المشاريع">Projects</a></li>
                <li><a href="software.html" class="nav-link {'active' if active_page=='software.html' else ''}" data-en="Software Stack" data-ar="البرامج والأدوات">Software Stack</a></li>
                <li><a href="experience.html" class="nav-link {'active' if active_page=='experience.html' else ''}" data-en="Experience" data-ar="المسيرة المهنية">Experience</a></li>
                <li><a href="certificates.html" class="nav-link {'active' if active_page=='certificates.html' else ''}" data-en="Certificates" data-ar="الشهادات">Certificates</a></li>
                <li><a href="contact.html" class="nav-link {'active' if active_page=='contact.html' else ''}" data-en="Contact" data-ar="تواصل وتعاقد">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <button id="lang-toggle" class="nav-btn" title="Toggle Language">
                    <span>AR</span>
                </button>
                <button id="theme-toggle" class="nav-btn" title="Toggle Theme">
                    <i class="fas fa-moon"></i>
                </button>
                <a href="contact.html" class="btn btn-sm btn-primary magnetic-btn nav-cta-btn" style="padding: 8px 16px; font-size: 0.82rem;">
                    <i class="fas fa-briefcase"></i> <span data-en="Hire Me" data-ar="طلب استشارة">Hire Me</span>
                </a>
                <button class="hamburger" id="hamburger" aria-label="Toggle navigation">
                    <span></span><span></span><span></span>
                </button>
            </div>
        </div>
    </nav>
"""

def get_footer(extra_scripts=""):
    return f"""
    <!-- ============ GLOBAL FOOTER ============ -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div style="display: flex; justify-content: center; align-items: center; gap: 15px; margin-bottom: 15px; flex-wrap: wrap;">
                    <a href="index.html" style="color: var(--gold-primary); font-weight: 700;">Home</a> •
                    <a href="about.html" style="color: var(--text-secondary);">About</a> •
                    <a href="services.html" style="color: var(--text-secondary);">Services & Freelance</a> •
                    <a href="projects.html" style="color: var(--text-secondary);">Projects</a> •
                    <a href="software.html" style="color: var(--text-secondary);">Software</a> •
                    <a href="experience.html" style="color: var(--text-secondary);">Experience</a> •
                    <a href="certificates.html" style="color: var(--text-secondary);">Certificates</a> •
                    <a href="contact.html" style="color: var(--text-secondary);">Contact</a>
                </div>
                <p data-en="Eng. Mostafa Abdelghany — MEP Procurement Section Head & Engineering Consultant" data-ar="م. مصطفى عبدالغني — رئيس قسم مشتريات MEP واستشاري هندسي">
                    Eng. Mostafa Abdelghany — MEP Procurement Section Head & Engineering Consultant
                </p>
                <div class="footer-links">
                    <a href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
                    <a href="https://wa.me/966502582122" target="_blank" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
                    <a href="mailto:engmostafamahoud2012@gmail.com" title="Email"><i class="fas fa-envelope"></i></a>
                    <a href="tel:+966502582122" title="Phone"><i class="fas fa-phone"></i></a>
                </div>
                <p class="footer-copy">&copy; 2026 Eng. Mostafa Abdelghany. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Floating CV Button -->
    <a href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download id="cv-float-btn" class="cv-float-btn" title="Download CV">
        <i class="fas fa-download"></i>
        <span data-en="CV" data-ar="السيرة">CV</span>
    </a>

    <!-- Leaflet JS -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

    <!-- Core Scripts -->
    <script src="scripts/projects-data.js"></script>
    <script src="scripts/main.js"></script>
    <script src="scripts/animations.js"></script>
    {extra_scripts}
</body>
</html>
"""

# ----------------- PAGE GENERATORS -----------------

def build_index():
    body = """
    <!-- ============ HERO SECTION WITH KAIG FADE THEME ============ -->
    <section class="hero-kaig-theme">
        <div class="hero-bg-media">
            <img src="assets/images/kaig_hero_bg.jpg" alt="King Abdullah International Gardens Mega Project Background">
        </div>
        <div class="hero-gradient-overlay"></div>
        <div id="particles-container" class="particles-bg"></div>

        <div class="hero-content" style="z-index: 2;">
            <div class="hero-text">
                <div style="display: inline-flex; align-items: center; gap: 8px; padding: 6px 16px; background: rgba(196,163,90,0.15); border: 1px solid rgba(196,163,90,0.3); border-radius: 20px; font-size: 0.85rem; color: var(--gold-light); margin-bottom: 20px;" class="animate-on-scroll">
                    <i class="fas fa-gem" style="color: var(--gold-primary);"></i>
                    <span data-en="Mega-Projects Procurement Leader • SAR 2.63B Managed" data-ar="قيادة مشتريات المشاريع الكبرى • إدارة مشاريع بـ 2.63 مليار ريال">Mega-Projects Procurement Leader • SAR 2.63B Managed</span>
                </div>

                <h1 class="hero-name animate-on-scroll" style="font-size: 3.6rem;">
                    <span data-en="Eng. Mostafa" data-ar="م. مصطفى">Eng. Mostafa</span>
                    <span class="gold-text" data-en="Abdelghany" data-ar="عبدالغني">Abdelghany</span>
                </h1>

                <div class="typewriter-container animate-on-scroll">
                    <span class="typewriter-prefix" data-en="Specialized in " data-ar="متخصص في ">Specialized in </span>
                    <span id="typewriter-text" class="typewriter-text"></span>
                    <span class="typewriter-cursor">|</span>
                </div>

                <p class="hero-desc animate-on-scroll" data-en="MEP Procurement Section Head at Zaid Al Hussain Group, Riyadh. Delivering end-to-end procurement mastery, value engineering, and high-stakes vendor negotiations across KSA & Egypt with over 9 years of proven track record." data-ar="رئيس قسم مشتريات أعمال MEP بمجموعة زيد الحصين، الرياض. خبرة هندسية واستراتيجية تتجاوز 9 سنوات في قيادة مشتريات المشاريع المليارية، وهندسة القيمة، وإدارة العقود الكبرى في السعودية ومصر.">
                    MEP Procurement Section Head at Zaid Al Hussain Group, Riyadh. Delivering end-to-end procurement mastery, value engineering, and high-stakes vendor negotiations across KSA & Egypt with over 9 years of proven track record.
                </p>

                <div class="hero-btns animate-on-scroll">
                    <a href="projects.html" class="btn btn-primary magnetic-btn">
                        <i class="fas fa-layer-group"></i>
                        <span data-en="Explore 14+ Projects" data-ar="استكشف كافة المشاريع (14)">Explore 14+ Projects</span>
                    </a>
                    <a href="services.html" class="btn btn-outline magnetic-btn">
                        <i class="fas fa-handshake"></i>
                        <span data-en="Freelance & Consulting" data-ar="خدمات الفريلانس والاستشارات">Freelance & Consulting</span>
                    </a>
                    <a href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download class="btn btn-sm btn-outline magnetic-btn" style="border-color: rgba(255,255,255,0.3); color: #fff;">
                        <i class="fas fa-file-pdf"></i>
                        <span data-en="Download CV" data-ar="تحميل CV">Download CV</span>
                    </a>
                </div>

                <div class="hero-badges animate-on-scroll" style="margin-top: 25px;">
                    <span class="badge"><i class="fas fa-map-marker-alt"></i> <span data-en="Riyadh, Saudi Arabia" data-ar="الرياض، السعودية">Riyadh, Saudi Arabia</span></span>
                    <span class="badge"><i class="fas fa-id-card"></i> SCE #1084929</span>
                    <span class="badge"><i class="fas fa-check-circle" style="color: var(--accent-teal);"></i> Available for Freelance & Consulting</span>
                </div>
            </div>

            <div class="hero-image animate-on-scroll">
                <div class="profile-square-frame">
                    <div class="img-container">
                        <img src="assets/images/headshot.jpg" alt="Eng. Mostafa Abdelghany">
                    </div>
                    <div class="frame-border-outer"></div>
                    <div class="frame-accent-corner corner-tl"></div>
                    <div class="frame-accent-corner corner-br"></div>
                    <div class="frame-badge-experience">
                        <i class="fas fa-award"></i>
                        <span>9+ Years Experience</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ KPI STATISTICS COUNTERS ============ -->
    <section class="section" style="padding: 60px 0; background: var(--bg-secondary); border-top: 1px solid rgba(196,163,90,0.15); border-bottom: 1px solid rgba(196,163,90,0.15);">
        <div class="container">
            <div class="kpi-grid">
                <div class="kpi-card animate-on-scroll">
                    <div class="kpi-icon"><i class="fas fa-landmark"></i></div>
                    <span class="kpi-number" data-target="14">0</span>
                    <span class="kpi-label" data-en="Mega & Prime Projects" data-ar="مشروعاً عملاقاً ورئيسياً">Mega & Prime Projects</span>
                </div>
                <div class="kpi-card animate-on-scroll">
                    <div class="kpi-icon"><i class="fas fa-business-time"></i></div>
                    <span class="kpi-number" data-target="9" data-suffix="+">0</span>
                    <span class="kpi-label" data-en="Years of Proven Mastery" data-ar="سنوات من الخبرة والتميز">Years of Proven Mastery</span>
                </div>
                <div class="kpi-card animate-on-scroll">
                    <div class="kpi-icon"><i class="fas fa-building-circle-check"></i></div>
                    <span class="kpi-number" data-target="5">0</span>
                    <span class="kpi-label" data-en="Top Construction Firms" data-ar="كبرى شركات المقاولات">Top Construction Firms</span>
                </div>
                <div class="kpi-card animate-on-scroll">
                    <div class="kpi-icon"><i class="fas fa-vault"></i></div>
                    <span class="kpi-number" data-target="2.63" data-prefix="SAR " data-suffix="B" data-decimal="true">0</span>
                    <span class="kpi-label" data-en="Flagship Project Value" data-ar="قيمة المشروع القيادي (KAIG)">Flagship Project Value</span>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ QUICK EXPLORATION HUB ============ -->
    <section class="section">
        <div class="container">
            <div style="text-align: center; max-width: 750px; margin: 0 auto 50px;" class="animate-on-scroll">
                <h2 class="section-title" style="justify-content: center; margin-bottom: 15px;">
                    <span class="title-number">01.</span>
                    <span data-en="Explore Portfolio Hub" data-ar="بوابة الاستكشاف السريع">Explore Portfolio Hub</span>
                </h2>
                <p style="color: var(--text-secondary); font-size: 1.05rem;" data-en="Navigate directly to specialized sections of Eng. Mostafa's comprehensive engineering portal." data-ar="انتقل مباشرة إلى الأقسام التخصصية في البوابة الهندسية للمهندس مصطفى.">
                    Navigate directly to specialized sections of Eng. Mostafa's comprehensive engineering portal.
                </p>
            </div>

            <div class="hub-shortcuts-grid">
                <!-- Card 1: Projects -->
                <a href="projects.html" class="hub-card animate-on-scroll">
                    <div>
                        <div class="hub-icon"><i class="fas fa-layer-group"></i></div>
                        <h3 class="hub-title" data-en="Projects Directory" data-ar="دليل المشاريع الشامل">Projects Directory</h3>
                        <p class="hub-desc" data-en="Explore all 14 iconic projects across KSA & Egypt with interactive filters and high-res image galleries." data-ar="تصفح جميع المشاريع الـ 14 في السعودية ومصر مع فلاتر تفاعلية ومعارض صور عالية الدقة.">
                            Explore all 14 iconic projects across KSA & Egypt with interactive filters and high-res image galleries.
                        </p>
                    </div>
                    <div class="hub-link-action">
                        <span data-en="View All Projects" data-ar="عرض كافة المشاريع">View All Projects</span>
                        <i class="fas fa-arrow-right"></i>
                    </div>
                </a>

                <!-- Card 2: Services & Freelance -->
                <a href="services.html" class="hub-card animate-on-scroll">
                    <div>
                        <div class="hub-icon"><i class="fas fa-handshake-simple"></i></div>
                        <h3 class="hub-title" data-en="Services & Freelance" data-ar="خدمات واستشارات الفريلانس">Services & Freelance</h3>
                        <p class="hub-desc" data-en="MEP Procurement Management, Value Engineering, BOQ preparation, and tailored consulting for contractors & developers." data-ar="إدارة مشتريات MEP، هندسة القيمة وتخفيض التكاليف، وإعداد جداول الكميات والاستشارات للمطورين.">
                            MEP Procurement Management, Value Engineering, BOQ preparation, and tailored consulting for contractors & developers.
                        </p>
                    </div>
                    <div class="hub-link-action">
                        <span data-en="Hire / Request Quote" data-ar="طلب استشارة / تعاقد">Hire / Request Quote</span>
                        <i class="fas fa-arrow-right"></i>
                    </div>
                </a>

                <!-- Card 3: Software Stack -->
                <a href="software.html" class="hub-card animate-on-scroll">
                    <div>
                        <div class="hub-icon"><i class="fas fa-laptop-code"></i></div>
                        <h3 class="hub-title" data-en="Software Stack" data-ar="البرامج والأدوات الهندسية">Software Stack</h3>
                        <p class="hub-desc" data-en="Mastery in Primavera P6, AutoCAD, BIM/Revit, Oracle ERP, SAP, MS Project, and advanced financial modeling." data-ar="إتقان برامج بريمافيرا P6، الأوتوكاد، BIM/Revit، أنظمة أوراكل و SAP ERP ونماذج التكاليف المتقدمة.">
                            Mastery in Primavera P6, AutoCAD, BIM/Revit, Oracle ERP, SAP, MS Project, and advanced financial modeling.
                        </p>
                    </div>
                    <div class="hub-link-action">
                        <span data-en="Explore Tech Stack" data-ar="استعراض الأدوات والبرمجيات">Explore Tech Stack</span>
                        <i class="fas fa-arrow-right"></i>
                    </div>
                </a>

                <!-- Card 4: About & Philosophy -->
                <a href="about.html" class="hub-card animate-on-scroll">
                    <div>
                        <div class="hub-icon"><i class="fas fa-user-gear"></i></div>
                        <h3 class="hub-title" data-en="About & Expertise" data-ar="نبذة عن المهندس">About & Expertise</h3>
                        <p class="hub-desc" data-en="Deep dive into Eng. Mostafa's procurement methodology, technical leadership, and engineering credentials." data-ar="تعرف على منهجية عمل المهندس مصطفى، رؤيته الهندسية، وشهادات اعتماده المهنية.">
                            Deep dive into Eng. Mostafa's procurement methodology, technical leadership, and engineering credentials.
                        </p>
                    </div>
                    <div class="hub-link-action">
                        <span data-en="Read Full Profile" data-ar="قراءة السيرة الكاملة">Read Full Profile</span>
                        <i class="fas fa-arrow-right"></i>
                    </div>
                </a>

                <!-- Card 5: Experience Timeline -->
                <a href="experience.html" class="hub-card animate-on-scroll">
                    <div>
                        <div class="hub-icon"><i class="fas fa-timeline"></i></div>
                        <h3 class="hub-title" data-en="Career Journey" data-ar="المسيرة المهنية">Career Journey</h3>
                        <p class="hub-desc" data-en="Progressive 9-year leadership across Zaid Al Hussain, Atrium (TMG), Pillars, Hassan Allam, and EDC Expertise." data-ar="تدرج مهني استثنائي عبر 5 من أكبر المجموعات الإنشائية في السعودية ومصر.">
                            Progressive 9-year leadership across Zaid Al Hussain, Atrium (TMG), Pillars, Hassan Allam, and EDC Expertise.
                        </p>
                    </div>
                    <div class="hub-link-action">
                        <span data-en="View Career Track" data-ar="عرض السجل الوظيفي">View Career Track</span>
                        <i class="fas fa-arrow-right"></i>
                    </div>
                </a>

                <!-- Card 6: Certificates & SCE -->
                <a href="certificates.html" class="hub-card animate-on-scroll">
                    <div>
                        <div class="hub-icon"><i class="fas fa-certificate"></i></div>
                        <h3 class="hub-title" data-en="Certifications & SCE" data-ar="الشهادات والاعتمادات">Certifications & SCE</h3>
                        <p class="hub-desc" data-en="Official Saudi Council of Engineers membership, engineering degree, and corporate certificates of recognition." data-ar="عضوية هيئة المهندسين السعودية الرسمية، شهادة التخرج، وشهادات الخبرة من كبرى المجموعات.">
                            Official Saudi Council of Engineers membership, engineering degree, and corporate certificates of recognition.
                        </p>
                    </div>
                    <div class="hub-link-action">
                        <span data-en="View Documents" data-ar="معاينة المستندات">View Documents</span>
                        <i class="fas fa-arrow-right"></i>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <!-- ============ FEATURED SHOWCASE SPOTLIGHT ============ -->
    <section class="section" style="background: var(--bg-secondary);">
        <div class="container">
            <div class="section-title animate-on-scroll">
                <span class="title-number">02.</span>
                <span data-en="Flagship Project Spotlight" data-ar="المشروع القيادي الأبرز">Flagship Project Spotlight</span>
                <span class="title-line"></span>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; background: var(--bg-surface); border-radius: var(--radius-lg); overflow: hidden; border: 1px solid rgba(196,163,90,0.25); box-shadow: var(--shadow-card);" class="about-grid-responsive animate-on-scroll">
                <div style="height: 100%; min-height: 380px; position: relative;">
                    <img src="assets/images/projects/kaig_6.jpg" alt="KAIG Main Dome" style="width: 100%; height: 100%; object-fit: cover;">
                    <div style="position: absolute; top: 20px; left: 20px; background: rgba(196,163,90,0.95); color: #0A192F; padding: 6px 16px; border-radius: 20px; font-weight: 800; font-size: 0.8rem;">
                        SAR 2.63 BILLION
                    </div>
                </div>
                <div style="padding: 40px;">
                    <span style="color: var(--accent-teal); font-weight: 700; font-size: 0.85rem; text-transform: uppercase;">Zaid Al Hussain Group • Riyadh, KSA</span>
                    <h3 style="font-size: 1.8rem; font-weight: 800; margin: 10px 0 15px; font-family: var(--font-display);">King Abdullah International Gardens (KAIG)</h3>
                    <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin-bottom: 25px;">
                        Leading the entire MEP procurement section for one of the world's largest bioclimatic botanic developments (2.1M m²). Managing sophisticated HVAC chiller plants, electrical substations, automated irrigation, and specialized environmental dome control networks.
                    </p>
                    <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                        <a href="project-detail.html?id=kaig" class="btn btn-primary magnetic-btn">
                            <i class="fas fa-images"></i>
                            <span data-en="View 7 High-Res Photos & Scope" data-ar="عرض 7 صور وتفاصيل المشروع">View 7 High-Res Photos & Scope</span>
                        </a>
                        <a href="projects.html" class="btn btn-outline magnetic-btn">
                            <span data-en="All 14 Projects" data-ar="جميع الـ 14 مشروع">All 14 Projects</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ FREELANCE WHATSAPP BANNER ============ -->
    <section class="section" style="padding: 40px 0;">
        <div class="container">
            <div class="whatsapp-cta-banner animate-on-scroll">
                <div>
                    <h3 style="font-size: 1.8rem; font-weight: 800; color: #fff; margin-bottom: 8px;">
                        <span data-en="Need Expert MEP Procurement Consultation?" data-ar="تحتاج استشارة متخصصة في مشتريات الـ MEP؟">Need Expert MEP Procurement Consultation?</span>
                    </h3>
                    <p style="color: #A3E6C8; font-size: 1rem; margin: 0; max-width: 600px;" data-en="Available for freelance procurement packages, BOQ reviews, cost optimization studies, and contractor negotiations." data-ar="متاح لتقديم خدمات الفريلانس الهندسية، مراجعة جداول الكميات، دراسات هندسة القيمة والتفاوض مع الموردين.">
                        Available for freelance procurement packages, BOQ reviews, cost optimization studies, and contractor negotiations.
                    </p>
                </div>
                <a href="https://wa.me/966502582122?text=Hello%20Eng.%20Mostafa,%20I%20would%20like%20to%20inquire%20about%20your%20MEP%20procurement%20consulting%20services." target="_blank" class="btn-whatsapp magnetic-btn">
                    <i class="fab fa-whatsapp" style="font-size: 1.4rem;"></i>
                    <span data-en="Chat on WhatsApp Directly" data-ar="تواصل عبر الواتساب مباشرة">Chat on WhatsApp Directly</span>
                </a>
            </div>
        </div>
    </section>
    """
    return get_head("Eng. Mostafa Abdelghany — MEP Procurement Section Head & Consultant") + get_navbar("index.html") + body + get_footer()

def build_about():
    body = """
    <div style="padding-top: 130px; background: var(--bg-secondary); border-bottom: 1px solid rgba(196,163,90,0.15);">
        <div class="container" style="padding-bottom: 60px;">
            <div class="section-title animate-on-scroll">
                <span class="title-number">01.</span>
                <span data-en="Professional Biography" data-ar="نبذة مهنية متكاملة">Professional Biography</span>
                <span class="title-line"></span>
            </div>

            <div style="display: grid; grid-template-columns: 360px 1fr; gap: 50px; align-items: start;" class="about-grid-responsive">
                <!-- Square Photo Frame -->
                <div class="animate-on-scroll">
                    <div class="profile-square-frame" style="width: 100%; max-width: 340px; height: 420px;">
                        <div class="img-container">
                            <img src="assets/images/headshot.jpg" alt="Eng. Mostafa Abdelghany">
                        </div>
                        <div class="frame-border-outer"></div>
                        <div class="frame-accent-corner corner-tl"></div>
                        <div class="frame-accent-corner corner-br"></div>
                        <div class="frame-badge-experience">
                            <i class="fas fa-award"></i>
                            <span>9+ Years in KSA & Egypt</span>
                        </div>
                    </div>

                    <div style="margin-top: 35px; background: var(--bg-surface); padding: 24px; border-radius: var(--radius-md); border: 1px solid rgba(196,163,90,0.2);">
                        <h4 style="color: var(--gold-primary); font-size: 1rem; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                            <i class="fas fa-id-card"></i> Official Accreditations
                        </h4>
                        <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 8px;">
                            <strong>SCE Membership:</strong> #1084929 (Saudi Council of Engineers)
                        </p>
                        <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 8px;">
                            <strong>Degree:</strong> B.Sc. Mechanical Engineering, Benha University
                        </p>
                        <p style="font-size: 0.88rem; color: var(--text-secondary); margin: 0;">
                            <strong>Location:</strong> Riyadh, Kingdom of Saudi Arabia
                        </p>
                    </div>
                </div>

                <!-- Bio Content -->
                <div class="animate-on-scroll">
                    <h2 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 20px; font-family: var(--font-display);">
                        <span data-en="Engineering Excellence Through Strategic Procurement" data-ar="التميز الهندسي من خلال الإدارة الاستراتيجية للمشتريات">Engineering Excellence Through Strategic Procurement</span>
                    </h2>

                    <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;" data-en="Eng. Mostafa Abdelghany is a seasoned MEP Procurement Section Head and Senior Mechanical Engineer with over 9 years of progressive experience delivering mega-scale infrastructure, high-rise, hospitality, and residential projects across Saudi Arabia and Egypt." data-ar="المهندس مصطفى عبدالغني هو رئيس قسم مشتريات أعمال MEP ومهندس ميكانيكي أول يمتلك أكثر من 9 سنوات من الخبرة المتصاعدة في تسليم مشاريع البنية التحتية العملاقة، الأبراج الشاهقة، الفنادق العالمية، والمجمعات السكنية الكبرى في السعودية ومصر.">
                        Eng. Mostafa Abdelghany is a seasoned MEP Procurement Section Head and Senior Mechanical Engineer with over 9 years of progressive experience delivering mega-scale infrastructure, high-rise, hospitality, and residential projects across Saudi Arabia and Egypt.
                    </p>

                    <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.8; margin-bottom: 25px;" data-en="Currently spearheading MEP procurement operations for the SAR 2.63 Billion King Abdullah International Gardens (KAIG) at Zaid Al Hussain Group, Mostafa combines deep technical engineering expertise with commercial acumen to drive multi-million dollar cost optimizations, enforce stringent QA/QC standards, and secure favorable contract terms with top global suppliers." data-ar="يقود حالياً عمليات مشتريات الـ MEP لمشروع حدائق الملك عبدالله الدولية (KAIG) بقيمة 2.63 مليار ريال في مجموعة زيد الحصين. يجمع المهندس مصطفى بين المعرفة الهندسية التقنية الدقيقة والذكاء التجاري لتحقيق وفورات مالية بملايين الريالات، وضمان أعلى معايير الجودة والاعتماد، وإبرام عقود استراتيجية مع كبرى الشركات العالمية.">
                        Currently spearheading MEP procurement operations for the SAR 2.63 Billion King Abdullah International Gardens (KAIG) at Zaid Al Hussain Group, Mostafa combines deep technical engineering expertise with commercial acumen to drive multi-million dollar cost optimizations, enforce stringent QA/QC standards, and secure favorable contract terms with top global suppliers.
                    </p>

                    <!-- Core Competencies Bar -->
                    <div style="margin-top: 30px;">
                        <h3 class="subsection-title" data-en="Procurement Mastery & Skills" data-ar="مجالات الخبرة والكفاءة الأساسية">Procurement Mastery & Skills</h3>
                        
                        <div class="skill-item">
                            <div class="skill-header"><span>MEP Technical Procurement & Package Strategy</span><span class="skill-percent">96%</span></div>
                            <div class="skill-bar"><div class="skill-fill" data-percentage="96"></div></div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-header"><span>Value Engineering & Cost Optimization Models</span><span class="skill-percent">94%</span></div>
                            <div class="skill-bar"><div class="skill-fill" data-percentage="94"></div></div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-header"><span>Subcontract & Vendor High-Stakes Negotiation</span><span class="skill-percent">92%</span></div>
                            <div class="skill-bar"><div class="skill-fill" data-percentage="92"></div></div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-header"><span>Supply Chain Logistics & Material Submittals</span><span class="skill-percent">95%</span></div>
                            <div class="skill-bar"><div class="skill-fill" data-percentage="95"></div></div>
                        </div>
                    </div>

                    <div style="margin-top: 35px; display: flex; gap: 15px; flex-wrap: wrap;">
                        <a href="services.html" class="btn btn-primary magnetic-btn">
                            <i class="fas fa-handshake"></i>
                            <span data-en="View Consulting Services" data-ar="استعراض الخدمات والاستشارات">View Consulting Services</span>
                        </a>
                        <a href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download class="btn btn-outline magnetic-btn">
                            <i class="fas fa-file-pdf"></i>
                            <span data-en="Download Official CV" data-ar="تحميل السيرة الذاتية الرسمية">Download Official CV</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return get_head("About Eng. Mostafa Abdelghany — MEP Procurement Section Head") + get_navbar("about.html") + body + get_footer()

def build_services():
    body = """
    <div style="padding-top: 130px; background: var(--bg-secondary); border-bottom: 1px solid rgba(196,163,90,0.15);">
        <div class="container" style="padding-bottom: 60px;">
            <div class="section-title animate-on-scroll">
                <span class="title-number">01.</span>
                <span data-en="Services & Freelance Consulting" data-ar="الخدمات الهندسية واستشارات الفريلانس">Services & Freelance Consulting</span>
                <span class="title-line"></span>
            </div>

            <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 800px; line-height: 1.8;" class="animate-on-scroll" data-en="Empowering main contractors, engineering consultancies, and private real estate developers with high-level MEP procurement mastery, aggressive cost reduction strategies, and bulletproof supplier contracts." data-ar="تمكين كبرى شركات المقاولات، المكاتب الاستشارية، والمطورين العقاريين من خلال إدارة احترافية لمشتريات الـ MEP، استراتيجيات خفض التكاليف المتقدمة، وصياغة عقود توريد محكمة تضمن أقصى ربحية وأعلى جودة.">
                Empowering main contractors, engineering consultancies, and private real estate developers with high-level MEP procurement mastery, aggressive cost reduction strategies, and bulletproof supplier contracts.
            </p>

            <!-- 6 Core Services Grid -->
            <div class="services-grid">
                <!-- Service 1 -->
                <div class="service-card animate-on-scroll">
                    <span class="service-badge">High Impact</span>
                    <div class="service-icon"><i class="fas fa-calculator"></i></div>
                    <h3 class="service-title" data-en="Value Engineering & Cost Optimization" data-ar="هندسة القيمة وتقليل التكاليف">Value Engineering & Cost Optimization</h3>
                    <p class="service-desc" data-en="In-depth analysis of MEP design specifications and material selections to identify equivalent high-quality alternatives, driving 10% to 25% direct savings without compromising quality or compliance." data-ar="دراسة وتحليل المواصفات الفنية لشبكات الـ MEP لاقتراح بدائل معتمدة ومطابقة للمواصفات، مما يحقق وفورات مالية مباشرة تتراوح بين 10% إلى 25% دون المساس بالجودة أو كفاءة التشغيل.">
                        In-depth analysis of MEP design specifications and material selections to identify equivalent high-quality alternatives, driving 10% to 25% direct savings without compromising quality or compliance.
                    </p>
                    <div class="service-deliverables">
                        <h5 data-en="Key Deliverables" data-ar="مخرجات الخدمة">Key Deliverables</h5>
                        <ul>
                            <li><i class="fas fa-check"></i> Comparative Cost Benefit Reports</li>
                            <li><i class="fas fa-check"></i> Approved Material Alternative Submittals</li>
                            <li><i class="fas fa-check"></i> Life-Cycle Cost & Energy Assessments</li>
                        </ul>
                    </div>
                    <a href="contact.html?service=value-engineering" class="btn btn-sm btn-outline magnetic-btn" style="margin-top: auto;">
                        <span data-en="Inquire This Service" data-ar="طلب الخدمة">Inquire This Service</span>
                    </a>
                </div>

                <!-- Service 2 -->
                <div class="service-card animate-on-scroll">
                    <span class="service-badge">Full Package</span>
                    <div class="service-icon"><i class="fas fa-sitemap"></i></div>
                    <h3 class="service-title" data-en="End-to-End MEP Procurement Packages" data-ar="إدارة حزم مشتريات MEP المتكاملة">End-to-End MEP Procurement Packages</h3>
                    <p class="service-desc" data-en="Managing the complete lifecycle of MEP procurement packages from RFP preparation, technical leveling, commercial comparisons, to purchase order issuance and factory inspection coordination." data-ar="إدارة دورة المشتريات بالكامل لحزم الـ MEP بدءاً من إعداد كراسات الشروط، التقييم الفني للموردين، المقارنات المالية، وحتى إصدار أوامر الشراء واعتماد العينات.">
                        Managing the complete lifecycle of MEP procurement packages from RFP preparation, technical leveling, commercial comparisons, to purchase order issuance and factory inspection coordination.
                    </p>
                    <div class="service-deliverables">
                        <h5 data-en="Key Deliverables" data-ar="مخرجات الخدمة">Key Deliverables</h5>
                        <ul>
                            <li><i class="fas fa-check"></i> Comprehensive Commercial Comparison Sheets</li>
                            <li><i class="fas fa-check"></i> Technical Evaluation Summaries</li>
                            <li><i class="fas fa-check"></i> Procurement Tracking Logs (PTS)</li>
                        </ul>
                    </div>
                    <a href="contact.html?service=mep-procurement" class="btn btn-sm btn-outline magnetic-btn" style="margin-top: auto;">
                        <span data-en="Inquire This Service" data-ar="طلب الخدمة">Inquire This Service</span>
                    </a>
                </div>

                <!-- Service 3 -->
                <div class="service-card animate-on-scroll">
                    <span class="service-badge">Strategic</span>
                    <div class="service-icon"><i class="fas fa-file-contract"></i></div>
                    <h3 class="service-title" data-en="Subcontract & FIDIC Contract Negotiations" data-ar="التفاوض على العقود وإدارة المقاولين الباطن">Subcontract & FIDIC Contract Negotiations</h3>
                    <p class="service-desc" data-en="Drafting robust subcontract agreements, mitigating commercial risks, negotiating payment terms, warranty periods, and penalty clauses under Saudi and international FIDIC frameworks." data-ar="صياغة وتدقيق عقود مقاولي الباطن والموردين، تخفيف المخاطر القانونية والمالية، والتفاوض على شروط الدفع والضمانات البنكية وفق أنظمة FIDIC والأنظمة السعودية.">
                        Drafting robust subcontract agreements, mitigating commercial risks, negotiating payment terms, warranty periods, and penalty clauses under Saudi and international FIDIC frameworks.
                    </p>
                    <div class="service-deliverables">
                        <h5 data-en="Key Deliverables" data-ar="مخرجات الخدمة">Key Deliverables</h5>
                        <ul>
                            <li><i class="fas fa-check"></i> Subcontract Agreements & Special Conditions</li>
                            <li><i class="fas fa-check"></i> Risk Mitigation Matrix</li>
                            <li><i class="fas fa-check"></i> Scope Gap Minimization Reports</li>
                        </ul>
                    </div>
                    <a href="contact.html?service=contract-negotiation" class="btn btn-sm btn-outline magnetic-btn" style="margin-top: auto;">
                        <span data-en="Inquire This Service" data-ar="طلب الخدمة">Inquire This Service</span>
                    </a>
                </div>

                <!-- Service 4 -->
                <div class="service-card animate-on-scroll">
                    <span class="service-badge">Precision</span>
                    <div class="service-icon"><i class="fas fa-list-check"></i></div>
                    <h3 class="service-title" data-en="BOQ Preparation & Quantity Take-offs" data-ar="إعداد وتدقيق جداول الكميات (BOQ)">BOQ Preparation & Quantity Take-offs</h3>
                    <p class="service-desc" data-en="Precise mechanical and electrical quantity take-offs directly from AutoCAD and BIM models, preparing detailed Bill of Quantities (BOQs) aligned with CSI MasterFormat standards." data-ar="حصر كميات هندسي دقيق لجميع بنود الميكانيكا والكهرباء من المخططات ونماذج الـ BIM، وإعداد جداول كميات مسعرة ومعتمدة ومطابقة لمواصفات المشروع.">
                        Precise mechanical and electrical quantity take-offs directly from AutoCAD and BIM models, preparing detailed Bill of Quantities (BOQs) aligned with CSI MasterFormat standards.
                    </p>
                    <div class="service-deliverables">
                        <h5 data-en="Key Deliverables" data-ar="مخرجات الخدمة">Key Deliverables</h5>
                        <ul>
                            <li><i class="fas fa-check"></i> Itemized BOQ Excel Workbooks with Formulas</li>
                            <li><i class="fas fa-check"></i> Material Quantity Verification Audits</li>
                            <li><i class="fas fa-check"></i> Rate Breakdown & Cost Estimating</li>
                        </ul>
                    </div>
                    <a href="contact.html?service=boq-preparation" class="btn btn-sm btn-outline magnetic-btn" style="margin-top: auto;">
                        <span data-en="Inquire This Service" data-ar="طلب الخدمة">Inquire This Service</span>
                    </a>
                </div>

                <!-- Service 5 -->
                <div class="service-card animate-on-scroll">
                    <span class="service-badge">Advisory</span>
                    <div class="service-icon"><i class="fas fa-comments-dollar"></i></div>
                    <h3 class="service-title" data-en="Freelance MEP Procurement Advisory" data-ar="استشارات فريلانس هندسية متخصصة">Freelance MEP Procurement Advisory</h3>
                    <p class="service-desc" data-en="On-demand consulting for engineering consultancies, startups, or contracting firms needing expert guidance on supplier selection, price auditing, and vendor claims resolution." data-ar="تقديم استشارات هندسية وتجارية مرنة حسب الطلب للشركات والمطورين لفحص عروض الموردين، تدقيق الأسعار، وحل النزاعات التعاقدية والتأخيرات.">
                        On-demand consulting for engineering consultancies, startups, or contracting firms needing expert guidance on supplier selection, price auditing, and vendor claims resolution.
                    </p>
                    <div class="service-deliverables">
                        <h5 data-en="Key Deliverables" data-ar="مخرجات الخدمة">Key Deliverables</h5>
                        <ul>
                            <li><i class="fas fa-check"></i> Vendor Prequalification Reports</li>
                            <li><i class="fas fa-check"></i> Material Claims Audit & Claim Defense</li>
                            <li><i class="fas fa-check"></i> Direct 1-on-1 Strategic Consulting Calls</li>
                        </ul>
                    </div>
                    <a href="contact.html?service=freelance-advisory" class="btn btn-sm btn-outline magnetic-btn" style="margin-top: auto;">
                        <span data-en="Inquire This Service" data-ar="طلب الخدمة">Inquire This Service</span>
                    </a>
                </div>

                <!-- Service 6 -->
                <div class="service-card animate-on-scroll">
                    <span class="service-badge">Global Sourcing</span>
                    <div class="service-icon"><i class="fas fa-truck-ramp-box"></i></div>
                    <h3 class="service-title" data-en="Supply Chain & International Sourcing" data-ar="سلاسل الإمداد والتوريد الدولي">Supply Chain & International Sourcing</h3>
                    <p class="service-desc" data-en="Leveraging an extensive network of verified MEP manufacturers across GCC, Europe, and Asia for long-lead equipment like chillers, transformers, generators, and specialized pumps." data-ar="الاستفادة من شبكة علاقات وتوريد دولية واسعة بالمصانع المعتمدة في الخليج وأوروبا وآسيا لتوريد المعدات ذات فترات التصنيع الطويلة (Long Lead Items).">
                        Leveraging an extensive network of verified MEP manufacturers across GCC, Europe, and Asia for long-lead equipment like chillers, transformers, generators, and specialized pumps.
                    </p>
                    <div class="service-deliverables">
                        <h5 data-en="Key Deliverables" data-ar="مخرجات الخدمة">Key Deliverables</h5>
                        <ul>
                            <li><i class="fas fa-check"></i> Long-Lead Items Tracking & Expediting</li>
                            <li><i class="fas fa-check"></i> Logistics & Customs Coordination</li>
                            <li><i class="fas fa-check"></i> Manufacturer Warranty & Compliance Seals</li>
                        </ul>
                    </div>
                    <a href="contact.html?service=supply-chain" class="btn btn-sm btn-outline magnetic-btn" style="margin-top: auto;">
                        <span data-en="Inquire This Service" data-ar="طلب الخدمة">Inquire This Service</span>
                    </a>
                </div>
            </div>

            <!-- Engagement Models Section -->
            <div class="engagement-models-section animate-on-scroll">
                <div style="text-align: center; max-width: 700px; margin: 0 auto;">
                    <h3 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 12px;" data-en="Flexible Engagement Models" data-ar="نماذج التعاقد والعمل المرنة">Flexible Engagement Models</h3>
                    <p style="color: var(--text-secondary); font-size: 0.95rem;" data-en="Choose the cooperation framework that fits your project timeline and organizational scope." data-ar="اختر نموذج التعاون الذي يناسب حجم وطبيعة مشروعك واحتياجات فريقك.">
                        Choose the cooperation framework that fits your project timeline and organizational scope.
                    </p>
                </div>

                <div class="models-grid">
                    <div class="model-card">
                        <h4 class="model-title" data-en="Hourly / Retainer Advisory" data-ar="استشارة بالساعة / اشتراك شهري">Hourly / Retainer Advisory</h4>
                        <div class="model-highlight" data-en="On-Demand" data-ar="حسب الطلب">On-Demand</div>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 20px;">
                            Perfect for quick vendor quote reviews, contract clauses auditing, and strategic procurement consultations.
                        </p>
                        <a href="contact.html?plan=hourly" class="btn btn-sm btn-outline magnetic-btn">Select Model</a>
                    </div>

                    <div class="model-card featured">
                        <span style="background: var(--gold-primary); color: #0A192F; font-size: 0.75rem; font-weight: 800; padding: 3px 12px; border-radius: 10px; display: inline-block; margin-bottom: 10px;">MOST POPULAR</span>
                        <h4 class="model-title" data-en="Project-Based Package" data-ar="تسليم حزم مشتريات بالمشروع">Project-Based Package</h4>
                        <div class="model-highlight" data-en="Fixed Scope" data-ar="نطاق محدد">Fixed Scope</div>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 20px;">
                            Complete ownership of specific MEP packages (e.g. Chillers, Transformers, BOQ preparation, or Subcontract).
                        </p>
                        <a href="contact.html?plan=project" class="btn btn-sm btn-primary magnetic-btn">Select Model</a>
                    </div>

                    <div class="model-card">
                        <h4 class="model-title" data-en="Full Procurement Leadership" data-ar="إدارة مشتريات المشروع الكاملة">Full Procurement Leadership</h4>
                        <div class="model-highlight" data-en="Milestone / KPI" data-ar="بناءً على الإنجاز">Milestone / KPI</div>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 20px;">
                            Managing the entire project procurement portfolio, team coordination, and value engineering targets.
                        </p>
                        <a href="contact.html?plan=full" class="btn btn-sm btn-outline magnetic-btn">Select Model</a>
                    </div>
                </div>
            </div>

            <!-- WhatsApp Banner -->
            <div class="whatsapp-cta-banner animate-on-scroll">
                <div>
                    <h3 style="font-size: 1.8rem; font-weight: 800; color: #fff; margin-bottom: 8px;">
                        <span data-en="Ready to Elevate Your MEP Procurement?" data-ar="جاهز لتعظيم أرباح وخفض تكاليف مشروعك؟">Ready to Elevate Your MEP Procurement?</span>
                    </h3>
                    <p style="color: #A3E6C8; font-size: 1rem; margin: 0;" data-en="Send a message on WhatsApp for instant response and project quotation." data-ar="تواصل عبر الواتساب مباشرة لمناقشة تفاصيل مشروعك واستلام عرض السعر.">
                        Send a message on WhatsApp for instant response and project quotation.
                    </p>
                </div>
                <a href="https://wa.me/966502582122?text=Hello%20Eng.%20Mostafa,%20I%20would%20like%20to%20discuss%20a%20procurement%20consulting%20opportunity." target="_blank" class="btn-whatsapp magnetic-btn">
                    <i class="fab fa-whatsapp" style="font-size: 1.4rem;"></i>
                    <span data-en="Chat on WhatsApp Now" data-ar="محادثة واتساب فورية">Chat on WhatsApp Now</span>
                </a>
            </div>
        </div>
    </div>
    """
    return get_head("Services & Freelance Consulting — Eng. Mostafa Abdelghany") + get_navbar("services.html") + body + get_footer()

def build_software():
    body = """
    <div style="padding-top: 130px; background: var(--bg-secondary); border-bottom: 1px solid rgba(196,163,90,0.15);">
        <div class="container" style="padding-bottom: 60px;">
            <div class="section-title animate-on-scroll">
                <span class="title-number">01.</span>
                <span data-en="Software & Engineering Tools" data-ar="البرامج والأدوات الهندسية">Software & Engineering Tools</span>
                <span class="title-line"></span>
            </div>

            <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 800px; line-height: 1.8;" class="animate-on-scroll" data-en="Combining advanced engineering modeling software with enterprise ERP platforms and financial tools to orchestrate multi-million dollar procurement schedules with pinpoint accuracy." data-ar="الدمج بين البرمجيات الهندسية المتقدمة وأنظمة إدارة الموارد المؤسسية (ERP) ونماذج التكاليف المالية لإدارة جداول التوريد المليارية بأعلى درجات الدقة.">
                Combining advanced engineering modeling software with enterprise ERP platforms and financial tools to orchestrate multi-million dollar procurement schedules with pinpoint accuracy.
            </p>

            <div class="software-grid">
                <!-- Tool 1: Primavera P6 -->
                <div class="software-card animate-on-scroll">
                    <div class="software-header">
                        <div class="software-icon-wrapper"><i class="fas fa-calendar-check"></i></div>
                        <div>
                            <h3 class="software-title">Primavera P6 Professional</h3>
                            <span class="software-category">Project Planning & Procurement Tracking</span>
                        </div>
                    </div>
                    <p class="service-desc" data-en="Tracking long-lead MEP equipment schedules, critical path milestones, vendor delivery variance, and material submittal integration." data-ar="إدارة وتتبع جداول توريد المعدات الحساسة، المسار الحرج (Critical Path)، وانحرافات مواعيد التوريد وربطها بالجدول الزمني العام للمشروع.">
                        Tracking long-lead MEP equipment schedules, critical path milestones, vendor delivery variance, and material submittal integration.
                    </p>
                    <div class="software-level">
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--gold-primary); font-weight: 700;">
                            <span>Mastery Level</span><span>92%</span>
                        </div>
                        <div class="level-bar"><div class="level-fill" style="width: 92%;"></div></div>
                    </div>
                </div>

                <!-- Tool 2: AutoCAD -->
                <div class="software-card animate-on-scroll">
                    <div class="software-header">
                        <div class="software-icon-wrapper"><i class="fas fa-drafting-compass"></i></div>
                        <div>
                            <h3 class="software-title">AutoCAD MEP</h3>
                            <span class="software-category">Shop Drawings & As-Built Verification</span>
                        </div>
                    </div>
                    <p class="service-desc" data-en="Reviewing mechanical & electrical shop drawings, verifying routing coordination, quantity take-offs, and resolving site clashes." data-ar="مراجعة وتدقيق الرسومات التنفيذية لشبكات الميكانيكا والكهرباء، حصر الكميات الهندسي، والتأكد من مطابقة المخططات للمواصفات المعمارية.">
                        Reviewing mechanical & electrical shop drawings, verifying routing coordination, quantity take-offs, and resolving site clashes.
                    </p>
                    <div class="software-level">
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--gold-primary); font-weight: 700;">
                            <span>Mastery Level</span><span>95%</span>
                        </div>
                        <div class="level-bar"><div class="level-fill" style="width: 95%;"></div></div>
                    </div>
                </div>

                <!-- Tool 3: BIM & Revit -->
                <div class="software-card animate-on-scroll">
                    <div class="software-header">
                        <div class="software-icon-wrapper"><i class="fas fa-cubes"></i></div>
                        <div>
                            <h3 class="software-title">Autodesk Revit & BIM</h3>
                            <span class="software-category">3D Coordination & Quantity Extraction</span>
                        </div>
                    </div>
                    <p class="service-desc" data-en="Extracting exact bill of quantities from 3D BIM models, verifying spatial clearance for large MEP plant rooms, and model clash detection." data-ar="استخراج جداول الكميات الدقيقة من نماذج الـ BIM ثلاثية الأبعاد، وتدقيق مساحات غرف المضخات والمحولات والمحطات المركزية.">
                        Extracting exact bill of quantities from 3D BIM models, verifying spatial clearance for large MEP plant rooms, and model clash detection.
                    </p>
                    <div class="software-level">
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--gold-primary); font-weight: 700;">
                            <span>Mastery Level</span><span>88%</span>
                        </div>
                        <div class="level-bar"><div class="level-fill" style="width: 88%;"></div></div>
                    </div>
                </div>

                <!-- Tool 4: Oracle ERP -->
                <div class="software-card animate-on-scroll">
                    <div class="software-header">
                        <div class="software-icon-wrapper"><i class="fas fa-database"></i></div>
                        <div>
                            <h3 class="software-title">Oracle ERP / Fusion</h3>
                            <span class="software-category">Enterprise Procurement Management</span>
                        </div>
                    </div>
                    <p class="service-desc" data-en="Issuing purchase orders (POs), managing RFQ workflows, supplier master database, budget control, and three-way invoice matching." data-ar="إصدار أوامر الشراء الرسمية، إدارة طلبات عروض الأسعار RFQ، الرقابة على ميزانية المشروعات، ومطابقة الفواتير المالية مع التوريدات الفعلية.">
                        Issuing purchase orders (POs), managing RFQ workflows, supplier master database, budget control, and three-way invoice matching.
                    </p>
                    <div class="software-level">
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--gold-primary); font-weight: 700;">
                            <span>Mastery Level</span><span>94%</span>
                        </div>
                        <div class="level-bar"><div class="level-fill" style="width: 94%;"></div></div>
                    </div>
                </div>

                <!-- Tool 5: SAP ERP -->
                <div class="software-card animate-on-scroll">
                    <div class="software-header">
                        <div class="software-icon-wrapper"><i class="fas fa-network-wired"></i></div>
                        <div>
                            <h3 class="software-title">SAP Materials Management (MM)</h3>
                            <span class="software-category">Supply Chain & Inventory Controls</span>
                        </div>
                    </div>
                    <p class="service-desc" data-en="Managing material master data, purchase requisitions, good receipts (GRN), and site warehouse inventory controls." data-ar="إدارة حركة المواد والمخزون، أذونات الاستلام الفني (GRN)، وتتبع التوريدات الموقعية عبر وحدات SAP MM.">
                        Managing material master data, purchase requisitions, good receipts (GRN), and site warehouse inventory controls.
                    </p>
                    <div class="software-level">
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--gold-primary); font-weight: 700;">
                            <span>Mastery Level</span><span>90%</span>
                        </div>
                        <div class="level-bar"><div class="level-fill" style="width: 90%;"></div></div>
                    </div>
                </div>

                <!-- Tool 6: Advanced Excel Financial Models -->
                <div class="software-card animate-on-scroll">
                    <div class="software-header">
                        <div class="software-icon-wrapper"><i class="fas fa-file-excel"></i></div>
                        <div>
                            <h3 class="software-title">Advanced Excel & Cost Modeling</h3>
                            <span class="software-category">Commercial Comparison & Cash Flow</span>
                        </div>
                    </div>
                    <p class="service-desc" data-en="Building complex multi-vendor commercial evaluation sheets, automated currency conversion, price indexing, and cash outflow forecasting." data-ar="بناء جداول مقارنات مالية متقدمة متعددة الموردين مع معادلات التحليل المالي وحساب التدفقات النقدية المتوقعة وفروق الأسعار.">
                        Building complex multi-vendor commercial evaluation sheets, automated currency conversion, price indexing, and cash outflow forecasting.
                    </p>
                    <div class="software-level">
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--gold-primary); font-weight: 700;">
                            <span>Mastery Level</span><span>98%</span>
                        </div>
                        <div class="level-bar"><div class="level-fill" style="width: 98%;"></div></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return get_head("Software Stack & Engineering Tools — Eng. Mostafa Abdelghany") + get_navbar("software.html") + body + get_footer()

def build_projects():
    body = """
    <div style="padding-top: 130px; background: var(--bg-secondary); border-bottom: 1px solid rgba(196,163,90,0.15);">
        <div class="container" style="padding-bottom: 50px;">
            <div class="section-title animate-on-scroll">
                <span class="title-number">01.</span>
                <span data-en="Projects Directory (14 Iconic Projects)" data-ar="دليل المشاريع الشامل (14 مشروعاً)">Projects Directory (14 Iconic Projects)</span>
                <span class="title-line"></span>
            </div>

            <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 800px; line-height: 1.8; margin-bottom: 35px;" class="animate-on-scroll" data-en="Explore Eng. Mostafa Abdelghany's comprehensive portfolio of 14 mega infrastructure, residential smart cities, airports, 5-star hotels, and educational complexes across Saudi Arabia and Egypt." data-ar="تصفح السجل الهندسي الشامل للمهندس مصطفى عبدالغني المتضمن 14 مشروعاً استراتيجياً للبنية التحتية، المدن الذكية، المطارات الدولية، الأبراج والفنادق العالمية في السعودية ومصر.">
                Explore Eng. Mostafa Abdelghany's comprehensive portfolio of 14 mega infrastructure, residential smart cities, airports, 5-star hotels, and educational complexes across Saudi Arabia and Egypt.
            </p>

            <!-- Search and Controls Bar -->
            <div class="projects-header-controls animate-on-scroll">
                <div class="project-search-box">
                    <i class="fas fa-search"></i>
                    <input type="text" id="project-search-input" placeholder="Search projects by name, company, or sector...">
                </div>

                <!-- Country Tabs -->
                <div class="filter-tabs" style="margin: 0;">
                    <button class="filter-tab active" data-filter="all" data-en="All Projects" data-ar="كل المشاريع">All Projects</button>
                    <button class="filter-tab" data-filter="ksa" data-en="Saudi Arabia" data-ar="السعودية">Saudi Arabia</button>
                    <button class="filter-tab" data-filter="egypt" data-en="Egypt" data-ar="مصر">Egypt</button>
                </div>
            </div>

            <!-- Sector Pills -->
            <div class="sector-filter-pills animate-on-scroll" style="margin-bottom: 35px;">
                <span class="sector-pill active" data-sector="all" data-en="All Sectors" data-ar="كافة القطاعات">All Sectors</span>
                <span class="sector-pill" data-sector="infrastructure" data-en="Mega Infrastructure" data-ar="بنية تحتية عملاقة">Mega Infrastructure</span>
                <span class="sector-pill" data-sector="compounds" data-en="Smart Cities & Compounds" data-ar="مدن ذكية ومجمعات">Smart Cities & Compounds</span>
                <span class="sector-pill" data-sector="highrise" data-en="High-Rise Towers" data-ar="أبراج شاهقة">High-Rise Towers</span>
                <span class="sector-pill" data-sector="hospitality" data-en="5-Star Hotels" data-ar="فنادق عالمية">5-Star Hotels</span>
                <span class="sector-pill" data-sector="aviation" data-en="Aviation & Airports" data-ar="مطارات وطيران">Aviation & Airports</span>
                <span class="sector-pill" data-sector="education" data-en="Universities & Research" data-ar="جامعات ومراكز أبحاث">Universities & Research</span>
                <span class="sector-pill" data-sector="healthcare" data-en="Healthcare & Medical" data-ar="منشآت طبية">Healthcare & Medical</span>
            </div>

            <div style="font-size: 0.9rem; color: var(--gold-light); margin-bottom: 25px;">
                Showing <strong id="projects-count-display" style="color: var(--gold-primary);">14</strong> projects (Click any project to view full gallery & technical scope)
            </div>

            <!-- Dynamic Projects Grid -->
            <div class="projects-grid" id="projects-grid-container"></div>
        </div>
    </div>
    """
    return get_head("Projects Directory — Eng. Mostafa Abdelghany") + get_navbar("projects.html") + body + get_footer("<script src='scripts/projects.js'></script>")

def build_project_detail():
    body = """
    <div class="project-detail-hero">
        <div class="container">
            <a href="projects.html" class="back-to-projects-btn magnetic-btn">
                <i class="fas fa-arrow-left"></i>
                <span data-en="Back to All Projects" data-ar="الرجوع إلى دليل المشاريع">Back to All Projects</span>
            </a>

            <div style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; margin-bottom: 8px;" id="project-detail-sector">
                Sector
            </div>

            <h1 class="project-detail-title" id="project-detail-title">Project Title</h1>

            <div class="project-detail-meta-bar">
                <span><i class="fas fa-building"></i> <span id="project-detail-company">Company</span></span>
                <span><i class="fas fa-user-tie"></i> <span id="project-detail-role">Role</span></span>
                <span><i class="fas fa-calendar"></i> <span id="project-detail-period">Period</span></span>
                <span><i class="fas fa-map-marker-alt"></i> <span id="project-detail-location">Location</span></span>
            </div>

            <!-- High-Res Interactive Gallery Component -->
            <div class="project-gallery-wrapper animate-on-scroll">
                <div class="main-image-display" id="gallery-main-container">
                    <img src="" alt="Project Photo" id="gallery-main-img">
                    <button class="gallery-fullscreen-btn" id="gallery-fullscreen-btn" title="View Fullscreen">
                        <i class="fas fa-expand"></i>
                    </button>
                    <button class="gallery-nav-btn gallery-prev" id="gallery-prev-btn" aria-label="Previous Photo">
                        <i class="fas fa-chevron-left"></i>
                    </button>
                    <button class="gallery-nav-btn gallery-next" id="gallery-next-btn" aria-label="Next Photo">
                        <i class="fas fa-chevron-right"></i>
                    </button>
                </div>

                <!-- Thumbnails Strip -->
                <div class="gallery-thumbnails-strip" id="gallery-thumbs-container"></div>
            </div>

            <!-- Project Details & Sidebar -->
            <div class="project-sheet-grid">
                <!-- Main Body -->
                <div class="project-details-body animate-on-scroll">
                    <h3 style="font-size: 1.5rem; font-weight: 700; color: var(--gold-primary); margin-bottom: 16px;">
                        <span data-en="Project Overview & Engineering Leadership" data-ar="نظرة عامة والقيادة الهندسية للمشروع">Project Overview & Engineering Leadership</span>
                    </h3>
                    <p id="project-detail-desc" style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.8; margin-bottom: 35px;"></p>

                    <h3 style="font-size: 1.4rem; font-weight: 700; color: var(--gold-primary); margin-bottom: 20px;">
                        <span data-en="MEP Procurement Scope of Work" data-ar="نطاق أعمال مشتريات الـ MEP">MEP Procurement Scope of Work</span>
                    </h3>
                    <div id="project-mep-scope-container"></div>
                </div>

                <!-- Sidebar Metadata -->
                <div class="project-sidebar-meta animate-on-scroll">
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: var(--gold-primary); margin-bottom: 20px; border-bottom: 1px solid rgba(196,163,90,0.2); padding-bottom: 10px;">
                        <span data-en="Project Data Sheet" data-ar="بطاقة بيانات المشروع">Project Data Sheet</span>
                    </h4>

                    <div class="sidebar-meta-item">
                        <span class="sidebar-meta-label"><i class="fas fa-coins"></i> <span data-en="Project Value" data-ar="القيمة المالية">Project Value</span></span>
                        <div class="sidebar-meta-val gold-text" id="project-detail-value">-</div>
                    </div>

                    <div class="sidebar-meta-item">
                        <span class="sidebar-meta-label"><i class="fas fa-handshake"></i> <span data-en="Client / Owner" data-ar="المالك / العميل">Client / Owner</span></span>
                        <div class="sidebar-meta-val" id="project-detail-client">-</div>
                    </div>

                    <div class="sidebar-meta-item">
                        <span class="sidebar-meta-label"><i class="fas fa-users"></i> <span data-en="Key Stakeholders" data-ar="الشركاء والاستشاريون">Key Stakeholders</span></span>
                        <div id="project-stakeholders-container" style="margin-top: 8px;"></div>
                    </div>
                </div>
            </div>

            <!-- Next/Prev Pagination -->
            <div class="project-pagination-bar animate-on-scroll">
                <a href="#" id="prev-project-btn" class="nav-proj-btn magnetic-btn">
                    <i class="fas fa-arrow-left"></i>
                    <span class="proj-btn-label">Previous Project</span>
                </a>
                <a href="#" id="next-project-btn" class="nav-proj-btn magnetic-btn">
                    <span class="proj-btn-label">Next Project</span>
                    <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    </div>

    <!-- Lightbox Modal -->
    <div class="lightbox-modal" id="lightbox-modal">
        <button class="lightbox-close-btn" id="lightbox-close-btn">&times;</button>
        <img src="" alt="Fullscreen Lightbox" id="lightbox-img">
    </div>
    """
    return get_head("Project Showcase & Gallery — Eng. Mostafa Abdelghany") + get_navbar("project-detail.html") + body + get_footer("<script src='scripts/project-detail.js'></script>")

def build_experience():
    body = """
    <div style="padding-top: 130px; background: var(--bg-secondary); border-bottom: 1px solid rgba(196,163,90,0.15);">
        <div class="container" style="padding-bottom: 60px;">
            <div class="section-title animate-on-scroll">
                <span class="title-number">01.</span>
                <span data-en="Career Journey & Track Record" data-ar="المسيرة المهنية وسجل الإنجازات">Career Journey & Track Record</span>
                <span class="title-line"></span>
            </div>

            <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 800px; line-height: 1.8; margin-bottom: 50px;" class="animate-on-scroll" data-en="A continuous track record of excellence spanning over 9 years in premier contracting groups across the Kingdom of Saudi Arabia and the Arab Republic of Egypt." data-ar="سجل حافل بالتميز الهندسي والقيادي يمتد لأكثر من 9 سنوات في كبرى مجموعات المقاولات والإنشاءات في المملكة العربية السعودية وجمهورية مصر العربية.">
                A continuous track record of excellence spanning over 9 years in premier contracting groups across the Kingdom of Saudi Arabia and the Arab Republic of Egypt.
            </p>

            <div class="timeline">
                <!-- Company 1: Zaid Al Hussain Group -->
                <div class="timeline-item animate-on-scroll" data-side="right">
                    <div class="timeline-dot current"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">Oct 2024 — Present</span>
                        <h3 class="timeline-company">Zaid Al Hussain Group (مجموعة زيد الحصين)</h3>
                        <h4 class="timeline-role" data-en="MEP Procurement Section Head" data-ar="رئيس قسم مشتريات أعمال MEP">MEP Procurement Section Head</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Riyadh, Saudi Arabia" data-ar="الرياض، المملكة العربية السعودية">Riyadh, Saudi Arabia</span></p>
                        <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.7; margin-bottom: 12px;">
                            Leading procurement operations for the SAR 2.63 Billion King Abdullah International Gardens (KAIG) project. Managing multimillion-dollar packages, direct supplier negotiations, and value engineering models.
                        </p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-star" style="color: var(--gold-primary);"></i> <span>Flagship: King Abdullah International Gardens (SAR 2.63B)</span>
                        </div>
                    </div>
                </div>

                <!-- Company 2: Atrium TMG -->
                <div class="timeline-item animate-on-scroll" data-side="left">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">2023 — 2024</span>
                        <h3 class="timeline-company">Atrium Quality Contractors (Talaat Moustafa Group)</h3>
                        <h4 class="timeline-role" data-en="Procurement Team Lead" data-ar="رئيس فريق المشتريات">Procurement Team Lead</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Cairo, Egypt" data-ar="القاهرة، مصر">Cairo, Egypt</span></p>
                        <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.7; margin-bottom: 12px;">
                            Headed the MEP procurement division for the Noor City Mega Compound in the Capital Region, coordinating high-volume material submittals and vendor agreements.
                        </p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>Mega Project: Noor Smart City (TMG)</span>
                        </div>
                    </div>
                </div>

                <!-- Company 3: Pillars Construction -->
                <div class="timeline-item animate-on-scroll" data-side="right">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">2020 — 2022</span>
                        <h3 class="timeline-company">Pillars Construction (شركة بيلرز للإنشاءات)</h3>
                        <h4 class="timeline-role" data-en="Senior Procurement Engineer" data-ar="مهندس مشتريات أول">Senior Procurement Engineer</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Cairo, Egypt" data-ar="القاهرة، مصر">Cairo, Egypt</span></p>
                        <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.7; margin-bottom: 12px;">
                            Managed critical MEP procurement packages for La Verde Compound in the New Capital, Zagazig University campus, and Berenice Military Base utilities.
                        </p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>3 Prime Projects (La Verde, Zagazig Uni, Berenice Military)</span>
                        </div>
                    </div>
                </div>

                <!-- Company 4: Hassan Allam -->
                <div class="timeline-item animate-on-scroll" data-side="left">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">2018 — 2021</span>
                        <h3 class="timeline-company">Hassan Allam Construction (حسن علام للإنشاءات)</h3>
                        <h4 class="timeline-role" data-en="Procurement Engineer" data-ar="مهندس مشتريات">Procurement Engineer</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Cairo, Egypt" data-ar="القاهرة، مصر">Cairo, Egypt</span></p>
                        <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.7; margin-bottom: 12px;">
                            Executed technical leveling and procurement for high-profile national projects including Aeon High-Rise Towers (20 floors), Zewail Science City, and Berenice Civil Airport.
                        </p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>4 Major Projects (Aeon Towers, Zewail City, Berenice Airport, Exhibition Center)</span>
                        </div>
                    </div>
                </div>

                <!-- Company 5: EDC Expertise -->
                <div class="timeline-item animate-on-scroll" data-side="right">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">2016 — 2018</span>
                        <h3 class="timeline-company">EDC Expertise (شركة الخبرات والمقاولات)</h3>
                        <h4 class="timeline-role" data-en="Junior Procurement Engineer" data-ar="مهندس مشتريات مبتدئ">Junior Procurement Engineer</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Riyadh, Saudi Arabia" data-ar="الرياض، المملكة العربية السعودية">Riyadh, Saudi Arabia</span></p>
                        <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.7; margin-bottom: 12px;">
                            Coordinated procurement for prestigious Riyadh landmarks including Riyadh Metro stations, Hilton Riyadh Hotel, Radisson Blu, and King Fahd Medical City.
                        </p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>5 Landmark Projects in Riyadh</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return get_head("Career Experience — Eng. Mostafa Abdelghany") + get_navbar("experience.html") + body + get_footer()

def build_certificates():
    body = """
    <div style="padding-top: 130px; background: var(--bg-secondary); border-bottom: 1px solid rgba(196,163,90,0.15);">
        <div class="container" style="padding-bottom: 60px;">
            <div class="section-title animate-on-scroll">
                <span class="title-number">01.</span>
                <span data-en="Official Certificates & Credentials" data-ar="الشهادات والمستندات الرسمية">Official Certificates & Credentials</span>
                <span class="title-line"></span>
            </div>

            <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 800px; line-height: 1.8; margin-bottom: 40px;" class="animate-on-scroll" data-en="Verified accreditations from the Saudi Council of Engineers, Bachelor of Science degree, and official letters of experience from premier contracting conglomerates." data-ar="اعتمادات رسمية موثقة من هيئة المهندسين السعوديين، شهادة بكالوريوس الهندسة، وشهادات الخبرة من كبرى المجموعات والشركات الإنشائية.">
                Verified accreditations from the Saudi Council of Engineers, Bachelor of Science degree, and official letters of experience from premier contracting conglomerates.
            </p>

            <div class="certs-grid">
                <!-- Card 1: SCE -->
                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-id-badge"></i></div>
                        <h3 data-en="Saudi Council of Engineers" data-ar="هيئة المهندسين السعوديين">Saudi Council of Engineers</h3>
                        <p data-en="Official Membership #1084929" data-ar="عضوية رسمية معتمدة #1084929">Official Membership #1084929</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Official accreditation letter from the Saudi Council of Engineers (SCE)." data-ar="خطاب اعتماد مهني رسمي من الهيئة السعودية للمهندسين.">Official accreditation letter from the Saudi Council of Engineers.</p>
                        <a href="assets/docs/Saudi_Council_of_Engineers_Letter.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download PDF" data-ar="تحميل PDF">Download PDF</span>
                        </a>
                    </div>
                </div>

                <!-- Card 2: CV -->
                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-file-pdf"></i></div>
                        <h3 data-en="Executive Procurement CV" data-ar="السيرة الذاتية المهنية 2026">Executive Procurement CV</h3>
                        <p data-en="Comprehensive Track 2026" data-ar="المسار التخصصي المتكامل">Comprehensive Track 2026</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Full professional curriculum vitae detailing 9+ years in MEP procurement." data-ar="سيرة ذاتية تنفيذية مفصلة توضح كافة المشاريع والخبرات.">Full professional curriculum vitae detailing 9+ years in MEP procurement.</p>
                        <a href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download PDF" data-ar="تحميل PDF">Download PDF</span>
                        </a>
                    </div>
                </div>

                <!-- Card 3: Atrium Experience -->
                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-award"></i></div>
                        <h3 data-en="Atrium TMG Experience" data-ar="شهادة خبرة أتريوم (طلعت مصطفى)">Atrium TMG Experience</h3>
                        <p data-en="Talaat Moustafa Group" data-ar="مجموعة طلعت مصطفى">Talaat Moustafa Group</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Experience certificate as Procurement Team Lead from Atrium (TMG)." data-ar="شهادة خبرة كرئيس فريق المشتريات بمجموعة طلعت مصطفى.">Experience certificate as Procurement Team Lead from Atrium.</p>
                        <a href="assets/docs/Atrium_Talaat_Moustafa_Experience_Certificate.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download PDF" data-ar="تحميل PDF">Download PDF</span>
                        </a>
                    </div>
                </div>

                <!-- Card 4: Pillars Experience -->
                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-award"></i></div>
                        <h3 data-en="Pillars Experience" data-ar="شهادة خبرة شركة بيلرز">Pillars Experience</h3>
                        <p data-en="Pillars Construction" data-ar="شركة بيلرز للإنشاءات">Pillars Construction</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Senior Procurement Engineer certificate from Pillars Construction." data-ar="شهادة خبرة كمهندس مشتريات أول من شركة بيلرز للإنشاءات.">Senior Procurement Engineer certificate from Pillars Construction.</p>
                        <a href="assets/docs/Pillars_Construction_Experience_Certificate.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download PDF" data-ar="تحميل PDF">Download PDF</span>
                        </a>
                    </div>
                </div>

                <!-- Card 5: Graduation -->
                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-graduation-cap"></i></div>
                        <h3 data-en="Graduation Degree" data-ar="شهادة التخرج الهندسية">Graduation Degree</h3>
                        <p data-en="B.Sc. Mechanical Engineering — Benha Univ." data-ar="بكالوريوس هندسة ميكانيكية — جامعة بنها">B.Sc. Mechanical Engineering</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Bachelor of Science in Mechanical Engineering certificate." data-ar="شهادة بكالوريوس العلوم في الهندسة الميكانيكية المعتمدة.">Bachelor of Science in Mechanical Engineering certificate.</p>
                        <a href="assets/docs/Graduation_Certificate.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download PDF" data-ar="تحميل PDF">Download PDF</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return get_head("Certificates & SCE Membership — Eng. Mostafa Abdelghany") + get_navbar("certificates.html") + body + get_footer()

def build_contact():
    body = """
    <div style="padding-top: 130px; background: var(--bg-secondary); border-bottom: 1px solid rgba(196,163,90,0.15);">
        <div class="container" style="padding-bottom: 60px;">
            <div class="section-title animate-on-scroll">
                <span class="title-number">01.</span>
                <span data-en="Get In Touch & Hire Me" data-ar="تواصل وتعاقد واستشارات">Get In Touch & Hire Me</span>
                <span class="title-line"></span>
            </div>

            <div class="contact-content">
                <div class="contact-info animate-on-scroll">
                    <p class="contact-intro" data-en="Whether you have an upcoming mega-project, require freelance MEP procurement consulting, need BOQ preparation, or want to discuss strategic executive roles, feel free to reach out directly." data-ar="سواء كنت تبحث عن استشارة متخصصة لمشروعك القادم، إعداد وتدقيق جداول الكميات، أو ترغب في مناقشة فرص قيادية استراتيجية، يسعدني تواصلك المباشر.">
                        Whether you have an upcoming mega-project, require freelance MEP procurement consulting, need BOQ preparation, or want to discuss strategic executive roles, feel free to reach out directly.
                    </p>

                    <div class="contact-cards">
                        <a href="https://wa.me/966502582122?text=Hello%20Eng.%20Mostafa,%20I%20would%20like%20to%20get%20in%20touch." target="_blank" class="contact-card magnetic-btn" style="border-color: #25D366; background: rgba(37,211,102,0.08);">
                            <i class="fab fa-whatsapp" style="color: #25D366;"></i>
                            <div>
                                <span class="contact-label" style="color: #25D366;" data-en="WhatsApp Direct" data-ar="واتساب مباشر">WhatsApp Direct</span>
                                <span class="contact-value">+966 502 582 122</span>
                            </div>
                        </a>

                        <a href="tel:+966502582122" class="contact-card magnetic-btn">
                            <i class="fas fa-phone"></i>
                            <div>
                                <span class="contact-label" data-en="Mobile Phone" data-ar="الهاتف المباشر">Mobile Phone</span>
                                <span class="contact-value">+966 502 582 122</span>
                            </div>
                        </a>

                        <a href="mailto:engmostafamahoud2012@gmail.com" class="contact-card magnetic-btn">
                            <i class="fas fa-envelope"></i>
                            <div>
                                <span class="contact-label" data-en="Email Address" data-ar="البريد الإلكتروني">Email Address</span>
                                <span class="contact-value">engmostafamahoud2012@gmail.com</span>
                            </div>
                        </a>

                        <a href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank" class="contact-card magnetic-btn">
                            <i class="fab fa-linkedin"></i>
                            <div>
                                <span class="contact-label">LinkedIn Profile</span>
                                <span class="contact-value" data-en="Connect on LinkedIn" data-ar="تواصل عبر لينكد إن">Connect on LinkedIn</span>
                            </div>
                        </a>

                        <div class="contact-card">
                            <i class="fas fa-map-marker-alt"></i>
                            <div>
                                <span class="contact-label" data-en="Location" data-ar="الموقع">Location</span>
                                <span class="contact-value" data-en="Riyadh, Kingdom of Saudi Arabia" data-ar="الرياض، المملكة العربية السعودية">Riyadh, Kingdom of Saudi Arabia</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Interactive Inquiry Form -->
                <form id="contact-form" class="contact-form animate-on-scroll">
                    <div class="form-group">
                        <input type="text" id="form-name" name="name" required placeholder=" ">
                        <label for="form-name" data-en="Your Full Name" data-ar="الاسم الكامل">Your Full Name</label>
                    </div>

                    <div class="form-group">
                        <input type="email" id="form-email" name="email" required placeholder=" ">
                        <label for="form-email" data-en="Your Email Address" data-ar="البريد الإلكتروني">Your Email Address</label>
                    </div>

                    <div class="form-group">
                        <select id="form-service" name="service" style="width: 100%; padding: 16px 18px; background: rgba(196,163,90,0.05); border: 1px solid rgba(196,163,90,0.15); border-radius: var(--radius-sm); color: var(--text-primary); outline: none;">
                            <option value="General Inquiry" style="background: #0A192F;">General Inquiry / تواصل عام</option>
                            <option value="Value Engineering & Cost Optimization" style="background: #0A192F;">Value Engineering & Cost Optimization / هندسة القيمة</option>
                            <option value="MEP Procurement Package" style="background: #0A192F;">MEP Procurement Package Management / إدارة حزم مشتريات</option>
                            <option value="BOQ Preparation & Review" style="background: #0A192F;">BOQ Preparation & Quantity Take-offs / إعداد جداول كميات</option>
                            <option value="Subcontract Negotiation" style="background: #0A192F;">Subcontract Negotiation / التفاوض على العقود</option>
                            <option value="Freelance Consultation" style="background: #0A192F;">Freelance MEP Consulting / استشارة فريلانس</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <input type="text" id="form-subject" name="subject" placeholder=" ">
                        <label for="form-subject" data-en="Subject / Project Title" data-ar="موضوع الرسالة / اسم المشروع">Subject / Project Title</label>
                    </div>

                    <div class="form-group">
                        <textarea id="form-message" name="message" rows="4" required placeholder=" "></textarea>
                        <label for="form-message" data-en="Describe Your Project or Inquiry..." data-ar="تفاصيل المشروع أو الاستفسار...">Describe Your Project or Inquiry...</label>
                    </div>

                    <button type="submit" class="btn btn-primary magnetic-btn" style="width: 100%; justify-content: center;">
                        <i class="fas fa-paper-plane"></i>
                        <span data-en="Send Message via WhatsApp / Email" data-ar="إرسال الطلب فوراً">Send Message via WhatsApp / Email</span>
                    </button>

                    <div id="form-status" class="form-status"></div>
                </form>
            </div>
        </div>
    </div>
    """
    return get_head("Contact & Hire Me — Eng. Mostafa Abdelghany") + get_navbar("contact.html") + body + get_footer()

def main():
    pages = {
        'index.html': build_index(),
        'about.html': build_about(),
        'services.html': build_services(),
        'software.html': build_software(),
        'projects.html': build_projects(),
        'project-detail.html': build_project_detail(),
        'experience.html': build_experience(),
        'certificates.html': build_certificates(),
        'contact.html': build_contact()
    }

    for filename, content in pages.items():
        file_path = os.path.join(BASE_DIR, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated: {filename} ({len(content):,} bytes)")

    print("\nAll 9 Multi-Page files generated successfully!")

if __name__ == '__main__':
    main()
