import os

base_dir = r"c:\Users\civil\Downloads\eng mostafa profile"

def get_nav_html(active_page="home"):
    links = [
        {"id": "home", "href": "index.html", "en": "Home", "ar": "الرئيسية"},
        {"id": "projects", "href": "projects.html", "en": "Projects", "ar": "المشاريع"},
        {"id": "services", "href": "services.html", "en": "Services", "ar": "الخدمات"},
        {"id": "software", "href": "software.html", "en": "Software", "ar": "البرامج"},
        {"id": "about", "href": "about.html", "en": "About", "ar": "نبذة عني"},
        {"id": "experience", "href": "experience.html", "en": "Experience", "ar": "الخبرات"},
        {"id": "certificates", "href": "certificates.html", "en": "Certificates", "ar": "الشهادات"},
        {"id": "contact", "href": "contact.html", "en": "Contact", "ar": "تواصل"},
    ]
    
    links_html = ""
    for l in links:
        active_cls = " active" if l["id"] == active_page else ""
        links_html += f'<a class="nav-pill-link{active_cls}" href="{l["href"]}" data-en="{l["en"]}" data-ar="{l["ar"]}">{l["en"]}</a>\n'
    
    return f"""
    <header class="navbar-floating-header">
      <div class="navbar-inner-box">
        <a class="nav-brand-logo" href="index.html">
          <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--accent);"></span>
          <span data-en="Eng. Mostafa" data-ar="م. مصطفى عبد الغني">Eng. Mostafa</span>
        </a>

        <nav class="nav-pill-menu" id="nav-menu">
          {links_html}
        </nav>

        <div class="nav-controls-box">
          <button class="nav-pill-btn" id="lang-toggle" title="Switch Language">
            <span id="lang-text">AR</span>
          </button>
          <button class="nav-pill-btn" id="theme-toggle" title="Toggle Theme" aria-label="Toggle Theme">
            <i class="fas fa-moon"></i>
          </button>
          <a class="nav-cta-pill" href="contact.html" data-en="Hire Me" data-ar="تعاقد معي">Hire Me</a>
          <button class="hamburger-btn" id="hamburger-btn" aria-label="Menu">
            <i class="fas fa-bars"></i>
          </button>
        </div>
      </div>
    </header>
    """

def get_footer_html():
    return """
    <footer class="footer-high-end">
      <div class="container">
        <div class="footer-grid-top">
          <div>
            <h3 class="font-display" style="font-size:1.4rem;font-weight:600;color:var(--ink);margin-bottom:8px;">Eng. Mostafa Abdelghany</h3>
            <p style="color:var(--ink-dim);font-size:0.92rem;max-width:380px;line-height:1.7;" data-en="MEP Procurement Section Head & Engineering Consultant. Translating complex engineering specifications into optimized procurement packages." data-ar="رئيس قسم مشتريات الكهروميكانيك (MEP) واستشاري هندسي. تحويل المواصفات الهندسية المعقدة إلى حزم شراء ومناقصات محسوبة بأعلى كفاءة.">MEP Procurement Section Head & Engineering Consultant. Translating complex engineering specifications into optimized procurement packages.</p>
          </div>
          <div>
            <div class="footer-col-title" data-en="Reach" data-ar="تواصل مباشر">Reach</div>
            <div class="footer-link-list">
              <a class="footer-link-item" href="mailto:engmostafamahoud2012@gmail.com"><i class="fas fa-envelope gold-text"></i> engmostafamahoud2012@gmail.com</a>
              <a class="footer-link-item" href="tel:+966502582122"><i class="fas fa-phone gold-text"></i> +966 502 582 122</a>
              <a class="footer-link-item" href="https://wa.me/966502582122" target="_blank"><i class="fab fa-whatsapp gold-text"></i> WhatsApp Direct</a>
              <a class="footer-link-item" href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank"><i class="fab fa-linkedin gold-text"></i> LinkedIn Profile</a>
            </div>
          </div>
          <div>
            <div class="footer-col-title" data-en="Navigation" data-ar="أقسام الموقع">Navigation</div>
            <div class="footer-link-list">
              <a class="footer-link-item" href="projects.html" data-en="Projects Directory" data-ar="دليل المشاريع">Projects Directory</a>
              <a class="footer-link-item" href="services.html" data-en="Freelance & Consulting" data-ar="الخدمات والفريلانس">Freelance & Consulting</a>
              <a class="footer-link-item" href="software.html" data-en="Software Stack" data-ar="البرمجيات">Software Stack</a>
              <a class="footer-link-item" href="certificates.html" data-en="Credentials & SCE" data-ar="الاعتمادات والشهادات">Credentials & SCE</a>
            </div>
          </div>
        </div>
        <div class="footer-bottom-bar">
          <div>© 2026 ENG. MOSTAFA ABDELGHANY — ALL RIGHTS RESERVED</div>
          <div>RIYADH, SAUDI ARABIA · SCE #1084929</div>
        </div>
      </div>
    </footer>
    """

def get_page_head(title_en, title_ar, active_page="home"):
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title data-en="{title_en}" data-ar="{title_ar}">{title_en}</title>
  <meta name="description" content="Eng. Mostafa Abdelghany - MEP Procurement Section Head | Portfolio & Engineering Hub" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <link rel="stylesheet" href="styles/main.css" />
  <link rel="stylesheet" href="styles/pages.css" />
  <link rel="stylesheet" href="styles/animations.css" />
  <link rel="stylesheet" href="styles/responsive.css" />
</head>
<body>
  <div class="grain-overlay"></div>
  <div id="scroll-progress"></div>
  {get_nav_html(active_page)}
"""

def get_page_tail(extra_scripts=""):
    return f"""
  {get_footer_html()}
  <a class="cv-float-btn" id="cv-float-btn" href="Mostafa Abdelghany - Procurement CV.pdf" target="_blank" title="Download CV">
    <i class="fas fa-file-pdf" style="font-size:16px;"></i>
    <span>CV</span>
  </a>
  <script src="scripts/projects-data.js"></script>
  <script src="scripts/animations.js"></script>
  <script src="scripts/main.js"></script>
  {extra_scripts}
