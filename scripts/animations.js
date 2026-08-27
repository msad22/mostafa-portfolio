/**
 * Comprehensive Animations & User Interactivity Controller
 * Eng. Mostafa Abdelghany Portfolio
 * Features: Canvas Constellations, CountUp Numbers, 3D Perspective Tilt,
 * Interactive Before/After Slider, and Freelance Package Estimator.
 */

document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------
    // 1. Canvas Constellation Particle System
    // -------------------------------------------------------------
    const canvas = document.getElementById('hero-particles-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width = (canvas.width = canvas.offsetWidth);
        let height = (canvas.height = canvas.offsetHeight);

        window.addEventListener('resize', () => {
            if (!canvas) return;
            width = canvas.width = canvas.offsetWidth;
            height = canvas.height = canvas.offsetHeight;
        });

        const particles = [];
        const particleCount = Math.min(Math.floor(width / 18), 65);

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.5;
                this.vy = (Math.random() - 0.5) * 0.5;
                this.radius = Math.random() * 2 + 1;
                this.color = Math.random() > 0.4 ? '#F59E0B' : '#06B6D4';
                this.alpha = Math.random() * 0.5 + 0.2;
            }
            update() {
                this.x += this.vx;
                this.y += this.vy;
                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;
            }
            draw() {
                ctx.save();
                ctx.globalAlpha = this.alpha;
                ctx.fillStyle = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }
        }

        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }

        let mouseX = null;
        let mouseY = null;
        window.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            if (e.clientY <= rect.bottom) {
                mouseX = e.clientX - rect.left;
                mouseY = e.clientY - rect.top;
            } else {
                mouseX = null;
                mouseY = null;
            }
        });

        const animateParticles = () => {
            ctx.clearRect(0, 0, width, height);

            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();

                // Connect nearby particles
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    if (dist < 110) {
                        ctx.save();
                        ctx.strokeStyle = '#F59E0B';
                        ctx.globalAlpha = (1 - dist / 110) * 0.18;
                        ctx.lineWidth = 0.8;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                        ctx.restore();
                    }
                }

                // Connect to mouse
                if (mouseX !== null && mouseY !== null) {
                    const mdx = particles[i].x - mouseX;
                    const mdy = particles[i].y - mouseY;
                    const mdist = Math.sqrt(mdx * mdx + mdy * mdy);
                    if (mdist < 130) {
                        ctx.save();
                        ctx.strokeStyle = '#06B6D4';
                        ctx.globalAlpha = (1 - mdist / 130) * 0.35;
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(mouseX, mouseY);
                        ctx.stroke();
                        ctx.restore();
                    }
                }
            }
            requestAnimationFrame(animateParticles);
        };
        animateParticles();
    }

    // -------------------------------------------------------------
    // 2. Animated Stats Number Counters (Count-Up)
    // -------------------------------------------------------------
    const countEls = document.querySelectorAll('.animate-counter');
    if (countEls.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const target = parseFloat(el.getAttribute('data-target'));
                    const isDecimal = el.getAttribute('data-decimal') === 'true';
                    const suffix = el.getAttribute('data-suffix') || '';
                    const duration = 2000;
                    const startTime = performance.now();

                    const updateCount = (now) => {
                        const elapsed = now - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const easeOut = 1 - Math.pow(1 - progress, 3);
                        const current = easeOut * target;

                        if (isDecimal) {
                            el.textContent = current.toFixed(2) + suffix;
                        } else {
                            el.textContent = Math.floor(current) + suffix;
                        }

                        if (progress < 1) {
                            requestAnimationFrame(updateCount);
                        } else {
                            if (isDecimal) {
                                el.textContent = target.toFixed(2) + suffix;
                            } else {
                                el.textContent = target + suffix;
                            }
                        }
                    };
                    requestAnimationFrame(updateCount);
                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.2 });

        countEls.forEach(el => observer.observe(el));
    }

    // -------------------------------------------------------------
    // 3. 3D Perspective Tilt on Mousemove
    // -------------------------------------------------------------
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
        const tiltCards = document.querySelectorAll('.tilt-card-item, .editorial-project-card');
        tiltCards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = ((y - centerY) / centerY) * -6;
                const rotateY = ((x - centerX) / centerX) * 6;

                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
            });
        });
    }

    // -------------------------------------------------------------
    // 4. Interactive Before/After (BIM vs Site) Slider
    // -------------------------------------------------------------
    const sliderContainer = document.getElementById('bim-comparison-slider');
    const overlayLayer = document.getElementById('comparison-overlay');
    const handle = document.getElementById('comparison-handle');

    if (sliderContainer && overlayLayer && handle) {
        let isSliding = false;

        const updateSliderPos = (clientX) => {
            const rect = sliderContainer.getBoundingClientRect();
            let offsetX = clientX - rect.left;
            if (offsetX < 0) offsetX = 0;
            if (offsetX > rect.width) offsetX = rect.width;

            const percent = (offsetX / rect.width) * 100;
            overlayLayer.style.width = `${percent}%`;
            handle.style.left = `${percent}%`;
        };

        sliderContainer.addEventListener('mousedown', (e) => {
            isSliding = true;
            updateSliderPos(e.clientX);
        });

        window.addEventListener('mouseup', () => { isSliding = false; });
        window.addEventListener('mousemove', (e) => {
            if (!isSliding) return;
            updateSliderPos(e.clientX);
        });

        // Touch support
        sliderContainer.addEventListener('touchstart', (e) => {
            isSliding = true;
            updateSliderPos(e.touches[0].clientX);
        });
        window.addEventListener('touchend', () => { isSliding = false; });
        window.addEventListener('touchmove', (e) => {
            if (!isSliding) return;
            updateSliderPos(e.touches[0].clientX);
        });
    }

    // -------------------------------------------------------------
    // 5. Scroll Reveal — brings existing content to life on scroll.
    // Uses the .animate-on-scroll / .is-visible system already
    // defined in styles/animations.css. Exposed on window so
    // scripts that render content after DOMContentLoaded (project
    // cards, project-detail chips) can call it again on new nodes.
    // -------------------------------------------------------------
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const revealIO = (!prefersReducedMotion && 'IntersectionObserver' in window)
        ? new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    revealIO.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' })
        : null;

    const REVEAL_SELECTORS = [
        '.section-heading-block',
        '.about-bio-text',
        '.philosophy-callout-card',
        '.tilt-card-item',
        '.workflow-step',
        '.service-dark-card',
        '.pricing-plan-card',
        '.cert-perspective-card',
        '.contact-card-box',
        '.stat-cell',
        '.timeline-station',
        '.meta-sheet-card',
        '.editorial-project-card'
    ].join(', ');

    const initScrollReveal = (root) => {
        const scope = root || document;
        scope.querySelectorAll(REVEAL_SELECTORS).forEach((el) => {
            if (el.classList.contains('animate-on-scroll') || el.classList.contains('is-visible')) return;
            el.classList.add('animate-on-scroll');
            const parent = el.parentElement;
            const siblingIndex = parent ? Array.from(parent.children).indexOf(el) % 6 : 0;
            el.style.transitionDelay = (siblingIndex * 90) + 'ms';
            if (revealIO) {
                revealIO.observe(el);
            } else {
                el.classList.add('is-visible');
            }
        });
    };

    window.ScrollReveal = { init: initScrollReveal };
    // Deferred to window 'load' (not DOMContentLoaded) so image loading has
    // already settled layout — observing too early can make below-fold
    // elements register as "in view" before late-loading images push them down.
    if (document.readyState === 'complete') {
        initScrollReveal(document);
    } else {
        window.addEventListener('load', () => initScrollReveal(document));
    }

    // -------------------------------------------------------------
    // 6. Interactive Freelance Package Estimator
    // -------------------------------------------------------------
    const areaSlider = document.getElementById('estimator-area-slider');
    const areaValDisplay = document.getElementById('estimator-area-val');
    const chips = document.querySelectorAll('.estimator-chip');
    const durationDisplay = document.getElementById('estimator-duration-display');
    const savingsDisplay = document.getElementById('estimator-savings-display');
    const estimatorWaBtn = document.getElementById('estimator-whatsapp-btn');

    if (areaSlider && areaValDisplay) {
        const calculateEstimate = () => {
            const area = parseInt(areaSlider.value);
            areaValDisplay.textContent = `${area.toLocaleString()} m²`;

            const activeChips = Array.from(chips).filter(c => c.classList.contains('active'));
            const count = activeChips.length || 1;

            // Turnaround calculation
            let days = Math.ceil((area / 15000) * 3 + count * 2);
            if (days < 4) days = 4;

            // Cost optimization projection
            const estSavingMillion = ((area * 180 * 0.08) / 1000000).toFixed(1);

            const isAr = document.documentElement.getAttribute('lang') === 'ar';
            if (durationDisplay) {
                durationDisplay.textContent = `${days} ${isAr ? 'أيام عمل' : 'Work Days'}`;
            }
            if (savingsDisplay) {
                savingsDisplay.textContent = `~ SAR ${estSavingMillion}M`;
            }

            if (estimatorWaBtn) {
                const serviceNames = activeChips.map(c => c.getAttribute('data-service')).join(', ');
                const msg = `Hello Eng. Mostafa, I used your MEP Package Estimator for project area: ${area.toLocaleString()} m², Scope: [${serviceNames}], Projected Turnaround: ${days} days. Let's discuss pricing!`;
                estimatorWaBtn.href = `https://wa.me/966502582122?text=${encodeURIComponent(msg)}`;
            }
        };

        areaSlider.addEventListener('input', calculateEstimate);

        chips.forEach(chip => {
            chip.addEventListener('click', () => {
                chip.classList.toggle('active');
                calculateEstimate();
            });
        });

        calculateEstimate();
    }
});
