/**
 * Project Detail & Gallery Showcase Page Controller (project-detail.html)
 * Dynamically loads and renders full project details, high-res interactive gallery,
 * Lightbox viewer, and WhatsApp scope inquiry.
 */

document.addEventListener('DOMContentLoaded', () => {
    if (typeof PROJECTS_DATA === 'undefined') return;

    // 1. Get Project ID from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    let projectId = urlParams.get('id');

    let project = PROJECTS_DATA.find(p => p.id === projectId);
    if (!project) {
        project = PROJECTS_DATA[0];
        projectId = project.id;
    }

    let currentPhotoIndex = 0;

    // 2. Render Page Content
    const renderProjectDetails = () => {
        const lang = document.documentElement.getAttribute('lang') || 'en';
        const isAr = lang === 'ar';

        const title = isAr ? project.titleAr : project.titleEn;
        const location = isAr ? project.locationAr : project.locationEn;
        const company = isAr ? project.companyAr : project.companyEn;
        const period = isAr ? project.periodAr : project.period;
        const value = isAr ? (project.valueAr || 'N/A') : (project.valueEn || 'N/A');
        const client = isAr ? (project.clientAr || 'Private / Gov') : (project.clientEn || 'Private / Gov');
        const consultant = isAr ? (project.consultantAr || 'Lead Consultant') : (project.consultantEn || 'Lead Consultant');
        const role = isAr ? project.roleAr : project.roleEn;
        const summary = isAr ? project.descriptionAr : project.descriptionEn;

        document.title = `${title} — Eng. Mostafa Abdelghany`;

        const titleEl = document.getElementById('proj-detail-title');
        if (titleEl) titleEl.textContent = title;

        const locEl = document.getElementById('proj-detail-location');
        if (locEl) locEl.textContent = `${location} · ${company}`;

        const valBadge = document.getElementById('proj-value-badge');
        if (valBadge) valBadge.textContent = value;

        const empEl = document.getElementById('proj-employer');
        if (empEl) empEl.textContent = company;

        const clientEl = document.getElementById('proj-client');
        if (clientEl) clientEl.textContent = client;

        const consEl = document.getElementById('proj-consultant');
        if (consEl) consEl.textContent = consultant;

        const periodEl = document.getElementById('proj-period');
        if (periodEl) periodEl.textContent = period;

        const roleEl = document.getElementById('proj-role');
        if (roleEl) roleEl.textContent = role;

        const sumEl = document.getElementById('proj-summary-text');
        if (sumEl) sumEl.textContent = summary;

        // Scope Chips
        const chipsBox = document.getElementById('proj-scope-chips');
        if (chipsBox && project.mepScope) {
            chipsBox.innerHTML = '';
            project.mepScope.forEach(s => {
                const chip = document.createElement('span');
                chip.className = 'scope-chip';
                chip.textContent = isAr ? s.nameAr : s.nameEn;
                chipsBox.appendChild(chip);
            });
        }

        // WhatsApp Inquire Button
        const inqBtn = document.getElementById('inquire-project-btn');
        if (inqBtn) {
            const waText = `Hello Eng. Mostafa, I am inquiring about your experience on project: ${project.titleEn} (${value}).`;
            inqBtn.href = `https://wa.me/966502582122?text=${encodeURIComponent(waText)}`;
        }
    };

    // 3. Interactive Gallery Logic
    const mainImg = document.getElementById('main-viewer-img');
    const mainBox = document.getElementById('main-image-box');
    const thumbsTrack = document.getElementById('thumbnails-track');
    const prevBtn = document.getElementById('gallery-prev');
    const nextBtn = document.getElementById('gallery-next');
    const lightboxModal = document.getElementById('lightbox-modal');
    const lightboxImg = document.getElementById('lightbox-full-img');
    const lightboxClose = document.getElementById('lightbox-close');

    const updatePhoto = (idx) => {
        if (!project.images || project.images.length === 0) return;
        currentPhotoIndex = (idx + project.images.length) % project.images.length;
        const src = project.images[currentPhotoIndex];

        if (mainImg) {
            mainImg.src = src;
        }

        if (thumbsTrack) {
            const allThumbs = thumbsTrack.querySelectorAll('.thumb-item');
            allThumbs.forEach((th, i) => {
                th.classList.toggle('active', i === currentPhotoIndex);
            });
        }
    };

    // Render Thumbnails
    if (thumbsTrack && project.images) {
        thumbsTrack.innerHTML = '';
        project.images.forEach((imgSrc, idx) => {
            const th = document.createElement('div');
            th.className = `thumb-item ${idx === 0 ? 'active' : ''}`;
            th.innerHTML = `<img src="${imgSrc}" alt="Thumbnail ${idx + 1}" loading="lazy">`;
            th.addEventListener('click', () => updatePhoto(idx));
            thumbsTrack.appendChild(th);
        });
    }

    if (prevBtn) prevBtn.addEventListener('click', (e) => { e.stopPropagation(); updatePhoto(currentPhotoIndex - 1); });
    if (nextBtn) nextBtn.addEventListener('click', (e) => { e.stopPropagation(); updatePhoto(currentPhotoIndex + 1); });

    // Lightbox modal
    const openLightbox = () => {
        if (!lightboxModal || !project.images) return;
        lightboxImg.src = project.images[currentPhotoIndex];
        lightboxModal.classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    const closeLightbox = () => {
        if (!lightboxModal) return;
        lightboxModal.classList.remove('active');
        document.body.style.overflow = 'auto';
    };

    if (mainBox) mainBox.addEventListener('click', openLightbox);
    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    if (lightboxModal) {
        lightboxModal.addEventListener('click', (e) => {
            if (e.target === lightboxModal) closeLightbox();
        });
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowRight') updatePhoto(currentPhotoIndex + 1);
        if (e.key === 'ArrowLeft') updatePhoto(currentPhotoIndex - 1);
    });

    renderProjectDetails();
    updatePhoto(0);

    window.addEventListener('languageChanged', renderProjectDetails);
});
