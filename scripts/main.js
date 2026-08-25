/**
 * Main Global Controller for Eng. Mostafa Abdelghany Portfolio Portal (V3)
 * Shared across all pages: Navigation, Language persistence (RTL/LTR),
 * Theme persistence (Dark/Light), Scroll progress, and Mobile Menu.
 */

document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------
    // 1. Navigation & Page Detection
    // -------------------------------------------------------------
    const navbar = document.getElementById('navbar');
    const scrollProgress = document.getElementById('scroll-progress');
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');
    const cvFloatBtn = document.getElementById('cv-float-btn');
    let lastScrollY = window.scrollY;

    // Detect active page in navbar
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links .nav-link').forEach(link => {
        const linkHref = link.getAttribute('href');
        if (linkHref === currentPath || (currentPath === '' && linkHref === 'index.html')) {
            link.classList.add('active');
        } else if (!linkHref.startsWith('#')) {
            link.classList.remove('active');
        }
    });

    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;

        // Navbar scroll behavior
        if (currentScrollY > 60) {
            navbar.classList.add('scrolled');
            if (currentScrollY > lastScrollY && currentScrollY > 250) {
                navbar.classList.add('hidden');
            } else {
                navbar.classList.remove('hidden');
            }
        } else {
            navbar.classList.remove('scrolled', 'hidden');
        }
        lastScrollY = currentScrollY;

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
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        document.querySelectorAll('.nav-links .nav-link').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
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
            langToggle.innerHTML = `<span>${isAr ? 'EN' : 'AR'}</span>`;
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
    // 4. Typewriter Effect (Used in Hero Sections)
    // -------------------------------------------------------------
    const typewriterEl = document.getElementById('typewriter-text');
    if (typewriterEl) {
        const phrasesEn = [
            'MEP Procurement Section Head',
            'SAR 2.63B+ Mega-Project Lead',
            'Senior MEP Procurement Expert',
            'Supply Chain & Cost Optimizer'
        ];
        const phrasesAr = [
            'رئيس قسم مشتريات أعمال MEP',
            'مدير مشتريات مشاريع بقيمة 2.63 مليار ريال',
            'خبير استراتيجي في سلاسل الإمداد',
            'متخصص في هندسة التكاليف والتفاوض'
        ];

        let pIdx = 0;
        let cIdx = 0;
        let deleting = false;

        const runTypewriter = () => {
            if (!typewriterEl) return;
            const isAr = document.documentElement.getAttribute('lang') === 'ar';
            const phrases = isAr ? phrasesAr : phrasesEn;
            const phrase = phrases[pIdx % phrases.length];

            if (deleting) {
                typewriterEl.textContent = phrase.substring(0, cIdx - 1);
                cIdx--;
            } else {
                typewriterEl.textContent = phrase.substring(0, cIdx + 1);
                cIdx++;
            }

            let speed = deleting ? 35 : 75;
            if (!deleting && cIdx === phrase.length) {
                speed = 2200;
                deleting = true;
            } else if (deleting && cIdx === 0) {
                deleting = false;
                pIdx = (pIdx + 1) % phrases.length;
                speed = 400;
            }

            setTimeout(runTypewriter, speed);
        };
        runTypewriter();
    }

    // -------------------------------------------------------------
    // 5. Magnetic Buttons & 3D Hover
    // -------------------------------------------------------------
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
        const magneticBtns = document.querySelectorAll('.magnetic-btn');
        magneticBtns.forEach(btn => {
            btn.addEventListener('mousemove', (e) => {
                const rect = btn.getBoundingClientRect();
                const bx = rect.left + rect.width / 2;
                const by = rect.top + rect.height / 2;
                const dx = (e.clientX - bx) * 0.25;
                const dy = (e.clientY - by) * 0.25;
                btn.style.transform = `translate(${dx}px, ${dy}px)`;
            });
            btn.addEventListener('mouseleave', () => {
                btn.style.transform = 'translate(0, 0)';
            });
        });
    }

    // -------------------------------------------------------------
    // 6. Contact Form (WhatsApp / Email Integration)
    // -------------------------------------------------------------
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('form-name')?.value || '';
            const email = document.getElementById('form-email')?.value || '';
            const service = document.getElementById('form-service')?.value || 'General Inquiry';
            const subject = document.getElementById('form-subject')?.value || `Inquiry: ${service}`;
            const message = document.getElementById('form-message')?.value || '';

            const isAr = document.documentElement.getAttribute('lang') === 'ar';

            // Open WhatsApp direct or Mailto fallback
            const fullBody = `*Client Inquiry*\nName: ${name}\nEmail: ${email}\nService: ${service}\nSubject: ${subject}\n\nMessage:\n${message}`;
            const waUrl = `https://wa.me/966502582122?text=${encodeURIComponent(fullBody)}`;
            
            window.open(waUrl, '_blank');

            if (formStatus) {
                formStatus.className = 'form-status success';
                formStatus.textContent = isAr 
                    ? 'جاري تحويلك إلى واتساب لإرسال رسالتك وتأكيد حجز الاستشارة مباشرة!'
                    : 'Redirecting to WhatsApp to send your inquiry directly!';
            }
            contactForm.reset();
        });
    }
});