</body>
</html>
"""

# -------------------------------------------------------------
# 1. INDEX.HTML (HOME)
# -------------------------------------------------------------
def build_index():
    head = get_page_head("Eng. Mostafa Abdelghany | MEP Procurement Section Head", "م. مصطفى عبد الغني | رئيس قسم مشتريات الكهروميكانيك", "home")
    body = """
  <!-- HERO SECTION -->
  <section class="hero-architect-section">
    <div class="hero-backdrop-img">
      <img src="assets/images/kaig_hero_bg.jpg" alt="King Abdullah International Gardens Mega Project" />
      <div class="hero-scrim-gradient"></div>
    </div>

    <div class="hero-main-container">
      <span class="label gold-text" data-en="Executive Engineering & Procurement" data-ar="إدارة مشتريات وهندسة الكهروميكانيك">Executive Engineering & Procurement</span>
      <h1 class="hero-display-headline" data-en="Eng. Mostafa Abdelghany" data-ar="م. مصطفى عبد الغني">Eng. Mostafa Abdelghany</h1>
      <p class="hero-lead-paragraph" data-en="MEP Procurement Section Head at Zaid Al Hussain Group. Managing mega-scale tenders, value engineering, and high-stakes procurement packages across KSA & Egypt." data-ar="رئيس قسم مشتريات الكهروميكانيك (MEP) بمجموعة زيد الحسين. إدارة المناقصات الكبرى، هندسة القيمة، وسلاسل الإمداد للمشاريع المليارية في المملكة ومصر.">MEP Procurement Section Head at Zaid Al Hussain Group. Managing mega-scale tenders, value engineering, and high-stakes procurement packages across KSA & Egypt.</p>
      
      <div class="hero-actions-row">
        <a class="btn-pill-primary" href="projects.html" data-en="View Projects" data-ar="استعراض المشاريع">View Projects</a>
        <a class="btn-pill-outline" href="services.html" data-en="Consulting & Freelance" data-ar="الخدمات والاستشارات">Consulting & Freelance</a>
      </div>
    </div>

    <!-- Spotlight Floating Glass Card -->
    <div class="spotlight-glass-card">
      <div class="spotlight-row">
        <span class="label" data-en="Role" data-ar="المنصب">Role</span>
        <span class="spotlight-val" data-en="MEP Procurement Head" data-ar="رئيس قسم المشتريات">MEP Procurement Head</span>
      </div>
      <div class="spotlight-row">
        <span class="label" data-en="Location" data-ar="المقر">Location</span>
        <span class="spotlight-val" data-en="Riyadh, Saudi Arabia" data-ar="الرياض، السعودية">Riyadh, Saudi Arabia</span>
      </div>
      <div class="spotlight-row">
        <span class="label" data-en="Experience" data-ar="الخبرة">Experience</span>
        <span class="spotlight-val" data-en="9+ Years (2016-2026)" data-ar="+9 سنوات (2016-2026)">9+ Years (2016-2026)</span>
      </div>
      <div class="spotlight-row">
        <span class="label" data-en="Flagship" data-ar="المشروع الأكبر">Flagship</span>
        <span class="spotlight-val gold-text" data-en="KAIG · SAR 2.63 Billion" data-ar="حدائق الملك عبدالله · 2.63 مليار">KAIG · SAR 2.63B</span>
      </div>
    </div>
  </section>

  <!-- STATS DIVIDER SECTION -->
  <section class="section-wrapper" style="padding:0;">
    <div class="container">
      <div class="stats-divider-grid">
        <div class="stat-cell">
          <div class="stat-big-number">14</div>
          <div class="stat-mono-label" data-en="Mega Projects" data-ar="مشاريع كبرى موثقة">Mega Projects</div>
        </div>
        <div class="stat-cell">
          <div class="stat-big-number">9+</div>
          <div class="stat-mono-label" data-en="Years Experience" data-ar="سنوات خبرة متقدمة">Years Experience</div>
        </div>
        <div class="stat-cell">
          <div class="stat-big-number">5</div>
          <div class="stat-mono-label" data-en="Industry Giants" data-ar="كبريات شركات المقاولات">Industry Giants</div>
        </div>
        <div class="stat-cell">
          <div class="stat-big-number" style="font-size: clamp(2rem, 3.2vw, 3.2rem);">2.63B</div>
          <div class="stat-mono-label" data-en="SAR Flagship Tender" data-ar="ريال قيمة أكبر مشروع (حدائق الملك عبدالله)">SAR Flagship Tender</div>
        </div>
      </div>
    </div>
  </section>

  <!-- INFINITE TOOLS MARQUEE -->
  <div class="marquee-wrapper">
    <div class="marquee-mask-left"></div>
    <div class="marquee-mask-right"></div>
    <div class="marquee-track">
      <span class="marquee-item">Primavera P6</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">AutoCAD MEP</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">Revit & BIM Coordination</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">Oracle ERP</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">SAP MM</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">Value Engineering</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">FIDIC Contract Negotiation</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">BOQ Preparation</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">HVAC & Firefighting Procurement</span>
      <span class="marquee-item">✦</span>
      <!-- Duplicate for seamless loop -->
      <span class="marquee-item">Primavera P6</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">AutoCAD MEP</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">Revit & BIM Coordination</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">Oracle ERP</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">SAP MM</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">Value Engineering</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">FIDIC Contract Negotiation</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">BOQ Preparation</span>
      <span class="marquee-item">✦</span>
      <span class="marquee-item">HVAC & Firefighting Procurement</span>
      <span class="marquee-item">✦</span>
    </div>
  </div>

  <!-- SELECTED PROJECTS EDITORIAL SECTION -->
  <section class="section-wrapper">
    <div class="container">
      <div class="section-heading-block" style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:20px;">
        <div>
          <span class="label" data-en="Selected Portfolio" data-ar="مختارات من أعمالي">Selected Portfolio</span>
          <h2 class="section-heading-title" data-en="Key Construction & MEP Projects" data-ar="أبرز مشاريع الكهروميكانيك والمقاولات">Key Construction & MEP Projects</h2>
        </div>
        <a class="btn-pill-outline" href="projects.html" data-en="View All 14 Projects" data-ar="استعراض كافة الـ 14 مشروعاً">View All 14 Projects</a>
      </div>

      <div class="editorial-projects-grid">
        <!-- Flagship 21:9 Card: KAIG -->
        <a class="editorial-project-card editorial-card-flagship" href="project-detail.html?id=kaig">
          <div class="editorial-img-box">
            <img src="assets/images/projects/kaig_6.jpg" alt="King Abdullah International Gardens (KAIG)" />
            <div class="editorial-card-scrim"></div>
          </div>
          <div class="editorial-card-content">
            <span class="label" style="color:var(--accent);" data-en="Zaid Al Hussain Group · SAR 2.63 Billion" data-ar="مجموعة زيد الحسين · 2.63 مليار ريال">Zaid Al Hussain Group · SAR 2.63 Billion</span>
            <h3 class="editorial-card-title" data-en="King Abdullah International Gardens (KAIG)" data-ar="مشروع حدائق الملك عبدالله العالمية">King Abdullah International Gardens (KAIG)</h3>
            <span class="editorial-card-location" data-en="Riyadh, Saudi Arabia · Mega Botanical Domes & MEP Infrastructure" data-ar="الرياض، المملكة العربية السعودية · البنية التحتية والقباب النباتية العملاقة">Riyadh, Saudi Arabia · Mega Botanical Domes & MEP Infrastructure</span>
          </div>
        </a>

        <!-- 2-Col Card 1: Noor City -->
        <a class="editorial-project-card editorial-card-standard" href="project-detail.html?id=noor-city">
          <div class="editorial-img-box">
            <img src="assets/images/projects/noor_city_1.jpg" alt="Noor City New Capital" />
            <div class="editorial-card-scrim"></div>
          </div>
          <div class="editorial-card-content">
            <span class="label" data-en="Atrium Quality Contractors · TMG" data-ar="شركة أتريوم للمقاولات · طلعت مصطفى">Atrium Quality Contractors · TMG</span>
            <h3 class="editorial-card-title" data-en="Noor City Integrated Megacity" data-ar="مدينة نور الذكية المتكاملة">Noor City Integrated Megacity</h3>
            <span class="editorial-card-location" data-en="New Administrative Capital, Egypt" data-ar="العاصمة الإدارية الجديدة، مصر">New Administrative Capital, Egypt</span>
          </div>
        </a>

        <!-- 2-Col Card 2: Aeon Towers -->
        <a class="editorial-project-card editorial-card-standard" href="project-detail.html?id=aeon-towers">
          <div class="editorial-img-box">
            <img src="assets/images/projects/aeon_towers_1.jpeg" alt="Aeon Towers" />
            <div class="editorial-card-scrim"></div>
          </div>
          <div class="editorial-card-content">
            <span class="label" data-en="Hassan Allam Construction · Marakez" data-ar="حسن علام للإنشاءات · مراكز">Hassan Allam Construction · Marakez</span>
            <h3 class="editorial-card-title" data-en="Aeon Towers (3x High-Rise 72m)" data-ar="أبراج إيون السكنية الشاهقة">Aeon Towers (3x High-Rise 72m)</h3>
            <span class="editorial-card-location" data-en="6th of October City, Egypt" data-ar="مدينة السادس من أكتوبر، مصر">6th of October City, Egypt</span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- FREELANCE DIRECT BANNER -->
  <section class="section-wrapper" style="border-bottom:none;">
    <div class="container">
      <div class="freelance-direct-banner">
        <div>
          <span class="label gold-text" data-en="Freelance & Project Tenders" data-ar="الاستشارات والتعاقدات الحرة">Freelance & Project Tenders</span>
          <h2 class="font-display" style="font-size:clamp(1.8rem,3vw,2.6rem);font-weight:600;color:var(--ink);margin:10px 0;" data-en="Need MEP Procurement or Tender Consultation?" data-ar="هل تحتاج استشارة في مشتريات MEP أو تسعير المناقصات؟">Need MEP Procurement or Tender Consultation?</h2>
          <p style="color:var(--ink-dim);font-size:0.95rem;max-width:550px;" data-en="Available for high-stakes procurement packages, value engineering audits, subcontractor negotiation, and BOQ preparation." data-ar="متاح لتقديم استشارات متخصصة للمقاولين والمطورين في تسعير حزم الكهروميكانيك، هندسة القيمة، وإعداد جداول الكميات.">Available for high-stakes procurement packages, value engineering audits, subcontractor negotiation, and BOQ preparation.</p>
        </div>
        <a class="btn-pill-primary" href="https://wa.me/966502582122?text=Hello%20Eng.%20Mostafa,%20I%20would%20like%20to%20consult%20you%20regarding%20an%20MEP%20procurement%20package." target="_blank">
          <i class="fab fa-whatsapp" style="font-size:16px;"></i>
          <span data-en="Inquire on WhatsApp" data-ar="استشارة فورية عبر واتساب">Inquire on WhatsApp</span>
        </a>
      </div>
    </div>
  </section>
