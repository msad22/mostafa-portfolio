/**
 * Main Global Controller for Eng. Mostafa Abdelghany Portfolio Portal (V3)
 * Shared across all pages: Floating Pill Nav, Language persistence (RTL/LTR),
 * Theme persistence (Dark/Light), Scroll progress, and Mobile Menu.
 */

document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------
    // 1. Navigation & Page Detection
    // -------------------------------------------------------------
    const scrollProgress = document.getElementById('scroll-progress');
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const navMenu = document.getElementById('nav-menu');
    const cvFloatBtn = document.getElementById('cv-float-btn');

    // Detect active page in navbar
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-pill-link').forEach(link => {
        const linkHref = link.getAttribute('href');
        if (linkHref === currentPath || (currentPath === '' && linkHref === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });

    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;

        // Scroll Progress Bar
        const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
        if (scrollHeight > 0 && scrollProgress) {
            const scrolled = (currentScrollY / scrollHeight) * 100;
            scrollProgress.style.width = `${scrolled}%`;
        }

        // Floating CV Button Visibility
        if (cvFloatBtn) {
            if (currentScrollY > 300) {
                cvFloatBtn.classList.add('visible');
            } else {
                cvFloatBtn.classList.remove('visible');
            }
        }
    });

    // Mobile Hamburger Toggle
    if (hamburgerBtn && navMenu) {
        hamburgerBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });

        document.querySelectorAll('.nav-pill-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });
    }

    // -------------------------------------------------------------
    // 2. Theme Toggle (Dark/Light) with localStorage
    // -------------------------------------------------------------
    const themeToggle = document.getElementById('theme-toggle');
    const savedTheme = localStorage.getItem('portfolio_theme') || 'dark';

    const applyTheme = (theme) => {
        if (theme === 'light') {
            document.body.classList.add('light-theme');
            if (themeToggle) themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        } else {
            document.body.classList.remove('light-theme');
            if (themeToggle) themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
        }
        localStorage.setItem('portfolio_theme', theme);
    };

    applyTheme(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const isLight = document.body.classList.contains('light-theme');
            applyTheme(isLight ? 'dark' : 'light');
        });
    }

    // -------------------------------------------------------------
    // 3. Language Toggle (Bilingual EN/AR with RTL Support)
    // -------------------------------------------------------------
    const langToggle = document.getElementById('lang-toggle');
    const savedLang = localStorage.getItem('portfolio_lang') || 'en';

    const applyLanguage = (lang) => {
        const isAr = lang === 'ar';
        document.documentElement.setAttribute('lang', lang);
        document.documentElement.setAttribute('dir', isAr ? 'rtl' : 'ltr');
        document.documentElement.classList.toggle('rtl', isAr);

        if (langToggle) {
            langToggle.innerHTML = `<span id="lang-text">${isAr ? 'EN' : 'AR'}</span>`;
        }

        // Swap all elements with data-en / data-ar
        const translatable = document.querySelectorAll('[data-en][data-ar]');
        translatable.forEach(el => {
            const text = el.getAttribute(`data-${lang}`);
            if (text) el.innerHTML = text;
        });

        localStorage.setItem('portfolio_lang', lang);

        // Notify other scripts
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang, isAr } }));
    };

    applyLanguage(savedLang);

    if (langToggle) {
        langToggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('lang') || 'en';
            const next = current === 'en' ? 'ar' : 'en';
            applyLanguage(next);
        });
    }

    // -------------------------------------------------------------
    // 4. Contact / Inquiry Form (WhatsApp Direct Integration)
    // -------------------------------------------------------------
    const contactForm = document.getElementById('contact-inquiry-form');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('form-name')?.value || '';
            const company = document.getElementById('form-company')?.value || '';
            const service = document.getElementById('form-service')?.value || 'Full-Time Job Opportunity';
            const message = document.getElementById('form-message')?.value || '';

            const fullBody = `*New Inquiry / رسالة جديدة*\nName: ${name}\nCompany: ${company}\nReason: ${service}\n\nMessage:\n${message}`;
            const waUrl = `https://wa.me/966502582122?text=${encodeURIComponent(fullBody)}`;
            
            window.open(waUrl, '_blank');
            contactForm.reset();
        });
    }
});
