/**
 * Animations and Visual Effects for Eng. Mostafa Portfolio
 * Features: Scroll Observer, Parallax, Particle Canvas, Skill Bars, Timelines
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. & 2. & 3. Animate On Scroll, Skill Bars, Timeline
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                
                // General animate on scroll
                el.classList.add('is-visible');

                // Stagger children
                const staggerChildren = el.querySelectorAll('.stagger-children > *');
                if (staggerChildren.length > 0) {
                    staggerChildren.forEach((child, index) => {
                        child.style.transitionDelay = `${index * 0.15}s`;
                        child.classList.add('is-visible');
                    });
                }

                // Skill Bars Fill
                if (el.classList.contains('skill-bar')) {
                    const fill = el.querySelector('.skill-fill');
                    if (fill) {
                        const percentage = fill.getAttribute('data-percentage');
                        fill.style.width = percentage + '%';
                    }
                }

                // Section Title Underline Expand (trigger CSS class)
                if (el.classList.contains('section-title')) {
                    el.classList.add('animate-underline');
                }
                
                // Stop observing once animated (optional, ensures it only runs once)
                // observer.unobserve(el);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-on-scroll, .skill-bar, .timeline-item, .section-title');
    animatedElements.forEach(el => scrollObserver.observe(el));

    // 5. Parallax Effect
    const parallaxElements = document.querySelectorAll('.parallax');
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        parallaxElements.forEach(el => {
            const speed = el.getAttribute('data-speed') || 0.5;
            const yPos = -(scrolled * speed);
            el.style.transform = `translateY(${yPos}px)`;
        });
    });

    // 6. Hero Particles (Canvas)
    const initParticles = () => {
        const container = document.getElementById('particles-container');
        if (!container) return;

        const canvas = document.createElement('canvas');
        container.appendChild(canvas);
        const ctx = canvas.getContext('2d');

        let width, height;
        const particles = [];
        const particleCount = 80;

        const resize = () => {
            width = container.clientWidth;
            height = container.clientHeight;
            canvas.width = width;
            canvas.height = height;
        };

        window.addEventListener('resize', resize);
        resize();

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.radius = Math.random() * 2 + 1;
                this.vx = (Math.random() - 0.5) * 0.5;
                this.vy = (Math.random() - 1) * 0.5; // floating upward mainly
                this.opacity = Math.random() * 0.5 + 0.1;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                // Wrap around
                if (this.x < 0) this.x = width;
                if (this.x > width) this.x = 0;
                if (this.y < 0) this.y = height;
                if (this.y > height) this.y = 0;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(196, 163, 90, ${this.opacity})`; // Gold color: #C4A35A
                ctx.fill();
            }
        }

        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }

        const connectParticles = () => {
            for (let a = 0; a < particles.length; a++) {
                for (let b = a; b < particles.length; b++) {
                    const dx = particles[a].x - particles[b].x;
                    const dy = particles[a].y - particles[b].y;
                    const distance = Math.hypot(dx, dy);

                    if (distance < 100) {
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(196, 163, 90, ${0.2 - distance / 500})`;
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(particles[a].x, particles[a].y);
                        ctx.lineTo(particles[b].x, particles[b].y);
                        ctx.stroke();
                    }
                }
            }
        };

        const animate = () => {
            ctx.clearRect(0, 0, width, height);
            
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            
            connectParticles();
            requestAnimationFrame(animate);
        };

        animate();
    };

    initParticles();

    // 7. Smooth Reveal for Hero Elements (Load effect)
    setTimeout(() => {
        const heroElements = document.querySelectorAll('.hero-reveal');
        heroElements.forEach((el, idx) => {
            setTimeout(() => {
                el.classList.add('is-visible');
            }, idx * 200);
        });
    }, 100);
});