"""
    return head + body + get_page_tail()

# -------------------------------------------------------------
# 2. ABOUT.HTML
# -------------------------------------------------------------
def build_about():
    head = get_page_head("About | Eng. Mostafa Abdelghany", "نبذة عني | م. مصطفى عبد الغني", "about")
    body = """
  <header class="page-intro-header">
    <div class="container">
      <span class="page-intro-tag" data-en="Professional Background" data-ar="السيرة المهنية والخبرات">Professional Background</span>
      <h1 class="page-intro-title" data-en="About & Engineering Philosophy" data-ar="نبذة عني وفلسفة العمل الهندسي">About & Engineering Philosophy</h1>
      <p class="page-intro-subtitle" data-en="B.Sc. Mechanical Power Engineer with over 9 years of specialized experience in mega-construction and MEP procurement." data-ar="مهندس ميكانيكا قوى معتمد بأكثر من 9 سنوات من الخبرة المتخصصة في كبرى مشاريع الإنشاءات والمشتريات الهندسية.">B.Sc. Mechanical Power Engineer with over 9 years of specialized experience in mega-construction and MEP procurement.</p>
    </div>
  </header>

  <section class="section-wrapper">
    <div class="container">
      <div class="about-architect-grid">
        <!-- Portrait Box -->
        <div>
          <div class="portrait-frame-box">
            <img src="assets/images/headshot.jpg" alt="Eng. Mostafa Abdelghany" />
            <div class="portrait-gold-tag">
              <i class="fas fa-certificate" style="margin-right:6px;"></i> SCE Registered #1084929
            </div>
          </div>
        </div>

        <!-- Bio & Philosophy -->
        <div>
          <h2 class="font-display" style="font-size:2.2rem;font-weight:600;color:var(--ink);margin-bottom:18px;" data-en="Turning Procurement into a Strategic Profit Center" data-ar="تحويل المشتريات إلى مركز قوة وربحية استراتيجية للمشاريع">Turning Procurement into a Strategic Profit Center</h2>
          <p class="about-bio-text" data-en="With 9+ years navigating multi-billion SAR/EGP infrastructure and building projects across Saudi Arabia and Egypt, I lead MEP procurement with an engineer's technical rigor and a financial strategist's cost acumen." data-ar="بخبرة تزيد عن 9 سنوات في إدارة مشاريع البنية التحتية والمباني المليارية في السعودية ومصر، أقود قطاع المشتريات الهندسية بدقة هندسية بالغة ورؤية مالية واستراتيجية تحقق أعلى وفر وجودة.">With 9+ years navigating multi-billion SAR/EGP infrastructure and building projects across Saudi Arabia and Egypt, I lead MEP procurement with an engineer's technical rigor and a financial strategist's cost acumen.</p>
          <p class="about-bio-text" data-en="Currently serving as MEP Procurement Section Head at Zaid Al Hussain Group in Riyadh, I spearhead major subcontracts, material approvals, FIDIC contract administration, and value engineering initiatives for landmark projects like the King Abdullah International Gardens (SAR 2.63B)." data-ar="أشغل حالياً منصب رئيس قسم مشتريات الكهروميكانيك بمجموعة زيد الحسين بالرياض، حيث أقود عقود الباطن الرئيسية، اعتمادات المواد، إدارة عقود الفيديك، وهندسة القيمة لمشاريع عملاقة على رأسها حدائق الملك عبدالله العالمية (2.63 مليار ريال).">Currently serving as MEP Procurement Section Head at Zaid Al Hussain Group in Riyadh, I spearhead major subcontracts, material approvals, FIDIC contract administration, and value engineering initiatives for landmark projects like the King Abdullah International Gardens (SAR 2.63B).</p>

          <div class="philosophy-callout-card">
            <div class="philosophy-quote" data-en="&ldquo;Procurement in mega-projects isn't merely buying equipment; it is engineering the commercial backbone that guarantees timely execution, technical compliance, and substantial margin optimization.&rdquo;" data-ar="&ldquo;المشتريات في المشاريع الكبرى ليست مجرد شراء معدات؛ بل هي هندسة العمود الفقري التجاري الذي يضمن الالتزام الزمني، المطابقة الفنية الصارمة، وتحقيق أعلى هوامش ربحية.&rdquo;">&ldquo;Procurement in mega-projects isn't merely buying equipment; it is engineering the commercial backbone that guarantees timely execution, technical compliance, and substantial margin optimization.&rdquo;</div>
          </div>

          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:30px;">
            <div style="background:var(--bg-elevated);border:1px solid var(--line);border-radius:var(--radius-md);padding:20px;">
              <span class="label" data-en="Education" data-ar="المؤهل العلمي">Education</span>
              <h4 style="font-size:1rem;color:var(--ink);margin-top:6px;" data-en="B.Sc. Mechanical Power Engineering" data-ar="بكالوريوس هندسة القوى الميكانيكية">B.Sc. Mechanical Power Engineering</h4>
              <span style="font-size:0.85rem;color:var(--ink-dim);" data-en="Benha University (2010 - 2015)" data-ar="جامعة بنها (2010 - 2015)">Benha University (2010 - 2015)</span>
            </div>
            <div style="background:var(--bg-elevated);border:1px solid var(--line);border-radius:var(--radius-md);padding:20px;">
              <span class="label" data-en="Accreditation" data-ar="الاعتماد المهني">Accreditation</span>
              <h4 style="font-size:1rem;color:var(--ink);margin-top:6px;" data-en="Saudi Council of Engineers (SCE)" data-ar="الهيئة السعودية للمهندسين">Saudi Council of Engineers (SCE)</h4>
              <span style="font-size:0.85rem;color:var(--ink-dim);" data-en="Professional Member #1084929" data-ar="عضوية مهنية #1084929">Professional Member #1084929</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    return head + body + get_page_tail()

