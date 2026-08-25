/**
 * Main JavaScript functionality for Eng. Mostafa Portfolio V2
 * Features: Navigation, KPI Counters, Project Filtering, Modal Carousel,
 *           Certificates Flip, Theme Toggle, Language Toggle (AR/EN RTL),
 *           Typewriter Effect, 3D Tilt, Magnetic Buttons, Contact Form
 */

document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------
    // 1. Navigation & Scroll Handling
    // -------------------------------------------------------------
    const navbar = document.getElementById('navbar');
    const scrollProgress = document.getElementById('scroll-progress');
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');
    const cvFloatBtn = document.getElementById('cv-float-btn');
    const heroSection = document.getElementById('hero');
    let lastScrollY = window.scrollY;

    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;

        // Navbar hide on scroll down, show on scroll up
        if (currentScrollY > 100) {
            navbar.classList.add('scrolled');
            if (currentScrollY > lastScrollY && currentScrollY > 300) {
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

        // Active Link on Scroll
        const sections = document.querySelectorAll('section[id]');
        sections.forEach(sec => {
            const top = window.scrollY;
            const offset = sec.offsetTop - 180;
            const height = sec.offsetHeight;
            const id = sec.getAttribute('id');
            if (top >= offset && top < offset + height) {
                document.querySelectorAll('.nav-links .nav-link').forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });

        // Floating CV Button Visibility
        if (cvFloatBtn && heroSection) {
            if (currentScrollY > heroSection.offsetHeight * 0.6) {
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

        // Close mobile nav when clicking a link
        document.querySelectorAll('.nav-links .nav-link').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });
    }

    // -------------------------------------------------------------
    // 2. KPI Counter Animation (0 -> target with prefix/suffix)
    // -------------------------------------------------------------
    const counters = document.querySelectorAll('.kpi-number');
    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const targetEl = entry.target;
                const targetVal = parseFloat(targetEl.getAttribute('data-target')) || 0;
                const prefix = targetEl.getAttribute('data-prefix') || '';
                const suffix = targetEl.getAttribute('data-suffix') || '';
                const isDecimal = targetEl.getAttribute('data-decimal') === 'true';

                let startVal = 0;
                const duration = 2000;
                const steps = 60;
                const stepTime = duration / steps;
                const increment = targetVal / steps;

                const timer = setInterval(() => {
                    startVal += increment;
                    if (startVal >= targetVal) {
                        startVal = targetVal;
                        clearInterval(timer);
                    }
                    const formatted = isDecimal ? startVal.toFixed(2) : Math.floor(startVal).toString();
                    targetEl.textContent = `${prefix}${formatted}${suffix}`;
                }, stepTime);

                observer.unobserve(targetEl);
            }
        });
    }, { threshold: 0.3 });

    counters.forEach(c => counterObserver.observe(c));

    // -------------------------------------------------------------
    // 3. Project Filter Tabs
    // -------------------------------------------------------------
    const filterTabs = document.querySelectorAll('.filter-tab');
    const projectCards = document.querySelectorAll('.project-card');

    filterTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            filterTabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            const category = tab.getAttribute('data-filter');

            projectCards.forEach(card => {
                const cardCat = card.getAttribute('data-category');
                if (category === 'all' || cardCat === category) {
                    card.classList.remove('hide');
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    card.classList.add('hide');
                }
            });

            // Trigger Map synchronization
            if (typeof window.filterMapMarkers === 'function') {
                window.filterMapMarkers(category);
            }
        });
    });

    // -------------------------------------------------------------
    // 4. Project Modal & Carousel Lightbox
    // -------------------------------------------------------------
    const projectModal = document.getElementById('project-modal');
    const modalClose = projectModal ? projectModal.querySelector('.modal-close') : null;
    const carouselTrack = document.getElementById('carousel-track');
    const carouselDots = document.getElementById('carousel-dots');
    const prevBtn = projectModal ? projectModal.querySelector('.carousel-prev') : null;
    const nextBtn = projectModal ? projectModal.querySelector('.carousel-next') : null;

    let currentSlide = 0;
    let totalSlides = 0;

    const updateCarousel = (index) => {
        currentSlide = (index + totalSlides) % totalSlides;
        if (carouselTrack) {
            carouselTrack.style.transform = `translateX(-${currentSlide * 100}%)`;
        }
        if (carouselDots) {
            const dots = carouselDots.querySelectorAll('.dot');
            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === currentSlide);
            });
        }
    };

    if (prevBtn) prevBtn.addEventListener('click', () => updateCarousel(currentSlide - 1));
    if (nextBtn) nextBtn.addEventListener('click', () => updateCarousel(currentSlide + 1));

    if (projectModal) {
        projectCards.forEach(card => {
            card.addEventListener('click', () => {
                const isAr = document.documentElement.getAttribute('lang') === 'ar';
                const name = isAr ? (card.getAttribute('data-name-ar') || card.getAttribute('data-name')) : card.getAttribute('data-name');
                const company = card.getAttribute('data-company') || '';
                const role = card.getAttribute('data-role') || '';
                const year = card.getAttribute('data-year') || '';
                const location = card.getAttribute('data-location') || '';
                const value = card.getAttribute('data-value') || '';
                const client = card.getAttribute('data-client') || '';
                const stakeholders = card.getAttribute('data-stakeholders') || '';
                const desc = card.getAttribute('data-desc') || '';
                const imagesStr = card.getAttribute('data-images') || '';
                const images = imagesStr ? imagesStr.split(',').map(s => s.trim()).filter(Boolean) : [];

                // Populate modal text fields
                document.getElementById('modal-title').textContent = name;
                document.getElementById('modal-company').textContent = company;
                document.getElementById('modal-role').textContent = role;
                document.getElementById('modal-year').textContent = year;
                document.getElementById('modal-location').textContent = location;
                document.getElementById('modal-desc').textContent = desc;

                // Value container
                const valContainer = document.getElementById('modal-value-container');
                if (valContainer) {
                    if (value) {
                        valContainer.style.display = 'block';
                        document.getElementById('modal-value').textContent = value;
                    } else {
                        valContainer.style.display = 'none';
                    }
                }

                // Client container
                const clientContainer = document.getElementById('modal-client-container');
                if (clientContainer) {
                    if (client) {
                        clientContainer.style.display = 'block';
                        document.getElementById('modal-client').textContent = client;
                    } else {
                        clientContainer.style.display = 'none';
                    }
                }

                // Stakeholders container
                const stContainer = document.getElementById('modal-stakeholders-container');
                if (stContainer) {
                    if (stakeholders) {
                        stContainer.style.display = 'block';
                        document.getElementById('modal-stakeholders').textContent = stakeholders;
                    } else {
                        stContainer.style.display = 'none';
                    }
                }

                // Populate Carousel Images
                if (carouselTrack && carouselDots) {
                    carouselTrack.innerHTML = '';
                    carouselDots.innerHTML = '';
                    totalSlides = images.length;
                    currentSlide = 0;

                    if (images.length === 0) {
                        const fallbackImg = card.querySelector('.card-image img');
                        if (fallbackImg) images.push(fallbackImg.src);
                        totalSlides = images.length;
                    }

                    images.forEach((imgSrc, idx) => {
                        const img = document.createElement('img');
                        img.src = imgSrc;
                        img.alt = `${name} - Photo ${idx + 1}`;
                        carouselTrack.appendChild(img);

                        const dot = document.createElement('span');
                        dot.className = `dot ${idx === 0 ? 'active' : ''}`;
                        dot.addEventListener('click', () => updateCarousel(idx));
                        carouselDots.appendChild(dot);
                    });

                    // Hide next/prev if only 1 image
                    if (prevBtn && nextBtn) {
                        prevBtn.style.display = totalSlides > 1 ? 'flex' : 'none';
                        nextBtn.style.display = totalSlides > 1 ? 'flex' : 'none';
                    }
                    carouselDots.style.display = totalSlides > 1 ? 'flex' : 'none';

                    updateCarousel(0);
                }

                // Open modal
                projectModal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        const closeModal = () => {
            projectModal.classList.remove('active');
            document.body.style.overflow = 'auto';
        };

        if (modalClose) modalClose.addEventListener('click', closeModal);
        projectModal.addEventListener('click', (e) => {
            if (e.target === projectModal) closeModal();
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && projectModal.classList.contains('active')) closeModal();
        });
    }

    // -------------------------------------------------------------
    // 5. Certificate Flip Cards
    // -------------------------------------------------------------
    const certCards = document.querySelectorAll('.cert-card');
    certCards.forEach(card => {
        card.addEventListener('click', () => {
            card.classList.toggle('flipped');
        });
    });

    // -------------------------------------------------------------
    // 6. Theme Toggle (Dark/Light)
    // -------------------------------------------------------------
    const themeToggle = document.getElementById('theme-toggle');
    const savedTheme = localStorage.getItem('portfolio_theme');
    if (savedTheme === 'light') {
        document.body.classList.add('light-theme');
        if (themeToggle) themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('light-theme');
            const isLight = document.body.classList.contains('light-theme');
            themeToggle.innerHTML = isLight ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
            localStorage.setItem('portfolio_theme', isLight ? 'light' : 'dark');
        });
    }

    // -------------------------------------------------------------
    // 7. Language Toggle (Bilingual EN/AR with RTL support)
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

        // Update all elements with data-en / data-ar
        const translatable = document.querySelectorAll('[data-en][data-ar]');
        translatable.forEach(el => {
            const text = el.getAttribute(`data-${lang}`);
            if (text) el.innerHTML = text;
        });

        // Update placeholders
        const formInputs = document.querySelectorAll('#contact-form input, #contact-form textarea');
        // Let labels float correctly
        localStorage.setItem('portfolio_lang', lang);
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
    // 8. Typewriter Effect
    // -------------------------------------------------------------
    const typewriterEl = document.getElementById('typewriter-text');
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
            speed = 2200; // Pause at end of text
            deleting = true;
        } else if (deleting && cIdx === 0) {
            deleting = false;
            pIdx = (pIdx + 1) % phrases.length;
            speed = 400;
        }

        setTimeout(runTypewriter, speed);
    };
    runTypewriter();

    // -------------------------------------------------------------
    // 9. 3D Tilt Effect on Project Cards
    // -------------------------------------------------------------
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
        projectCards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const cx = rect.width / 2;
                const cy = rect.height / 2;
                const rotX = ((y - cy) / cy) * -8;
                const rotY = ((x - cx) / cx) * 8;
                card.style.transform = `perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateY(-8px)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
            });
        });
    }

    // -------------------------------------------------------------
    // 10. Magnetic Buttons
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
    // 11. Contact Form Handling
    // -------------------------------------------------------------
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('form-name').value;
            const email = document.getElementById('form-email').value;
            const subject = document.getElementById('form-subject').value || 'Portfolio Contact';
            const message = document.getElementById('form-message').value;

            // Direct mailto fallback or notification
            const mailtoLink = `mailto:engmostafamahoud2012@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(`From: ${name} (${email})\n\nMessage:\n${message}`)}`;
            window.location.href = mailtoLink;

            if (formStatus) {
                formStatus.className = 'form-status success';
                const isAr = document.documentElement.getAttribute('lang') === 'ar';
                formStatus.textContent = isAr ? 'تم فتح تطبيق البريد لإرسال رسالتك مباشرة!' : 'Opening your email client to send the message!';
            }
            contactForm.reset();
        });
    }
});
