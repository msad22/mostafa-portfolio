#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Portfolio V2 index.html for Eng. Mostafa Abdelghany"""

import os

html = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Eng. Mostafa Abdelghany — MEP Procurement Section Head | 14+ Projects | 9+ Years Experience in KSA & Egypt">
    <meta name="keywords" content="MEP Procurement, Construction, Saudi Arabia, Egypt, Portfolio, Engineer">
    <meta name="author" content="Eng. Mostafa Abdelghany">
    <title>Eng. Mostafa Abdelghany — MEP Procurement Portfolio</title>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cairo:wght@300;400;600;700;800&family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet">

    <!-- Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />

    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

    <!-- Custom CSS -->
    <link rel="stylesheet" href="styles/main.css">
    <link rel="stylesheet" href="styles/animations.css">
    <link rel="stylesheet" href="styles/responsive.css">
</head>
<body>

    <!-- ============ SCROLL PROGRESS BAR ============ -->
    <div id="scroll-progress"></div>

    <!-- ============ NAVIGATION ============ -->
    <nav id="navbar" class="navbar">
        <div class="nav-container">
            <a href="#hero" class="nav-logo">
                <span class="logo-text">M</span><span class="logo-dot">.</span><span class="logo-text">A</span>
            </a>
            <ul class="nav-links" id="nav-links">
                <li><a href="#hero" class="nav-link active" data-en="Home" data-ar="الرئيسية">Home</a></li>
                <li><a href="#about" class="nav-link" data-en="About" data-ar="نبذة عني">About</a></li>
                <li><a href="#projects" class="nav-link" data-en="Projects" data-ar="المشاريع">Projects</a></li>
                <li><a href="#experience" class="nav-link" data-en="Experience" data-ar="الخبرات">Experience</a></li>
                <li><a href="#map" class="nav-link" data-en="Map" data-ar="الخريطة">Map</a></li>
                <li><a href="#certificates" class="nav-link" data-en="Certificates" data-ar="الشهادات">Certificates</a></li>
                <li><a href="#contact" class="nav-link" data-en="Contact" data-ar="تواصل">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <button id="lang-toggle" class="nav-btn" title="Toggle Language">
                    <span data-en="AR" data-ar="EN">AR</span>
                </button>
                <button id="theme-toggle" class="nav-btn" title="Toggle Theme">
                    <i class="fas fa-moon"></i>
                </button>
                <button class="hamburger" id="hamburger" aria-label="Toggle menu">
                    <span></span><span></span><span></span>
                </button>
            </div>
        </div>
    </nav>

    <!-- ============ HERO SECTION ============ -->
    <section id="hero" class="hero-section">
        <div id="particles-container" class="particles-bg"></div>
        <div class="hero-content">
            <div class="hero-text">
                <p class="hero-greeting animate-on-scroll" data-en="Hello, I'm" data-ar="مرحباً، أنا">Hello, I'm</p>
                <h1 class="hero-name animate-on-scroll">
                    <span data-en="Eng. Mostafa" data-ar="م. مصطفى">Eng. Mostafa</span>
                    <span class="gold-text" data-en="Abdelghany" data-ar="عبدالغني">Abdelghany</span>
                </h1>
                <div class="typewriter-container animate-on-scroll">
                    <span class="typewriter-prefix" data-en="I'm a " data-ar="أنا ">I'm a </span>
                    <span id="typewriter-text" class="typewriter-text"></span>
                    <span class="typewriter-cursor">|</span>
                </div>
                <p class="hero-desc animate-on-scroll" data-en="MEP Procurement Section Head at Zaid Al Hussain Group, Riyadh, KSA. Specializing in mega-scale construction procurement with 9+ years of expertise managing projects worth SAR 2.63+ Billion." data-ar="رئيس قسم مشتريات MEP في مجموعة زيد الحصين، الرياض. متخصص في مشتريات البناء الضخمة مع خبرة 9+ سنوات في إدارة مشاريع بقيمة 2.63+ مليار ريال.">
                    MEP Procurement Section Head at Zaid Al Hussain Group, Riyadh, KSA. Specializing in mega-scale construction procurement with 9+ years of expertise managing projects worth SAR 2.63+ Billion.
                </p>
                <div class="hero-btns animate-on-scroll">
                    <a href="#projects" class="btn btn-primary magnetic-btn">
                        <i class="fas fa-building"></i>
                        <span data-en="View Projects" data-ar="عرض المشاريع">View Projects</span>
                    </a>
                    <a href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download class="btn btn-outline magnetic-btn">
                        <i class="fas fa-download"></i>
                        <span data-en="Download CV" data-ar="تحميل السيرة الذاتية">Download CV</span>
                    </a>
                </div>
                <div class="hero-badges animate-on-scroll">
                    <span class="badge"><i class="fas fa-map-marker-alt"></i> <span data-en="Riyadh, KSA" data-ar="الرياض، السعودية">Riyadh, KSA</span></span>
                    <span class="badge"><i class="fas fa-id-card"></i> SCE #1084929</span>
                    <span class="badge"><i class="fas fa-graduation-cap"></i> B.Sc. Mech. Eng.</span>
                </div>
            </div>
            <div class="hero-image animate-on-scroll">
                <div class="headshot-wrapper">
                    <img src="assets/images/headshot.jpg" alt="Eng. Mostafa Abdelghany" class="headshot-img" loading="eager">
                    <div class="headshot-ring"></div>
                    <div class="headshot-glow"></div>
                </div>
            </div>
        </div>
        <a href="#about" class="scroll-indicator" aria-label="Scroll down">
            <div class="scroll-arrow">
                <i class="fas fa-chevron-down"></i>
            </div>
        </a>
    </section>

    <!-- ============ ABOUT SECTION ============ -->
    <section id="about" class="section about-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">
                <span class="title-number">01.</span>
                <span data-en="About Me" data-ar="نبذة عني">About Me</span>
                <span class="title-line"></span>
            </h2>
            <div class="about-content">
                <div class="about-text animate-on-scroll">
                    <p data-en="Results-driven MEP Procurement professional with over 9 years of progressive experience in Saudi Arabia and Egypt. Currently leading procurement operations for the SAR 2.63 Billion King Abdullah International Gardens (KAIG) project — one of the largest landscape and infrastructure projects in the Middle East." data-ar="محترف مشتريات MEP موجه بالنتائج مع أكثر من 9 سنوات خبرة تصاعدية في السعودية ومصر. حالياً أقود عمليات المشتريات لمشروع حدائق الملك عبدالله الدولية (KAIG) بقيمة 2.63 مليار ريال — أحد أكبر مشاريع البنية التحتية في الشرق الأوسط.">
                        Results-driven MEP Procurement professional with over 9 years of progressive experience in Saudi Arabia and Egypt. Currently leading procurement operations for the SAR 2.63 Billion King Abdullah International Gardens (KAIG) project — one of the largest landscape and infrastructure projects in the Middle East.
                    </p>
                    <p data-en="Expert in vendor management, contract negotiation, cost optimization, and supply chain coordination for HVAC, electrical, plumbing, and fire-fighting systems across mega-scale construction projects." data-ar="خبير في إدارة الموردين، التفاوض على العقود، تحسين التكاليف، وتنسيق سلسلة الإمداد لأنظمة HVAC والكهرباء والسباكة ومكافحة الحرائق في مشاريع البناء الضخمة.">
                        Expert in vendor management, contract negotiation, cost optimization, and supply chain coordination for HVAC, electrical, plumbing, and fire-fighting systems across mega-scale construction projects.
                    </p>
                </div>

                <!-- KPI Counters -->
                <div class="kpi-grid animate-on-scroll">
                    <div class="kpi-card">
                        <div class="kpi-icon"><i class="fas fa-building"></i></div>
                        <span class="kpi-number" data-target="14">0</span>
                        <span class="kpi-label" data-en="Projects" data-ar="مشروع">Projects</span>
                    </div>
                    <div class="kpi-card">
                        <div class="kpi-icon"><i class="fas fa-clock"></i></div>
                        <span class="kpi-number" data-target="9" data-suffix="+">0</span>
                        <span class="kpi-label" data-en="Years Experience" data-ar="سنوات خبرة">Years Experience</span>
                    </div>
                    <div class="kpi-card">
                        <div class="kpi-icon"><i class="fas fa-briefcase"></i></div>
                        <span class="kpi-number" data-target="5">0</span>
                        <span class="kpi-label" data-en="Companies" data-ar="شركات">Companies</span>
                    </div>
                    <div class="kpi-card">
                        <div class="kpi-icon"><i class="fas fa-coins"></i></div>
                        <span class="kpi-number" data-target="2.63" data-prefix="SAR " data-suffix="B" data-decimal="true">0</span>
                        <span class="kpi-label" data-en="Managed Value" data-ar="قيمة مُدارة">Managed Value</span>
                    </div>
                </div>

                <!-- Skills -->
                <div class="skills-grid animate-on-scroll">
                    <h3 class="subsection-title" data-en="Core Competencies" data-ar="الكفاءات الأساسية">Core Competencies</h3>
                    <div class="skill-item">
                        <div class="skill-header">
                            <span data-en="MEP Procurement" data-ar="مشتريات MEP">MEP Procurement</span>
                            <span class="skill-percent">95%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-percentage="95"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="skill-header">
                            <span data-en="Vendor Management" data-ar="إدارة الموردين">Vendor Management</span>
                            <span class="skill-percent">92%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-percentage="92"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="skill-header">
                            <span data-en="Contract Negotiation" data-ar="التفاوض على العقود">Contract Negotiation</span>
                            <span class="skill-percent">90%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-percentage="90"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="skill-header">
                            <span data-en="Cost Optimization" data-ar="تحسين التكاليف">Cost Optimization</span>
                            <span class="skill-percent">88%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-percentage="88"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="skill-header">
                            <span data-en="Supply Chain Management" data-ar="إدارة سلسلة الإمداد">Supply Chain Management</span>
                            <span class="skill-percent">90%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-percentage="90"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="skill-header">
                            <span data-en="Technical Evaluation" data-ar="التقييم الفني">Technical Evaluation</span>
                            <span class="skill-percent">87%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-percentage="87"></div></div>
                    </div>
                </div>

                <!-- Tags -->
                <div class="competency-tags animate-on-scroll">
                    <span class="tag">HVAC Systems</span>
                    <span class="tag">Electrical Systems</span>
                    <span class="tag">Plumbing</span>
                    <span class="tag">Fire Fighting</span>
                    <span class="tag">BOQ Preparation</span>
                    <span class="tag">ERP Systems</span>
                    <span class="tag">Material Submittals</span>
                    <span class="tag">Subcontractor Management</span>
                    <span class="tag">RFQ/RFP</span>
                    <span class="tag">ISO Standards</span>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ PROJECTS SECTION ============ -->
    <section id="projects" class="section projects-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">
                <span class="title-number">02.</span>
                <span data-en="Featured Projects" data-ar="المشاريع المميزة">Featured Projects</span>
                <span class="title-line"></span>
            </h2>

            <!-- Filter Tabs -->
            <div class="filter-tabs animate-on-scroll">
                <button class="filter-tab active" data-filter="all" data-en="All Projects" data-ar="كل المشاريع">All Projects <span class="filter-count">14</span></button>
                <button class="filter-tab" data-filter="ksa" data-en="KSA" data-ar="السعودية">KSA <span class="filter-count">6</span></button>
                <button class="filter-tab" data-filter="egypt" data-en="Egypt" data-ar="مصر">Egypt <span class="filter-count">8</span></button>
            </div>

            <!-- Projects Grid -->
            <div class="projects-grid">

                <!-- Project 1: KAIG (Flagship) -->
                <div class="project-card featured" data-category="ksa" data-id="1"
                     data-name="King Abdullah International Gardens (KAIG)"
                     data-name-ar="حدائق الملك عبدالله الدولية"
                     data-company="Zaid Al Hussain Group"
                     data-role="MEP Procurement Section Head"
                     data-year="Oct 2024 — Present"
                     data-location="Riyadh, KSA"
                     data-value="SAR 2.63 Billion"
                     data-client="Riyadh Municipality"
                     data-stakeholders="Barton Willmore (Masterplanner), Buro Happold (Structural), Dar Al-Handasah (Technical Review), Omrania & Egis Group (Supervision)"
                     data-images="assets/images/projects/kaig_1.jpg,assets/images/projects/kaig_2.jpg,assets/images/projects/kaig_3.jpg,assets/images/projects/kaig_4.jpg,assets/images/projects/kaig_5.jpg,assets/images/projects/kaig_6.jpg,assets/images/projects/kaig_7.jpg"
                     data-desc="One of the largest landscape and infrastructure mega-projects in the Middle East. Leading MEP procurement for HVAC, electrical, plumbing, and fire-fighting systems.">
                    <div class="card-image">
                        <img src="assets/images/projects/kaig_6.jpg" alt="King Abdullah International Gardens" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-badge featured-badge">Flagship Project</span>
                        <span class="card-country"><i class="fas fa-flag"></i> KSA</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">King Abdullah International Gardens</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Zaid Al Hussain Group</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2024 — Present</span>
                            <span><i class="fas fa-map-marker-alt"></i> Riyadh</span>
                        </div>
                        <div class="card-value">SAR 2.63 Billion</div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">MEP Procurement Section Head</p>
                        <p class="hover-client">Client: Riyadh Municipality</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 2: Riyadh Metro -->
                <div class="project-card" data-category="ksa" data-id="2"
                     data-name="Riyadh Metro Project"
                     data-name-ar="مشروع مترو الرياض"
                     data-company="EDC Expertise"
                     data-role="Junior Procurement Engineer"
                     data-year="2016 — 2017"
                     data-location="Riyadh, KSA"
                     data-value=""
                     data-client=""
                     data-stakeholders=""
                     data-images="assets/images/projects/riyadh_metro_1.jpg,assets/images/projects/riyadh_metro_2.jpg"
                     data-desc="Part of the world's largest urban transit project. Managed MEP procurement for metro station infrastructure.">
                    <div class="card-image">
                        <img src="assets/images/projects/riyadh_metro_1.jpg" alt="Riyadh Metro Project" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> KSA</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Riyadh Metro Project</h3>
                        <p class="card-company"><i class="fas fa-building"></i> EDC Expertise</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2016 — 2017</span>
                            <span><i class="fas fa-map-marker-alt"></i> Riyadh</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Junior Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 3: Radisson Blu -->
                <div class="project-card" data-category="ksa" data-id="3"
                     data-name="Radisson Blu Hotel Riyadh"
                     data-name-ar="فندق راديسون بلو الرياض"
                     data-company="EDC Expertise"
                     data-role="Junior Procurement Engineer"
                     data-year="2018"
                     data-location="Riyadh, KSA"
                     data-images="assets/images/projects/radisson_riyadh_1.jpg"
                     data-desc="Luxury hotel project procurement for MEP systems including HVAC, electrical, and plumbing.">
                    <div class="card-image">
                        <img src="assets/images/projects/radisson_riyadh_1.jpg" alt="Radisson Blu Hotel Riyadh" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> KSA</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Radisson Blu Hotel</h3>
                        <p class="card-company"><i class="fas fa-building"></i> EDC Expertise</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2018</span>
                            <span><i class="fas fa-map-marker-alt"></i> Riyadh</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Junior Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 4: Hilton Riyadh -->
                <div class="project-card" data-category="ksa" data-id="4"
                     data-name="Hilton Riyadh Hotel & Residences"
                     data-name-ar="فندق هيلتون الرياض"
                     data-company="EDC Expertise"
                     data-role="Junior Procurement Engineer"
                     data-year="2018"
                     data-location="Riyadh, KSA"
                     data-images="assets/images/projects/hilton_riyadh_3.jpg,assets/images/projects/hilton_riyadh_4.jpg"
                     data-desc="Five-star hotel and residences project. Managed procurement for MEP systems and installations.">
                    <div class="card-image">
                        <img src="assets/images/projects/hilton_riyadh_3.jpg" alt="Hilton Riyadh Hotel" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> KSA</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Hilton Riyadh Hotel & Residences</h3>
                        <p class="card-company"><i class="fas fa-building"></i> EDC Expertise</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2018</span>
                            <span><i class="fas fa-map-marker-alt"></i> Riyadh</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Junior Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 5: King Fahd Medical City -->
                <div class="project-card" data-category="ksa" data-id="5"
                     data-name="King Fahd Medical City"
                     data-name-ar="مدينة الملك فهد الطبية"
                     data-company="EDC Expertise"
                     data-role="Junior Procurement Engineer"
                     data-year="2017"
                     data-location="Riyadh, KSA"
                     data-images="assets/images/project_5.jpg"
                     data-desc="Major healthcare facility. Procurement of specialized medical MEP systems and equipment.">
                    <div class="card-image">
                        <img src="assets/images/project_5.jpg" alt="King Fahd Medical City" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> KSA</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">King Fahd Medical City</h3>
                        <p class="card-company"><i class="fas fa-building"></i> EDC Expertise</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2017</span>
                            <span><i class="fas fa-map-marker-alt"></i> Riyadh</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Junior Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 6: Haifa Compound -->
                <div class="project-card" data-category="ksa" data-id="6"
                     data-name="Haifa Compound"
                     data-name-ar="مجمع حيفا السكني"
                     data-company="EDC Expertise"
                     data-role="Junior Procurement Engineer"
                     data-year="2017"
                     data-location="Riyadh, KSA"
                     data-images="assets/images/project_6.jpg"
                     data-desc="Residential compound project. Managed procurement for MEP systems including HVAC and electrical.">
                    <div class="card-image">
                        <img src="assets/images/project_6.jpg" alt="Haifa Compound" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> KSA</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Haifa Compound</h3>
                        <p class="card-company"><i class="fas fa-building"></i> EDC Expertise</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2017</span>
                            <span><i class="fas fa-map-marker-alt"></i> Riyadh</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Junior Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 7: Noor City -->
                <div class="project-card featured" data-category="egypt" data-id="7"
                     data-name="Noor City Mega Compound"
                     data-name-ar="مشروع مدينة نور الضخم"
                     data-company="Atrium Quality Contractors (Talaat Moustafa Group)"
                     data-role="Procurement Team Lead"
                     data-year="2023 — 2024"
                     data-location="New Administrative Capital, Egypt"
                     data-images="assets/images/projects/noor_city_1.jpg,assets/images/projects/noor_city_2.jpeg,assets/images/projects/noor_city_3.jpeg,assets/images/projects/noor_city_4.jpg,assets/images/projects/noor_city_5.jpg,assets/images/projects/noor_city_6.jpg"
                     data-desc="Mega residential compound by Talaat Moustafa Group in the New Administrative Capital. Led procurement team for full MEP scope.">
                    <div class="card-image">
                        <img src="assets/images/projects/noor_city_1.jpg" alt="Noor City Mega Compound" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-badge">Mega Project</span>
                        <span class="card-country"><i class="fas fa-flag"></i> Egypt</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Noor City Mega Compound</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Atrium (Talaat Moustafa Group)</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2023 — 2024</span>
                            <span><i class="fas fa-map-marker-alt"></i> New Capital</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Procurement Team Lead</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 8: Zewail City -->
                <div class="project-card" data-category="egypt" data-id="8"
                     data-name="Zewail City of Science & Technology"
                     data-name-ar="مدينة زويل للعلوم والتكنولوجيا"
                     data-company="Hassan Allam Construction"
                     data-role="Procurement Engineer"
                     data-year="2019"
                     data-location="6th October City, Egypt"
                     data-images="assets/images/projects/zewail_city_1.jpg,assets/images/projects/zewail_city_3.jpeg,assets/images/projects/zewail_city_4.jpg"
                     data-desc="Prestigious science and technology university campus. Managed procurement for educational facility MEP systems.">
                    <div class="card-image">
                        <img src="assets/images/projects/zewail_city_1.jpg" alt="Zewail City" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> Egypt</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Zewail City of Science & Technology</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Hassan Allam Construction</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2019</span>
                            <span><i class="fas fa-map-marker-alt"></i> 6th October</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 9: Aeon Towers -->
                <div class="project-card" data-category="egypt" data-id="9"
                     data-name="Aeon Towers (20 Floors)"
                     data-name-ar="أبراج إيون (20 طابق)"
                     data-company="Hassan Allam Construction"
                     data-role="Procurement Engineer"
                     data-year="2020 — 2021"
                     data-location="6th October City, Egypt"
                     data-images="assets/images/projects/aeon_towers_1.jpeg,assets/images/projects/aeon_towers_2.jpeg,assets/images/projects/aeon_towers_3.jpeg,assets/images/projects/aeon_towers_4.jpeg"
                     data-desc="High-rise 20-floor residential towers project. Managed procurement for full MEP scope including high-rise-specific systems.">
                    <div class="card-image">
                        <img src="assets/images/projects/aeon_towers_1.jpeg" alt="Aeon Towers" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> Egypt</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Aeon Towers (20 Floors)</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Hassan Allam Construction</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2020 — 2021</span>
                            <span><i class="fas fa-map-marker-alt"></i> 6th October</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 10: Egypt Exhibition Center -->
                <div class="project-card" data-category="egypt" data-id="10"
                     data-name="Egypt International Exhibition Center"
                     data-name-ar="مركز مصر الدولي للمعارض"
                     data-company="Hassan Allam Construction"
                     data-role="Procurement Engineer"
                     data-year="2016"
                     data-location="New Cairo, Egypt"
                     data-images="assets/images/projects/egyptian_space_agency_1.jpeg"
                     data-desc="Major exhibition and conference facility in New Cairo. Managed procurement for large-span MEP systems.">
                    <div class="card-image">
                        <img src="assets/images/projects/egyptian_space_agency_1.jpeg" alt="Egypt Exhibition Center" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> Egypt</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Egypt International Exhibition Center</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Hassan Allam Construction</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2016</span>
                            <span><i class="fas fa-map-marker-alt"></i> New Cairo</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 11: Berenice Airport -->
                <div class="project-card" data-category="egypt" data-id="11"
                     data-name="Berenice Civil Airport"
                     data-name-ar="مطار برنيس المدني"
                     data-company="Hassan Allam Construction"
                     data-role="Procurement Engineer"
                     data-year="2019"
                     data-location="Red Sea, Egypt"
                     data-images="assets/images/projects/berenice_airport_1.jpeg"
                     data-desc="Civil airport project in the Red Sea region. Managed procurement for airport MEP infrastructure.">
                    <div class="card-image">
                        <img src="assets/images/projects/berenice_airport_1.jpeg" alt="Berenice Airport" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> Egypt</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Berenice Civil Airport</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Hassan Allam Construction</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2019</span>
                            <span><i class="fas fa-map-marker-alt"></i> Red Sea</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 12: Berenice Military -->
                <div class="project-card" data-category="egypt" data-id="12"
                     data-name="Berenice Military Air Base"
                     data-name-ar="قاعدة برنيس الجوية العسكرية"
                     data-company="Pillars Construction"
                     data-role="Senior Procurement Engineer"
                     data-year="2020"
                     data-location="Red Sea, Egypt"
                     data-images="assets/images/project_12.jpg"
                     data-desc="Military air base facility. Managed specialized procurement for military-grade MEP systems.">
                    <div class="card-image">
                        <img src="assets/images/project_12.jpg" alt="Berenice Military Air Base" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> Egypt</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Berenice Military Air Base</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Pillars Construction</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2020</span>
                            <span><i class="fas fa-map-marker-alt"></i> Red Sea</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Senior Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 13: Zagazig University -->
                <div class="project-card" data-category="egypt" data-id="13"
                     data-name="Zagazig University Campus"
                     data-name-ar="حرم جامعة الزقازيق"
                     data-company="Pillars Construction"
                     data-role="Senior Procurement Engineer"
                     data-year="2023"
                     data-location="Sharqia, Egypt"
                     data-images="assets/images/projects/zagazig_uni_1.jpeg,assets/images/projects/zagazig_uni_2.jpg,assets/images/projects/zagazig_uni_3.jpg,assets/images/projects/zagazig_uni_4.jpg"
                     data-desc="University campus expansion project. Managed procurement for educational facility MEP systems.">
                    <div class="card-image">
                        <img src="assets/images/projects/zagazig_uni_1.jpeg" alt="Zagazig University" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> Egypt</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">Zagazig University Campus</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Pillars Construction</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2023</span>
                            <span><i class="fas fa-map-marker-alt"></i> Sharqia</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Senior Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Project 14: La Verde -->
                <div class="project-card" data-category="egypt" data-id="14"
                     data-name="La Verde Compound"
                     data-name-ar="كمبوند لا فيردي"
                     data-company="Pillars Construction"
                     data-role="Senior Procurement Engineer"
                     data-year="2021 — 2022"
                     data-location="New Administrative Capital, Egypt"
                     data-images="assets/images/project_14.jpg"
                     data-desc="Luxury residential compound in the New Administrative Capital. Managed procurement for residential MEP systems.">
                    <div class="card-image">
                        <img src="assets/images/project_14.jpg" alt="La Verde Compound" loading="lazy">
                        <div class="card-overlay"></div>
                        <span class="card-country"><i class="fas fa-flag"></i> Egypt</span>
                    </div>
                    <div class="card-content">
                        <div class="card-accent"></div>
                        <h3 class="card-title">La Verde Compound</h3>
                        <p class="card-company"><i class="fas fa-building"></i> Pillars Construction</p>
                        <div class="card-meta">
                            <span><i class="fas fa-calendar"></i> 2021 — 2022</span>
                            <span><i class="fas fa-map-marker-alt"></i> New Capital</span>
                        </div>
                    </div>
                    <div class="card-hover-info">
                        <p class="hover-role">Senior Procurement Engineer</p>
                        <button class="btn-view-details">View Details <i class="fas fa-arrow-right"></i></button>
                    </div>
                </div>

            </div><!-- /projects-grid -->
        </div>
    </section>

    <!-- ============ PROJECT MODAL ============ -->
    <div id="project-modal" class="modal-overlay" role="dialog" aria-hidden="true">
        <div class="modal-content">
            <button class="modal-close" aria-label="Close">&times;</button>
            <div class="modal-carousel">
                <div class="carousel-track" id="carousel-track"></div>
                <button class="carousel-btn carousel-prev"><i class="fas fa-chevron-left"></i></button>
                <button class="carousel-btn carousel-next"><i class="fas fa-chevron-right"></i></button>
                <div class="carousel-dots" id="carousel-dots"></div>
            </div>
            <div class="modal-details">
                <h3 id="modal-title" class="modal-title"></h3>
                <div class="modal-info-grid">
                    <div class="modal-info-item">
                        <span class="info-label"><i class="fas fa-building"></i> Company</span>
                        <span id="modal-company" class="info-value"></span>
                    </div>
                    <div class="modal-info-item">
                        <span class="info-label"><i class="fas fa-user-tie"></i> Role</span>
                        <span id="modal-role" class="info-value"></span>
                    </div>
                    <div class="modal-info-item">
                        <span class="info-label"><i class="fas fa-calendar"></i> Period</span>
                        <span id="modal-year" class="info-value"></span>
                    </div>
                    <div class="modal-info-item">
                        <span class="info-label"><i class="fas fa-map-marker-alt"></i> Location</span>
                        <span id="modal-location" class="info-value"></span>
                    </div>
                    <div class="modal-info-item" id="modal-value-container">
                        <span class="info-label"><i class="fas fa-coins"></i> Project Value</span>
                        <span id="modal-value" class="info-value gold-text"></span>
                    </div>
                    <div class="modal-info-item" id="modal-client-container">
                        <span class="info-label"><i class="fas fa-handshake"></i> Client</span>
                        <span id="modal-client" class="info-value"></span>
                    </div>
                </div>
                <p id="modal-desc" class="modal-desc"></p>
                <div id="modal-stakeholders-container" class="modal-stakeholders">
                    <h4><i class="fas fa-users"></i> Key Stakeholders</h4>
                    <p id="modal-stakeholders"></p>
                </div>
            </div>
        </div>
    </div>

    <!-- ============ EXPERIENCE TIMELINE ============ -->
    <section id="experience" class="section experience-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">
                <span class="title-number">03.</span>
                <span data-en="Career Journey" data-ar="المسيرة المهنية">Career Journey</span>
                <span class="title-line"></span>
            </h2>

            <div class="timeline">
                <!-- Timeline Item 1: Current -->
                <div class="timeline-item animate-on-scroll" data-side="right">
                    <div class="timeline-dot current"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">Oct 2024 — Present</span>
                        <h3 class="timeline-company">Zaid Al Hussain Group</h3>
                        <h4 class="timeline-role" data-en="MEP Procurement Section Head" data-ar="رئيس قسم مشتريات MEP">MEP Procurement Section Head</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Riyadh, KSA" data-ar="الرياض، السعودية">Riyadh, KSA</span></p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>1 Flagship Project (KAIG — SAR 2.63B)</span>
                        </div>
                    </div>
                </div>

                <!-- Timeline Item 2 -->
                <div class="timeline-item animate-on-scroll" data-side="left">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">2023 — 2024</span>
                        <h3 class="timeline-company">Atrium Quality Contractors</h3>
                        <h4 class="timeline-role" data-en="Procurement Team Lead" data-ar="رئيس فريق المشتريات">Procurement Team Lead</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Cairo, Egypt" data-ar="القاهرة، مصر">Cairo, Egypt</span></p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>1 Mega Project (Noor City — TMG)</span>
                        </div>
                    </div>
                </div>

                <!-- Timeline Item 3 -->
                <div class="timeline-item animate-on-scroll" data-side="right">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">2020 — 2022</span>
                        <h3 class="timeline-company">Pillars Constructions</h3>
                        <h4 class="timeline-role" data-en="Senior Procurement Engineer" data-ar="مهندس مشتريات أول">Senior Procurement Engineer</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Cairo, Egypt" data-ar="القاهرة، مصر">Cairo, Egypt</span></p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>3 Projects</span>
                        </div>
                    </div>
                </div>

                <!-- Timeline Item 4 -->
                <div class="timeline-item animate-on-scroll" data-side="left">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">2018 — 2021</span>
                        <h3 class="timeline-company">Hassan Allam Construction</h3>
                        <h4 class="timeline-role" data-en="Procurement Engineer" data-ar="مهندس مشتريات">Procurement Engineer</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Cairo, Egypt" data-ar="القاهرة، مصر">Cairo, Egypt</span></p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>4 Projects</span>
                        </div>
                    </div>
                </div>

                <!-- Timeline Item 5 -->
                <div class="timeline-item animate-on-scroll" data-side="right">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card glass-card">
                        <span class="timeline-date">2016 — 2018</span>
                        <h3 class="timeline-company">EDC Expertise</h3>
                        <h4 class="timeline-role" data-en="Junior Procurement Engineer" data-ar="مهندس مشتريات مبتدئ">Junior Procurement Engineer</h4>
                        <p class="timeline-location"><i class="fas fa-map-marker-alt"></i> <span data-en="Riyadh, KSA" data-ar="الرياض، السعودية">Riyadh, KSA</span></p>
                        <div class="timeline-projects-count">
                            <i class="fas fa-building"></i> <span>5 Projects</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ MAP SECTION ============ -->
    <section id="map" class="section map-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">
                <span class="title-number">04.</span>
                <span data-en="Project Locations" data-ar="مواقع المشاريع">Project Locations</span>
                <span class="title-line"></span>
            </h2>
            <div class="map-wrapper animate-on-scroll">
                <div class="map-filters">
                    <button class="map-filter-btn active" data-filter="all" data-en="All" data-ar="الكل">All</button>
                    <button class="map-filter-btn" data-filter="ksa" data-en="KSA" data-ar="السعودية">KSA</button>
                    <button class="map-filter-btn" data-filter="egypt" data-en="Egypt" data-ar="مصر">Egypt</button>
                </div>
                <div id="project-map" class="project-map"></div>
            </div>
        </div>
    </section>

    <!-- ============ CERTIFICATES SECTION ============ -->
    <section id="certificates" class="section certificates-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">
                <span class="title-number">05.</span>
                <span data-en="Certificates & Documents" data-ar="الشهادات والمستندات">Certificates & Documents</span>
                <span class="title-line"></span>
            </h2>
            <div class="certs-grid">
                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-file-pdf"></i></div>
                        <h3 data-en="Professional CV" data-ar="السيرة الذاتية">Professional CV</h3>
                        <p data-en="Procurement Track — 2026" data-ar="مسار المشتريات — 2026">Procurement Track — 2026</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Comprehensive CV detailing 9+ years in MEP procurement across KSA & Egypt." data-ar="سيرة ذاتية شاملة تفصل 9+ سنوات في مشتريات MEP في السعودية ومصر.">Comprehensive CV detailing 9+ years in MEP procurement across KSA & Egypt.</p>
                        <a href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download" data-ar="تحميل">Download</span>
                        </a>
                    </div>
                </div>

                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-certificate"></i></div>
                        <h3 data-en="SCE Membership" data-ar="عضوية هيئة المهندسين">SCE Membership</h3>
                        <p data-en="Saudi Council of Engineers — #1084929" data-ar="هيئة المهندسين السعوديين — #1084929">Saudi Council of Engineers — #1084929</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Official membership letter from Saudi Council of Engineers." data-ar="خطاب عضوية رسمي من هيئة المهندسين السعوديين.">Official membership letter from Saudi Council of Engineers.</p>
                        <a href="assets/docs/Saudi_Council_of_Engineers_Letter.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download" data-ar="تحميل">Download</span>
                        </a>
                    </div>
                </div>

                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-award"></i></div>
                        <h3 data-en="Atrium Experience" data-ar="خبرة اتريم">Atrium Experience</h3>
                        <p data-en="Talaat Moustafa Group" data-ar="مجموعة طلعت مصطفى">Talaat Moustafa Group</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Experience certificate from Atrium Quality Contractors — Talaat Moustafa Group." data-ar="شهادة خبرة من شركة اتريم — مجموعة طلعت مصطفى.">Experience certificate from Atrium Quality Contractors.</p>
                        <a href="assets/docs/Atrium_Talaat_Moustafa_Experience_Certificate.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download" data-ar="تحميل">Download</span>
                        </a>
                    </div>
                </div>

                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-award"></i></div>
                        <h3 data-en="Pillars Experience" data-ar="خبرة بيلرز">Pillars Experience</h3>
                        <p data-en="Pillars Construction" data-ar="شركة بيلرز للإنشاءات">Pillars Construction</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Experience certificate from Pillars Construction Company." data-ar="شهادة خبرة من شركة بيلرز للإنشاءات.">Experience certificate from Pillars Construction Company.</p>
                        <a href="assets/docs/Pillars_Construction_Experience_Certificate.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download" data-ar="تحميل">Download</span>
                        </a>
                    </div>
                </div>

                <div class="cert-card animate-on-scroll">
                    <div class="cert-front">
                        <div class="cert-icon"><i class="fas fa-graduation-cap"></i></div>
                        <h3 data-en="Graduation Certificate" data-ar="شهادة التخرج">Graduation Certificate</h3>
                        <p data-en="B.Sc. Mechanical Engineering — Benha University" data-ar="بكالوريوس هندسة ميكانيكية — جامعة بنها">B.Sc. Mech. Eng. — Benha University</p>
                    </div>
                    <div class="cert-back">
                        <p data-en="Bachelor of Science in Mechanical Engineering from Benha University." data-ar="بكالوريوس العلوم في الهندسة الميكانيكية من جامعة بنها.">Bachelor of Science in Mechanical Engineering from Benha University.</p>
                        <a href="assets/docs/Graduation_Certificate.pdf" download class="btn btn-sm">
                            <i class="fas fa-download"></i> <span data-en="Download" data-ar="تحميل">Download</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============ CONTACT SECTION ============ -->
    <section id="contact" class="section contact-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">
                <span class="title-number">06.</span>
                <span data-en="Get In Touch" data-ar="تواصل معي">Get In Touch</span>
                <span class="title-line"></span>
            </h2>
            <div class="contact-content">
                <div class="contact-info animate-on-scroll">
                    <p class="contact-intro" data-en="I'm always open to discussing new opportunities, challenging projects, or partnerships. Feel free to reach out!" data-ar="أنا دائماً منفتح لمناقشة فرص جديدة أو مشاريع صعبة أو شراكات. لا تتردد في التواصل!">
                        I'm always open to discussing new opportunities, challenging projects, or partnerships. Feel free to reach out!
                    </p>
                    <div class="contact-cards">
                        <a href="tel:+966502582122" class="contact-card magnetic-btn">
                            <i class="fas fa-phone"></i>
                            <div>
                                <span class="contact-label" data-en="Phone" data-ar="الهاتف">Phone</span>
                                <span class="contact-value">+966 502 582 122</span>
                            </div>
                        </a>
                        <a href="mailto:engmostafamahoud2012@gmail.com" class="contact-card magnetic-btn">
                            <i class="fas fa-envelope"></i>
                            <div>
                                <span class="contact-label" data-en="Email" data-ar="البريد">Email</span>
                                <span class="contact-value">engmostafamahoud2012@gmail.com</span>
                            </div>
                        </a>
                        <a href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank" class="contact-card magnetic-btn">
                            <i class="fab fa-linkedin"></i>
                            <div>
                                <span class="contact-label">LinkedIn</span>
                                <span class="contact-value" data-en="View Profile" data-ar="عرض الملف">View Profile</span>
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

                <form id="contact-form" class="contact-form animate-on-scroll">
                    <div class="form-group">
                        <input type="text" id="form-name" name="name" required placeholder=" ">
                        <label for="form-name" data-en="Your Name" data-ar="الاسم">Your Name</label>
                    </div>
                    <div class="form-group">
                        <input type="email" id="form-email" name="email" required placeholder=" ">
                        <label for="form-email" data-en="Your Email" data-ar="البريد الإلكتروني">Your Email</label>
                    </div>
                    <div class="form-group">
                        <input type="text" id="form-subject" name="subject" placeholder=" ">
                        <label for="form-subject" data-en="Subject" data-ar="الموضوع">Subject</label>
                    </div>
                    <div class="form-group">
                        <textarea id="form-message" name="message" rows="5" required placeholder=" "></textarea>
                        <label for="form-message" data-en="Message" data-ar="الرسالة">Message</label>
                    </div>
                    <button type="submit" class="btn btn-primary magnetic-btn">
                        <i class="fas fa-paper-plane"></i>
                        <span data-en="Send Message" data-ar="إرسال الرسالة">Send Message</span>
                    </button>
                    <div id="form-status" class="form-status"></div>
                </form>
            </div>
        </div>
    </section>

    <!-- ============ FOOTER ============ -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p data-en="Designed & Built by Eng. Mostafa Abdelghany" data-ar="تصميم وبناء م. مصطفى عبدالغني">Designed & Built by Eng. Mostafa Abdelghany</p>
                <div class="footer-links">
                    <a href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank"><i class="fab fa-linkedin"></i></a>
                    <a href="mailto:engmostafamahoud2012@gmail.com"><i class="fas fa-envelope"></i></a>
                    <a href="tel:+966502582122"><i class="fas fa-phone"></i></a>
                </div>
                <p class="footer-copy">&copy; 2026 All Rights Reserved</p>
            </div>
        </div>
    </footer>

    <!-- ============ FLOATING CV BUTTON ============ -->
    <a href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download id="cv-float-btn" class="cv-float-btn" title="Download CV">
        <i class="fas fa-download"></i>
        <span data-en="CV" data-ar="السيرة">CV</span>
    </a>

    <!-- ============ SCRIPTS ============ -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="scripts/main.js"></script>
    <script src="scripts/animations.js"></script>
    <script src="scripts/map.js"></script>

</body>
</html>"""

# Write the HTML file
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Written {len(html):,} bytes to {output_path}")
print("Done!")