# -------------------------------------------------------------
# 3. SERVICES.HTML
# -------------------------------------------------------------
def build_services():
    head = get_page_head("Services & Freelance Consulting | Eng. Mostafa Abdelghany", "الخدمات واستشارات الفريلانس | م. مصطفى عبد الغني", "services")
    body = """
  <header class="page-intro-header">
    <div class="container">
      <span class="page-intro-tag" data-en="Capabilities & Consulting" data-ar="الخدمات والاستشارات الفنية">Capabilities & Consulting</span>
      <h1 class="page-intro-title" data-en="MEP Procurement & Tender Advisory" data-ar="خدمات مشتريات MEP واستشارات المناقصات">MEP Procurement & Tender Advisory</h1>
      <p class="page-intro-subtitle" data-en="Comprehensive procurement engineering, cost optimization, contract negotiation, and freelance advisory for contracting firms and developers." data-ar="حزم خدمات شاملة في هندسة المشتريات، دراسة التكاليف، صياغة العقود، واستشارات الفريلانس لكبرى شركات التطوير والمقاولات.">Comprehensive procurement engineering, cost optimization, contract negotiation, and freelance advisory for contracting firms and developers.</p>
    </div>
  </header>

  <section class="section-wrapper">
    <div class="container">
      <div class="services-editorial-grid">
        <!-- Service 1 -->
        <div class="service-dark-card">
          <div>
            <div class="service-icon-box"><i class="fas fa-coins"></i></div>
            <h3 class="service-card-title" data-en="Value Engineering & Cost Optimization" data-ar="هندسة القيمة وتحسين التكاليف">Value Engineering & Cost Optimization</h3>
            <p class="service-card-desc" data-en="Systematic technical reviews of MEP systems to identify cost-saving alternatives without compromising specifications, performance, or consultant approvals." data-ar="مراجعة فنية شاملة لمنظومات MEP لتقديم بدائل فنية معتمدة توفر ملايين الريالات دون المساس بالجودة أو موافقة الاستشاري.">Systematic technical reviews of MEP systems to identify cost-saving alternatives without compromising specifications, performance, or consultant approvals.</p>
          </div>
          <div class="service-deliverables-list">
            <span class="service-deliverable-item" data-en="Alternative vendor technical comparisons" data-ar="مقارنات فنية ومالية للبدائل">Alternative vendor technical comparisons</span>
            <span class="service-deliverable-item" data-en="Lifecycle cost analysis" data-ar="تحليل تكلفة دورة الحياة">Lifecycle cost analysis</span>
            <span class="service-deliverable-item" data-en="Consultant approval submittal support" data-ar="إعداد مذكرات الاعتماد للاستشاري">Consultant approval submittal support</span>
          </div>
        </div>

        <!-- Service 2 -->
        <div class="service-dark-card">
          <div>
            <div class="service-icon-box"><i class="fas fa-file-signature"></i></div>
            <h3 class="service-card-title" data-en="Subcontract Negotiation & FIDIC" data-ar="صياغة وتفاوض عقود الباطن وفيديك">Subcontract Negotiation & FIDIC</h3>
            <p class="service-card-desc" data-en="Drafting robust subcontract agreements, back-to-back risk alignment with main contract conditions, and strategic commercial negotiations." data-ar="صياغة عقود باطن محكمة متوافقة مع شروط العقد الرئيسي والفيديك، وإدارة جلسات التفاوض المالي والفني بحرفية.">Drafting robust subcontract agreements, back-to-back risk alignment with main contract conditions, and strategic commercial negotiations.</p>
          </div>
          <div class="service-deliverables-list">
            <span class="service-deliverable-item" data-en="Back-to-back risk mitigation terms" data-ar="بنود حماية وحوكمة المخاطر">Back-to-back risk mitigation terms</span>
            <span class="service-deliverable-item" data-en="Scope gap matrix prevention" data-ar="منع ثغرات وتداخل نطاق الأعمال">Scope gap matrix prevention</span>
            <span class="service-deliverable-item" data-en="Payment milestones & retention clauses" data-ar="صياغة الدفعات النقدية والضمانات">Payment milestones & retention clauses</span>
          </div>
        </div>

        <!-- Service 3 -->
        <div class="service-dark-card">
          <div>
            <div class="service-icon-box"><i class="fas fa-boxes-stacked"></i></div>
            <h3 class="service-card-title" data-en="Tender Pricing & BOQ Estimation" data-ar="تسعير العطاءات وإعداد جداول الكميات">Tender Pricing & BOQ Estimation</h3>
            <p class="service-card-desc" data-en="Accurate quantity takeoff, RFQ management, supplier quotation evaluations, and tender package preparation for major MEP bids." data-ar="حصر كميات دقيق، إدارة طلبات عروض الأسعار RFQ، تحليل العروض، وإعداد مظاريف المناقصات التنافسية.">Accurate quantity takeoff, RFQ management, supplier quotation evaluations, and tender package preparation for major MEP bids.</p>
          </div>
          <div class="service-deliverables-list">
            <span class="service-deliverable-item" data-en="Detailed MEP BOQ takeoff" data-ar="حصر تفصيلي لمخططات الـ MEP">Detailed MEP BOQ takeoff</span>
            <span class="service-deliverable-item" data-en="Commercial bid leveling sheets" data-ar="جداول مقارنة وتفريغ الأسعار">Commercial bid leveling sheets</span>
            <span class="service-deliverable-item" data-en="Procurement schedule aligned with P6" data-ar="جدول زمني للمشتريات متوافق مع P6">Procurement schedule aligned with P6</span>
          </div>
        </div>

        <!-- Service 4 -->
        <div class="service-dark-card">
          <div>
            <div class="service-icon-box"><i class="fas fa-globe-americas"></i></div>
            <h3 class="service-card-title" data-en="Global Supply Chain & Vendor Sourcing" data-ar="سلاسل الإمداد وتأهيل الموردين الدوليين">Global Supply Chain & Vendor Sourcing</h3>
            <p class="service-card-desc" data-en="Establishing direct factory channels across Europe, Gulf, and Asia for chillers, fire pumps, transformers, and specialized MEP systems." data-ar="بناء قنوات استيراد وتوريد مباشرة مع المصانع العالمية في أوروبا والخليج وآسيا للمعدات الكبرى ومحطات التبريد.">Establishing direct factory channels across Europe, Gulf, and Asia for chillers, fire pumps, transformers, and specialized MEP systems.</p>
          </div>
          <div class="service-deliverables-list">
            <span class="service-deliverable-item" data-en="Approved vendor list (AVL) auditing" data-ar="تدقيق سجل الموردين المعتمدين">Approved vendor list (AVL) auditing</span>
            <span class="service-deliverable-item" data-en="International logistics & LC terms" data-ar="الاعتمادات المستندية والشحن الدولي">International logistics & LC terms</span>
            <span class="service-deliverable-item" data-en="Factory acceptance testing (FAT) protocol" data-ar="بروتوكولات فحص المصنع FAT">Factory acceptance testing (FAT) protocol</span>
          </div>
        </div>

        <!-- Service 5 -->
        <div class="service-dark-card">
          <div>
            <div class="service-icon-box"><i class="fas fa-handshake"></i></div>
            <h3 class="service-card-title" data-en="Freelance MEP Package Management" data-ar="إدارة حزم مشتريات MEP بنظام الفريلانس">Freelance MEP Package Management</h3>
            <p class="service-card-desc" data-en="End-to-end remote or hybrid handling of specific procurement packages (HVAC, Electrical, Plumbing, Firefighting) for fast-track projects." data-ar="إدارة متكاملة لحزم شراء محددة (تكييف، كهرباء، صحي، حريق) عن بعد أو هجين للمشاريع السريعة.">End-to-end remote or hybrid handling of specific procurement packages (HVAC, Electrical, Plumbing, Firefighting) for fast-track projects.</p>
          </div>
          <div class="service-deliverables-list">
            <span class="service-deliverable-item" data-en="Fast turnaround package delivery" data-ar="تسليم سريع ومحكم للحزمة">Fast turnaround package delivery</span>
            <span class="service-deliverable-item" data-en="Direct supplier negotiation representation" data-ar="تمثيل المالك/المقاول أمام الموردين">Direct supplier negotiation representation</span>
            <span class="service-deliverable-item" data-en="Weekly procurement status tracking" data-ar="تقارير متابعة أسبوعية دقيقة">Weekly procurement status tracking</span>
          </div>
        </div>

        <!-- Service 6 -->
        <div class="service-dark-card">
          <div>
            <div class="service-icon-box"><i class="fas fa-laptop-code"></i></div>
            <h3 class="service-card-title" data-en="ERP & Procurement System Setup" data-ar="هيكلة أنظمة المشتريات و ERP">ERP & Procurement System Setup</h3>
            <p class="service-card-desc" data-en="Configuring Oracle ERP & SAP MM procurement workflows, standardizing RFQ templates, and establishing procurement governance." data-ar="إعداد دورات المشتريات على أوراكل وساب، توحيد نماذج عروض الأسعار، وضبط حوكمة واعتمادات الشراء.">Configuring Oracle ERP & SAP MM procurement workflows, standardizing RFQ templates, and establishing procurement governance.</p>
          </div>
          <div class="service-deliverables-list">
            <span class="service-deliverable-item" data-en="Procurement approval matrix design" data-ar="مصفوفة صلاحيات واعتمادات الشراء">Procurement approval matrix design</span>
            <span class="service-deliverable-item" data-en="ERP item catalog coding standards" data-ar="أكواد وتصنيفات الأصناف الهندسية">ERP item catalog coding standards</span>
            <span class="service-deliverable-item" data-en="Procurement KPI dashboard setup" data-ar="لوحات مؤشرات الأداء KPIs">Procurement KPI dashboard setup</span>
          </div>
        </div>
      </div>

      <!-- Pricing Models -->
      <div style="margin-top:80px;">
        <span class="label gold-text" data-en="Engagement Options" data-ar="خيارات ونماذج التعاقد">Engagement Options</span>
        <h2 class="section-heading-title" data-en="Flexible Consulting Models" data-ar="نماذج تعاقد مرنة تناسب مشروعك">Flexible Consulting Models</h2>

        <div class="pricing-models-grid">
          <div class="pricing-plan-card">
            <h3 class="font-display" style="font-size:1.4rem;color:var(--ink);margin-bottom:8px;" data-en="Advisory & Review" data-ar="الاستشارة والمراجعة الفنية">Advisory & Review</h3>
            <p style="color:var(--ink-dim);font-size:0.88rem;margin-bottom:20px;" data-en="Per-hour or per-session consultation on specific tenders, vendor claims, or procurement disputes." data-ar="جلسات استشارية بالساعة لدراسة عروض أسعار محددة أو مراجعة مطالبات الموردين.">Per-hour or per-session consultation on specific tenders, vendor claims, or procurement disputes.</p>
            <div style="border-top:1px solid var(--line);padding-top:20px;">
              <a class="btn-pill-outline" style="width:100%;justify-content:center;" href="https://wa.me/966502582122?text=Hello%20Eng.%20Mostafa,%20I%20am%20interested%20in%20an%20Advisory%20Session." target="_blank" data-en="Book Advisory" data-ar="حجز جلسة استشارية">Book Advisory</a>
            </div>
          </div>

          <div class="pricing-plan-card featured">
            <div class="pricing-plan-tag" data-en="Most Popular" data-ar="الأكثر طلباً">Most Popular</div>
            <h3 class="font-display" style="font-size:1.4rem;color:var(--ink);margin-bottom:8px;" data-en="Package Deliverable" data-ar="تسليم الحزمة بالمشروع">Package Deliverable</h3>
            <p style="color:var(--ink-dim);font-size:0.88rem;margin-bottom:20px;" data-en="Complete delivery of a defined MEP package: RFQ, leveling, negotiation, and draft contract agreement." data-ar="تولي حزمة شراء محددة بالكامل من طرح الأسعار والتفاوض وحتى صياغة أمر الشراء أو العقد.">Complete delivery of a defined MEP package: RFQ, leveling, negotiation, and draft contract agreement.</p>
            <div style="border-top:1px solid var(--line);padding-top:20px;">
              <a class="btn-pill-primary" style="width:100%;justify-content:center;" href="https://wa.me/966502582122?text=Hello%20Eng.%20Mostafa,%20I%20have%20an%20MEP%20Package%20for%20consulting." target="_blank" data-en="Request Proposal" data-ar="طلب عرض تسعير حزمة">Request Proposal</a>
            </div>
          </div>

          <div class="pricing-plan-card">
            <h3 class="font-display" style="font-size:1.4rem;color:var(--ink);margin-bottom:8px;" data-en="Retained Procurement Lead" data-ar="إدارة مشتريات شهرية">Retained Procurement Lead</h3>
            <p style="color:var(--ink-dim);font-size:0.88rem;margin-bottom:20px;" data-en="Ongoing fractional leadership managing all procurement operations for medium-to-large contractors." data-ar="قيادة قسم المشتريات شهرياً للمقاولين مع حضور اجتماعات التفاوض الكبرى وإدارة الموردين.">Ongoing fractional leadership managing all procurement operations for medium-to-large contractors.</p>
            <div style="border-top:1px solid var(--line);padding-top:20px;">
              <a class="btn-pill-outline" style="width:100%;justify-content:center;" href="https://wa.me/966502582122?text=Hello%20Eng.%20Mostafa,%20I%20would%20like%20to%20discuss%20a%20Retained%20Procurement%20Role." target="_blank" data-en="Discuss Retainer" data-ar="مناقشة التعاقد الشهري">Discuss Retainer</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    return head + body + get_page_tail()

# -------------------------------------------------------------
# 4. SOFTWARE.HTML
# -------------------------------------------------------------
def build_software():
    head = get_page_head("Software & Tools Stack | Eng. Mostafa Abdelghany", "البرامج والأدوات الهندسية | م. مصطفى عبد الغني", "software")
    body = """
  <header class="page-intro-header">
    <div class="container">
      <span class="page-intro-tag" data-en="Technical Competencies" data-ar="الكفاءات البرمجية والهندسية">Technical Competencies</span>
      <h1 class="page-intro-title" data-en="Engineering & Enterprise Software Stack" data-ar="البرمجيات الهندسية والأنظمة المؤسسية">Engineering & Enterprise Software Stack</h1>
      <p class="page-intro-subtitle" data-en="Advanced mastery of construction scheduling, BIM coordination, ERP enterprise resource planning, and financial modeling tools." data-ar="إتقان متقدم لبرمجيات الجدولة الزمنية، التنسيق الهندسي BIM، أنظمة ERP العالمية، ونماذج التحليل المالي.">Advanced mastery of construction scheduling, BIM coordination, ERP enterprise resource planning, and financial modeling tools.</p>
    </div>
  </header>

  <section class="section-wrapper">
    <div class="container">
      <div class="software-dark-grid">
        <!-- Tool 1: Primavera P6 -->
        <div class="software-tool-card">
          <div class="software-card-top">
            <h3 class="software-tool-name">Primavera P6</h3>
            <span class="software-tool-score">95% Mastery</span>
          </div>
          <div class="software-gauge-bar"><div class="software-gauge-fill" style="width:95%;"></div></div>
          <p style="color:var(--ink-dim);font-size:0.9rem;line-height:1.6;" data-en="Procurement scheduling, critical path analysis, lead time tracking for long-lead MEP equipment, and baseline integration." data-ar="جدولة المشتريات، ربط مسار التوريد بالمسار الحرج للمشروع، ومتابعة مدة تصنيع وتوريد المعدات الرئيسية.">Procurement scheduling, critical path analysis, lead time tracking for long-lead MEP equipment, and baseline integration.</p>
        </div>

        <!-- Tool 2: AutoCAD MEP -->
        <div class="software-tool-card">
          <div class="software-card-top">
            <h3 class="software-tool-name">AutoCAD MEP</h3>
            <span class="software-tool-score">95% Mastery</span>
          </div>
          <div class="software-gauge-bar"><div class="software-gauge-fill" style="width:95%;"></div></div>
          <p style="color:var(--ink-dim);font-size:0.9rem;line-height:1.6;" data-en="Shop drawing audits, quantity takeoff, ductwork/piping routing reviews, and as-built verification for submittals." data-ar="مراجعة الرسومات التنفيذية، حصر الكميات الهندسي، تدقيق مسارات الدكت والمواسير، ومطابقة المخططات المحدثة.">Shop drawing audits, quantity takeoff, ductwork/piping routing reviews, and as-built verification for submittals.</p>
        </div>

        <!-- Tool 3: Revit & BIM -->
        <div class="software-tool-card">
          <div class="software-card-top">
            <h3 class="software-tool-name">Revit & BIM Coordination</h3>
            <span class="software-tool-score">88% Mastery</span>
          </div>
          <div class="software-gauge-bar"><div class="software-gauge-fill" style="width:88%;"></div></div>
          <p style="color:var(--ink-dim);font-size:0.9rem;line-height:1.6;" data-en="Navigating 3D multidisciplinary models, clash detection resolution with structural/architectural, and automated material schedules." data-ar="التنقل وفحص النماذج ثلاثية الأبعاد، حل التعارضات مع الإنشائي والمعماري، واستخراج جداول المواد بدقة.">Navigating 3D multidisciplinary models, clash detection resolution with structural/architectural, and automated material schedules.</p>
        </div>

        <!-- Tool 4: Oracle ERP -->
        <div class="software-tool-card">
          <div class="software-card-top">
            <h3 class="software-tool-name">Oracle ERP</h3>
            <span class="software-tool-score">92% Mastery</span>
          </div>
          <div class="software-gauge-bar"><div class="software-gauge-fill" style="width:92%;"></div></div>
          <p style="color:var(--ink-dim);font-size:0.9rem;line-height:1.6;" data-en="Purchase requisitions (PR), PO creation, budget allocation, vendor master file management, and inventory matching." data-ar="إدارة طلبات الشراء PR، إصدار أوامر الشراء PO، مراقبة الميزانيات، وإدارة سجل الموردين المعتمدين.">Purchase requisitions (PR), PO creation, budget allocation, vendor master file management, and inventory matching.</p>
        </div>

        <!-- Tool 5: SAP MM -->
        <div class="software-tool-card">
          <div class="software-card-top">
            <h3 class="software-tool-name">SAP MM</h3>
            <span class="software-tool-score">85% Mastery</span>
          </div>
          <div class="software-gauge-bar"><div class="software-gauge-fill" style="width:85%;"></div></div>
          <p style="color:var(--ink-dim);font-size:0.9rem;line-height:1.6;" data-en="Materials management, goods receipt verification (GRN), invoice validation, and supply chain transaction tracking." data-ar="إدارة المواد والمخزون، إشعارات الاستلام بالموقع GRN، مطابقة الفواتير، ومتابعة العمليات اللوجستية.">Materials management, goods receipt verification (GRN), invoice validation, and supply chain transaction tracking.</p>
        </div>

        <!-- Tool 6: Advanced Financial Excel -->
        <div class="software-tool-card">
          <div class="software-card-top">
            <h3 class="software-tool-name">Advanced Excel & BOQs</h3>
            <span class="software-tool-score">98% Mastery</span>
          </div>
          <div class="software-gauge-bar"><div class="software-gauge-fill" style="width:98%;"></div></div>
          <p style="color:var(--ink-dim);font-size:0.9rem;line-height:1.6;" data-en="Complex procurement leveling matrices, automated cost tracking dashboards, cash-flow forecasting, and macro models." data-ar="بناء نماذج تفريغ العطاءات المعقدة، لوحات متابعة التكاليف، التنبؤ بالتدفقات النقدية، ومعادلات التحليل المالي.">Complex procurement leveling matrices, automated cost tracking dashboards, cash-flow forecasting, and macro models.</p>
        </div>
      </div>
    </div>
  </section>
"""
    return head + body + get_page_tail()

# -------------------------------------------------------------
# 5. PROJECTS.HTML
# -------------------------------------------------------------
def build_projects():
    head = get_page_head("Projects Directory | Eng. Mostafa Abdelghany", "دليل المشاريع الشامل | م. مصطفى عبد الغني", "projects")
    body = """
  <header class="page-intro-header">
    <div class="container">
      <span class="page-intro-tag" data-en="Project Portfolio" data-ar="سجل الأعمال والمشاريع">Project Portfolio</span>
      <h1 class="page-intro-title" data-en="Comprehensive Projects Directory" data-ar="دليل المشاريع الكبرى والخبرات الموثقة">Comprehensive Projects Directory</h1>
      <p class="page-intro-subtitle" data-en="Explore 14 landmark infrastructure, high-rise, commercial, and governmental MEP projects across Saudi Arabia and Egypt." data-ar="استكشف 14 مشروعاً كبيراً في قطاعات البنية التحتية، الأبراج الشاهقة، المشافي، والمطارات في السعودية ومصر.">Explore 14 landmark infrastructure, high-rise, commercial, and governmental MEP projects across Saudi Arabia and Egypt.</p>
    </div>
  </header>

  <section class="section-wrapper">
    <div class="container">
      <!-- Filter Bar -->
      <div class="projects-filter-bar">
        <div class="pills-group" id="country-pills">
          <button class="filter-pill active" data-filter="all" data-en="All Projects (14)" data-ar="جميع المشاريع (14)">All Projects (14)</button>
          <button class="filter-pill" data-filter="ksa" data-en="Saudi Arabia 🇸🇦" data-ar="المملكة العربية السعودية 🇸🇦">Saudi Arabia 🇸🇦</button>
          <button class="filter-pill" data-filter="egypt" data-en="Egypt 🇪🇬" data-ar="جمهورية مصر العربية 🇪🇬">Egypt 🇪🇬</button>
        </div>

        <div class="search-input-box">
          <i class="fas fa-search" style="color:var(--ink-faint);font-size:13px;"></i>
          <input type="text" id="project-search" placeholder="Search projects, client, sector..." />
        </div>
      </div>

      <!-- Dynamic Project Cards Grid -->
      <div class="editorial-projects-grid" id="projects-grid-container">
        <!-- Rendered by scripts/projects.js -->
      </div>
    </div>
  </section>
"""
    return head + body + get_page_tail('<script src="scripts/projects.js"></script>')

# -------------------------------------------------------------
# 6. PROJECT-DETAIL.HTML
# -------------------------------------------------------------
def build_project_detail():
    head = get_page_head("Project Showcase | Eng. Mostafa Abdelghany", "تفاصيل المشروع | م. مصطفى عبد الغني", "projects")
    body = """
  <header class="page-intro-header">
    <div class="container">
      <a href="projects.html" class="page-intro-tag" style="display:inline-flex;align-items:center;gap:6px;cursor:pointer;">
        <i class="fas fa-arrow-left"></i> <span data-en="Back to Projects Directory" data-ar="العودة لدليل المشاريع">Back to Projects Directory</span>
      </a>
      <h1 class="page-intro-title" id="proj-detail-title">Project Title</h1>
      <p class="page-intro-subtitle" id="proj-detail-location">Location & Client Info</p>
    </div>
  </header>

  <section class="section-wrapper">
    <div class="container">
      <div class="project-sheet-layout">
        <!-- Gallery Viewer (Left) -->
        <div class="gallery-viewer-box">
          <div class="main-image-viewport" id="main-image-box">
            <img id="main-viewer-img" src="" alt="Project View" />
            <button class="gallery-nav-arrow prev" id="gallery-prev" aria-label="Previous image"><i class="fas fa-chevron-left"></i></button>
            <button class="gallery-nav-arrow next" id="gallery-next" aria-label="Next image"><i class="fas fa-chevron-right"></i></button>
          </div>
          <div class="thumbnails-strip" id="thumbnails-track">
            <!-- Rendered dynamically -->
          </div>
          <p style="font-family:var(--font-mono);font-size:11px;color:var(--ink-faint);margin-top:10px;text-align:center;" data-en="Click on image for Fullscreen Lightbox view" data-ar="انقر على الصورة للتكبير بشاشة كاملة (Lightbox)">Click on image for Fullscreen Lightbox view</p>
        </div>

        <!-- Metadata & Scope (Right) -->
        <div>
          <div class="meta-sheet-card">
            <span class="label" data-en="Contract & Value" data-ar="بيانات التعاقد والقيمة">Contract & Value</span>
            <div id="proj-value-badge" class="meta-sheet-value-badge">SAR 2.63 Billion</div>

            <div class="meta-spec-table">
              <div class="meta-spec-row">
                <span class="label" data-en="Employer" data-ar="شركة المقاولات">Employer</span>
                <span style="font-size:0.9rem;color:var(--ink);font-weight:500;" id="proj-employer">-</span>
              </div>
              <div class="meta-spec-row">
                <span class="label" data-en="Client" data-ar="المالك / العميل">Client</span>
                <span style="font-size:0.9rem;color:var(--ink);font-weight:500;" id="proj-client">-</span>
              </div>
              <div class="meta-spec-row">
                <span class="label" data-en="Consultant" data-ar="الاستشاري">Consultant</span>
                <span style="font-size:0.9rem;color:var(--ink);font-weight:500;" id="proj-consultant">-</span>
              </div>
              <div class="meta-spec-row">
                <span class="label" data-en="Timeline" data-ar="الفترة الزمنية">Timeline</span>
                <span style="font-size:0.9rem;color:var(--ink);font-weight:500;" id="proj-period">-</span>
              </div>
              <div class="meta-spec-row">
                <span class="label" data-en="My Role" data-ar="دوري في المشروع">My Role</span>
                <span style="font-size:0.9rem;color:var(--accent);font-weight:600;" id="proj-role">-</span>
              </div>
            </div>

            <span class="label" data-en="MEP Procurement & Technical Scope" data-ar="نطاق أعمال التوريد والكهروميكانيك">MEP Procurement & Technical Scope</span>
            <div class="scope-chips-group" id="proj-scope-chips">
              <!-- Rendered dynamically -->
            </div>

            <div style="border-top:1px solid var(--line);margin-top:24px;padding-top:20px;">
              <p style="color:var(--ink-dim);font-size:0.92rem;line-height:1.7;" id="proj-summary-text"></p>
            </div>

            <div style="margin-top:24px;display:flex;gap:12px;">
              <a class="btn-pill-primary" style="flex:1;justify-content:center;" id="inquire-project-btn" href="" target="_blank">
                <i class="fab fa-whatsapp"></i> <span data-en="Inquire About This Scope" data-ar="استفسار عن هذا النطاق">Inquire About This Scope</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- LIGHTBOX MODAL -->
  <div class="lightbox-overlay" id="lightbox-modal">
    <button class="lightbox-close-btn" id="lightbox-close"><i class="fas fa-times"></i></button>
    <div class="lightbox-img-box">
      <img id="lightbox-full-img" src="" alt="Enlarged Project Photo" />
    </div>
  </div>
"""
    return head + body + get_page_tail('<script src="scripts/project-detail.js"></script>')

# -------------------------------------------------------------
# 7. EXPERIENCE.HTML
# -------------------------------------------------------------
def build_experience():
    head = get_page_head("Career Experience | Eng. Mostafa Abdelghany", "المسيرة المهنية | م. مصطفى عبد الغني", "experience")
    body = """
  <header class="page-intro-header">
    <div class="container">
      <span class="page-intro-tag" data-en="Career Trajectory" data-ar="التسلسل الوظيفي">Career Trajectory</span>
      <h1 class="page-intro-title" data-en="9+ Years of Construction Leadership" data-ar="+9 سنوات من الريادة في قطاع الإنشاءات">9+ Years of Construction Leadership</h1>
      <p class="page-intro-subtitle" data-en="Progressive career progression from field site engineer to leading mega-procurement departments for tier-1 contracting groups." data-ar="مسار وظيفي تصاعدي من مهندس موقع إلى رئاسة أقسام المشتريات لكبرى مجموعات المقاولات في الشرق الأوسط.">Progressive career progression from field site engineer to leading mega-procurement departments for tier-1 contracting groups.</p>
    </div>
  </header>

  <section class="section-wrapper">
    <div class="container">
      <div style="max-width:900px;margin:0 auto;display:flex;flex-direction:column;gap:35px;">
        <!-- Station 1 -->
        <div style="background:var(--bg-elevated);border:1px solid var(--line-strong);border-radius:var(--radius-lg);padding:36px;border-left:4px solid var(--accent);">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;margin-bottom:12px;">
            <div>
              <span class="label gold-text" data-en="Current Leadership Position · Riyadh, KSA" data-ar="المنصب القيادي الحالي · الرياض، السعودية">Current Leadership Position · Riyadh, KSA</span>
              <h3 class="font-display" style="font-size:1.6rem;font-weight:600;color:var(--ink);margin-top:4px;" data-en="MEP Procurement Section Head" data-ar="رئيس قسم مشتريات الكهروميكانيك (MEP)">MEP Procurement Section Head</h3>
              <h4 style="font-size:1.1rem;color:var(--accent);margin-top:2px;">Zaid Al Hussain Group (2024 - Present)</h4>
            </div>
            <span class="label" style="background:rgba(212,175,55,0.1);padding:6px 14px;border-radius:var(--radius-full);color:var(--accent);">2024 — Present</span>
          </div>
          <p style="color:var(--ink-dim);font-size:0.95rem;line-height:1.7;margin-bottom:16px;" data-en="Spearheading MEP procurement, commercial negotiations, and subcontractor packages for the landmark King Abdullah International Gardens (SAR 2.63B)." data-ar="قيادة قسم المشتريات والتفاوض التجاري لحزم الكهروميكانيك والمقاولين الباطن لمشروع حدائق الملك عبدالله العالمية (2.63 مليار ريال).">Spearheading MEP procurement, commercial negotiations, and subcontractor packages for the landmark King Abdullah International Gardens (SAR 2.63B).</p>
          <div class="scope-chips-group">
            <span class="scope-chip">SAR 2.63B Tender Package</span>
            <span class="scope-chip">FIDIC Subcontracts</span>
            <span class="scope-chip">Value Engineering</span>
            <span class="scope-chip">Botanical Domes MEP</span>
          </div>
        </div>

        <!-- Station 2 -->
        <div style="background:var(--bg-elevated);border:1px solid var(--line);border-radius:var(--radius-lg);padding:36px;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;margin-bottom:12px;">
            <div>
              <span class="label" data-en="Megacity Development · New Capital, Egypt" data-ar="تطوير المدن الذكية · العاصمة الإدارية، مصر">Megacity Development · New Capital, Egypt</span>
              <h3 class="font-display" style="font-size:1.5rem;font-weight:600;color:var(--ink);margin-top:4px;" data-en="Senior Procurement Engineer" data-ar="مهندس مشتريات أول">Senior Procurement Engineer</h3>
              <h4 style="font-size:1rem;color:var(--ink-dim);margin-top:2px;">Atrium Quality Contractors / Talaat Moustafa Group (2023 - 2024)</h4>
            </div>
            <span class="label">2023 — 2024</span>
          </div>
          <p style="color:var(--ink-dim);font-size:0.95rem;line-height:1.7;margin-bottom:16px;" data-en="Managed multimillion procurement for Noor City infrastructure, commercial spine, water networks, and smart city infrastructure." data-ar="إدارة مشتريات البنية التحتية، شبكات المياه، والمنطقة التجارية لمدينة نور الذكية المتكاملة.">Managed multimillion procurement for Noor City infrastructure, commercial spine, water networks, and smart city infrastructure.</p>
        </div>

        <!-- Station 3 -->
        <div style="background:var(--bg-elevated);border:1px solid var(--line);border-radius:var(--radius-lg);padding:36px;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;margin-bottom:12px;">
            <div>
              <span class="label" data-en="Tier-1 Mega Contractor · Egypt" data-ar="المقاولات الكبرى · مصر">Tier-1 Mega Contractor · Egypt</span>
              <h3 class="font-display" style="font-size:1.5rem;font-weight:600;color:var(--ink);margin-top:4px;" data-en="Senior Procurement & MEP Engineer" data-ar="مهندس مشتريات وكهروميكانيك أول">Senior Procurement & MEP Engineer</h3>
              <h4 style="font-size:1rem;color:var(--ink-dim);margin-top:2px;">Hassan Allam Construction (2018 - 2021)</h4>
            </div>
            <span class="label">2018 — 2021</span>
          </div>
          <p style="color:var(--ink-dim);font-size:0.95rem;line-height:1.7;margin-bottom:16px;" data-en="Procurement engineering across strategic national assets including Aeon Towers (72m high-rise), Zewail City of Science, Berenice International Airport, and Egypt Exhibition Center." data-ar="هندسة المشتريات لمشاريع استراتيجية كبرى تشمل أبراج إيون، مدينة زويل للعلوم، مطار برنيس الدولي، ومركز مصر للمعارض.">Procurement engineering across strategic national assets including Aeon Towers (72m high-rise), Zewail City of Science, Berenice International Airport, and Egypt Exhibition Center.</p>
        </div>

        <!-- Station 4 & 5 -->
        <div style="background:var(--bg-elevated);border:1px solid var(--line);border-radius:var(--radius-lg);padding:36px;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;margin-bottom:12px;">
            <div>
              <span class="label" data-en="Early Career Foundations · KSA & Egypt" data-ar="التأسيس المهني · السعودية ومصر">Early Career Foundations · KSA & Egypt</span>
              <h3 class="font-display" style="font-size:1.5rem;font-weight:600;color:var(--ink);margin-top:4px;" data-en="Procurement & Technical Site Engineer" data-ar="مهندس موقع ومشتريات فنية">Procurement & Technical Site Engineer</h3>
              <h4 style="font-size:1rem;color:var(--ink-dim);margin-top:2px;">Pillars Construction & EDC Expertise (2016 - 2023)</h4>
            </div>
            <span class="label">2016 — 2023</span>
          </div>
          <p style="color:var(--ink-dim);font-size:0.95rem;line-height:1.7;" data-en="Executed site and procurement operations for Riyadh Metro Line 3, Hilton Riyadh, Radisson Blu, King Fahd Medical City, Zagazig University Hospital, and Berenice Military Base." data-ar="تنفيذ وإدارة المشتريات لمترو الرياض (المسار 3)، فندق هيلتون الرياض، راديسون بلو، مدينة الملك فهد الطبية، ومستشفى جامعة الزقازيق.">Executed site and procurement operations for Riyadh Metro Line 3, Hilton Riyadh, Radisson Blu, King Fahd Medical City, Zagazig University Hospital, and Berenice Military Base.</p>
        </div>
      </div>
    </div>
  </section>
"""
    return head + body + get_page_tail()

# -------------------------------------------------------------
# 8. CERTIFICATES.HTML
# -------------------------------------------------------------
def build_certificates():
    head = get_page_head("Certificates & Credentials | Eng. Mostafa Abdelghany", "الشهادات والاعتمادات الرسمية | م. مصطفى عبد الغني", "certificates")
    body = """
  <header class="page-intro-header">
    <div class="container">
      <span class="page-intro-tag" data-en="Verified Qualifications" data-ar="المؤهلات والشهادات المعتمدة">Verified Qualifications</span>
      <h1 class="page-intro-title" data-en="Certifications & Professional Licenses" data-ar="الشهادات المهنية والتراخيص الهندسية">Certifications & Professional Licenses</h1>
      <p class="page-intro-subtitle" data-en="All academic degrees, Saudi Council of Engineers accreditations, and company experience certificates with direct download access." data-ar="جميع الشهادات الأكاديمية، عضوية هيئة المهندسين، وشهادات الخبرة الرسمية مع إمكانية التحميل الفوري.">All academic degrees, Saudi Council of Engineers accreditations, and company experience certificates with direct download access.</p>
    </div>
  </header>

  <section class="section-wrapper">
    <div class="container">
      <div class="certs-3d-grid">
        <!-- Cert 1: SCE -->
        <div class="cert-perspective-card">
          <div class="cert-card-inner">
            <div class="cert-face">
              <div>
                <span class="label gold-text">Official License</span>
                <h3 class="font-display" style="font-size:1.3rem;color:var(--ink);margin:14px 0 6px;" data-en="Saudi Council of Engineers" data-ar="الهيئة السعودية للمهندسين">Saudi Council of Engineers</h3>
                <p style="color:var(--ink-dim);font-size:0.88rem;" data-en="Official Professional Membership #1084929 in Mechanical Power Engineering." data-ar="عضوية مهنية رسمية برقم 1084929 في الهندسة الميكانيكية.">Official Professional Membership #1084929 in Mechanical Power Engineering.</p>
              </div>
              <span class="label" style="color:var(--accent);">Flip for Details ↻</span>
            </div>
            <div class="cert-face cert-face-back">
              <i class="fas fa-id-card gold-text" style="font-size:36px;"></i>
              <h4 style="font-size:1.1rem;color:var(--ink);">SCE #1084929</h4>
              <p style="color:var(--ink-dim);font-size:0.85rem;" data-en="Registered in Riyadh, Saudi Arabia." data-ar="مسجل في الرياض، المملكة العربية السعودية.">Registered in Riyadh, Saudi Arabia.</p>
              <a class="btn-pill-primary" href="IntroductionLetter المهندسين السعوديين.pdf" target="_blank" data-en="Download Letter (PDF)" data-ar="تحميل الخطاب (PDF)">Download Letter</a>
            </div>
          </div>
        </div>

        <!-- Cert 2: B.Sc. Degree -->
        <div class="cert-perspective-card">
          <div class="cert-card-inner">
            <div class="cert-face">
              <div>
                <span class="label gold-text">Academic Degree</span>
                <h3 class="font-display" style="font-size:1.3rem;color:var(--ink);margin:14px 0 6px;" data-en="B.Sc. Mechanical Engineering" data-ar="بكالوريوس هندسة القوى الميكانيكية">B.Sc. Mechanical Engineering</h3>
                <p style="color:var(--ink-dim);font-size:0.88rem;" data-en="Faculty of Engineering, Benha University (Graduated 2015)." data-ar="كلية الهندسة بشبرا، جامعة بنها (دفعة 2015).">Faculty of Engineering, Benha University (Graduated 2015).</p>
              </div>
              <span class="label" style="color:var(--accent);">Flip for Details ↻</span>
            </div>
            <div class="cert-face cert-face-back">
              <i class="fas fa-graduation-cap gold-text" style="font-size:36px;"></i>
              <h4 style="font-size:1.1rem;color:var(--ink);">B.Sc. Mechanical Power</h4>
              <p style="color:var(--ink-dim);font-size:0.85rem;" data-en="Benha University, Egypt" data-ar="جامعة بنها، مصر">Benha University, Egypt</p>
              <a class="btn-pill-primary" href="شهادة التخرج.pdf" target="_blank" data-en="Download Degree (PDF)" data-ar="تحميل الشهادة (PDF)">Download Degree</a>
            </div>
          </div>
        </div>

        <!-- Cert 3: Experience Atrium -->
        <div class="cert-perspective-card">
          <div class="cert-card-inner">
            <div class="cert-face">
              <div>
                <span class="label gold-text">Experience Letter</span>
                <h3 class="font-display" style="font-size:1.3rem;color:var(--ink);margin:14px 0 6px;" data-en="Atrium Quality Contractors" data-ar="شهادة خبرة أتريوم للمقاولات">Atrium Quality Contractors</h3>
                <p style="color:var(--ink-dim);font-size:0.88rem;" data-en="Official experience documentation for Noor City New Capital project." data-ar="توثيق الخبرة الرسمية في مشروع مدينة نور بالعاصمة الإدارية.">Official experience documentation for Noor City New Capital project.</p>
              </div>
              <span class="label" style="color:var(--accent);">Flip for Details ↻</span>
            </div>
            <div class="cert-face cert-face-back">
              <i class="fas fa-building gold-text" style="font-size:36px;"></i>
              <h4 style="font-size:1.1rem;color:var(--ink);">Atrium / TMG Experience</h4>
              <p style="color:var(--ink-dim);font-size:0.85rem;" data-en="Senior Procurement Engineer" data-ar="مهندس مشتريات أول">Senior Procurement Engineer</p>
              <a class="btn-pill-primary" href="شهادة خبرة اتريم طلعت مصطفي.pdf" target="_blank" data-en="Download Letter (PDF)" data-ar="تحميل الشهادة (PDF)">Download Letter</a>
            </div>
          </div>
        </div>

        <!-- Cert 4: Experience Pillars -->
        <div class="cert-perspective-card">
          <div class="cert-card-inner">
            <div class="cert-face">
              <div>
                <span class="label gold-text">Experience Letter</span>
                <h3 class="font-display" style="font-size:1.3rem;color:var(--ink);margin:14px 0 6px;" data-en="Pillars Construction" data-ar="شهادة خبرة بيلرز للإنشاءات">Pillars Construction</h3>
                <p style="color:var(--ink-dim);font-size:0.88rem;" data-en="Official certification of procurement and technical execution." data-ar="شهادة خبرة رسمية في إدارة المشتريات والتنفيذ الفني.">Official certification of procurement and technical execution.</p>
              </div>
              <span class="label" style="color:var(--accent);">Flip for Details ↻</span>
            </div>
            <div class="cert-face cert-face-back">
              <i class="fas fa-award gold-text" style="font-size:36px;"></i>
              <h4 style="font-size:1.1rem;color:var(--ink);">Pillars Construction</h4>
              <p style="color:var(--ink-dim);font-size:0.85rem;" data-en="Procurement & MEP Engineer" data-ar="مهندس مشتريات وكهروميكانيك">Procurement & MEP Engineer</p>
              <a class="btn-pill-primary" href="شهادة خبرة بيلرز.pdf" target="_blank" data-en="Download Letter (PDF)" data-ar="تحميل الشهادة (PDF)">Download Letter</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    return head + body + get_page_tail()

# -------------------------------------------------------------
# 9. CONTACT.HTML
# -------------------------------------------------------------
def build_contact():
    head = get_page_head("Contact & Hire | Eng. Mostafa Abdelghany", "تواصل وتعاقد | م. مصطفى عبد الغني", "contact")
    body = """
  <header class="page-intro-header">
    <div class="container">
      <span class="page-intro-tag" data-en="Let's Collaborate" data-ar="ابدأ التعاون الهندسي">Let's Collaborate</span>
      <h1 class="page-intro-title" data-en="Initiate a Project or Consultation" data-ar="طلب استشارة أو مناقشة تعاقد جديد">Initiate a Project or Consultation</h1>
      <p class="page-intro-subtitle" data-en="Available for full-time leadership roles, executive freelance consulting, and tender procurement audits across the GCC." data-ar="متاح للمناصب القيادية، الاستشارات الفنية والتعاقدات الحرة، وتدقيق مناقصات الـ MEP في الخليج ومصر.">Available for full-time leadership roles, executive freelance consulting, and tender procurement audits across the GCC.</p>
    </div>
  </header>

  <section class="section-wrapper">
    <div class="container">
      <div class="contact-split-grid">
        <!-- Direct Contact Channels -->
        <div class="contact-info-panel">
          <a class="contact-card-box" href="https://wa.me/966502582122?text=Hello%20Eng.%20Mostafa,%20I%20would%20like%20to%20get%20in%20touch." target="_blank">
            <div>
              <span class="label" data-en="Instant Message" data-ar="محادثة فورية">Instant Message</span>
              <h4 style="font-size:1.1rem;color:var(--ink);margin-top:4px;">WhatsApp Direct</h4>
              <span style="font-size:0.88rem;color:var(--accent);">+966 502 582 122</span>
            </div>
            <i class="fab fa-whatsapp gold-text" style="font-size:26px;"></i>
          </a>

          <a class="contact-card-box" href="mailto:engmostafamahoud2012@gmail.com">
            <div>
              <span class="label" data-en="Email Inquiries" data-ar="البريد الإلكتروني">Email Inquiries</span>
              <h4 style="font-size:1.1rem;color:var(--ink);margin-top:4px;">Official Email</h4>
              <span style="font-size:0.88rem;color:var(--accent);">engmostafamahoud2012@gmail.com</span>
            </div>
            <i class="fas fa-envelope gold-text" style="font-size:24px;"></i>
          </a>

          <a class="contact-card-box" href="tel:+966502582122">
            <div>
              <span class="label" data-en="Direct Call" data-ar="اتصال هاتفي">Direct Call</span>
              <h4 style="font-size:1.1rem;color:var(--ink);margin-top:4px;">Phone (KSA)</h4>
              <span style="font-size:0.88rem;color:var(--accent);">+966 502 582 122</span>
            </div>
            <i class="fas fa-phone gold-text" style="font-size:22px;"></i>
          </a>

          <a class="contact-card-box" href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank">
            <div>
              <span class="label" data-en="Professional Network" data-ar="شبكة الأعمال">Professional Network</span>
              <h4 style="font-size:1.1rem;color:var(--ink);margin-top:4px;">LinkedIn Profile</h4>
              <span style="font-size:0.88rem;color:var(--accent);">/mostafa-abdelghany-procurement</span>
            </div>
            <i class="fab fa-linkedin gold-text" style="font-size:26px;"></i>
          </a>
        </div>

        <!-- Consultation Request Form -->
        <div class="contact-form-glass">
          <h3 class="font-display" style="font-size:1.5rem;font-weight:600;color:var(--ink);margin-bottom:20px;" data-en="Send an Inquiry / Project Request" data-ar="إرسال طلب استشارة أو تسعير مشروع">Send an Inquiry / Project Request</h3>
          <form id="contact-inquiry-form">
            <div class="form-group-block">
              <label class="form-label-title" data-en="Your Full Name" data-ar="الاسم الكامل">Your Full Name</label>
              <input class="form-input-field" type="text" id="form-name" required placeholder="e.g. Abdullah Al-Otaibi" />
            </div>

            <div class="form-group-block">
              <label class="form-label-title" data-en="Company / Organization" data-ar="اسم الشركة / الجهة">Company / Organization</label>
              <input class="form-input-field" type="text" id="form-company" placeholder="e.g. Saudi Construction Co." />
            </div>

            <div class="form-group-block">
              <label class="form-label-title" data-en="Service Required" data-ar="نوع الخدمة المطلوبة">Service Required</label>
              <select class="form-select-field" id="form-service">
                <option value="Tender Pricing & BOQ" data-en="Tender Pricing & BOQ" data-ar="تسعير مناقصات وجداول كميات">Tender Pricing & BOQ</option>
                <option value="Value Engineering Audit" data-en="Value Engineering Audit" data-ar="هندسة القيمة وتحسين التكاليف">Value Engineering Audit</option>
                <option value="Subcontract Negotiation" data-en="Subcontract Negotiation" data-ar="صياغة وتفاوض عقود الباطن">Subcontract Negotiation</option>
                <option value="Freelance Package Management" data-en="Freelance Package Management" data-ar="إدارة حزمة مشتريات فريلانس">Freelance Package Management</option>
                <option value="Executive Full-Time Role" data-en="Executive Full-Time Role" data-ar="عرض منصب قيادي بدوام كامل">Executive Full-Time Role</option>
              </select>
            </div>

            <div class="form-group-block">
              <label class="form-label-title" data-en="Project Details & Scope" data-ar="تفاصيل المشروع والنطاق المطلوب">Project Details & Scope</label>
              <textarea class="form-textarea-field" id="form-message" rows="4" required placeholder="Describe your project, timeline, and required deliverables..."></textarea>
            </div>

            <button type="submit" class="btn-pill-primary" style="width:100%;justify-content:center;">
              <i class="fab fa-whatsapp"></i> <span data-en="Send via WhatsApp Direct" data-ar="إرسال عبر الواتساب فوراً">Send via WhatsApp Direct</span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
"""
    return head + body + get_page_tail()

# Write all pages
pages = {
    "index.html": build_index(),
    "about.html": build_about(),
    "services.html": build_services(),
    "software.html": build_software(),
    "projects.html": build_projects(),
    "project-detail.html": build_project_detail(),
    "experience.html": build_experience(),
    "certificates.html": build_certificates(),
    "contact.html": build_contact(),
}

for name, content in pages.items():
    file_path = os.path.join(base_dir, name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated Ultra-Dark V3: {name} ({len(content.encode('utf-8')):,} bytes)")

print("\nAll 9 Ultra-Dark Multi-Page files generated successfully!")
