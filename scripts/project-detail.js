/**
 * Project Detail & Gallery Showcase Page Controller (project-detail.html)
 * Dynamically loads and renders full project details, high-res interactive gallery,
 * Lightbox viewer, MEP scope breakdown, stakeholders, and pagination.
 */

document.addEventListener('DOMContentLoaded', () => {
    if (typeof PROJECTS_DATA === 'undefined') return;

    // 1. Get Project ID from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    let projectId = urlParams.get('id');

    // Default to first project if not specified or not found
    let project = PROJECTS_DATA.find(p => p.id === projectId);
    if (!project) {
        project = PROJECTS_DATA[0];
        projectId = project.id;
    }

    const currentIndex = PROJECTS_DATA.findIndex(p => p.id === project.id);
    const prevProject = PROJECTS_DATA[(currentIndex - 1 + PROJECTS_DATA.length) % PROJECTS_DATA.length];
    const nextProject = PROJECTS_DATA[(currentIndex + 1) % PROJECTS_DATA.length];

    let currentPhotoIndex = 0;
    const isAr = document.documentElement.getAttribute('lang') === 'ar';

    // 2. Render Page Content
    const renderProjectDetails = () => {
        const lang = document.documentElement.getAttribute('lang') || 'en';
        const isArabic = lang === 'ar';

        // Titles & Meta
        document.title = `${isArabic ? project.titleAr : project.titleEn} — Eng. Mostafa Abdelghany`;
        
        const titleEl = document.getElementById('project-detail-title');
        if (titleEl) titleEl.textContent = isArabic ? project.titleAr : project.titleEn;

        const breadcrumbEl = document.getElementById('project-breadcrumb-title');
        if (breadcrumbEl) breadcrumbEl.textContent = isArabic ? project.titleAr : project.titleEn;

        const sectorEl = document.getElementById('project-detail-sector');
        if (sectorEl) sectorEl.textContent = isArabic ? project.sectorAr : project.sectorEn;

        const companyEl = document.getElementById('project-detail-company');
        if (companyEl) companyEl.textContent = isArabic ? project.companyAr : project.companyEn;

        const periodEl = document.getElementById('project-detail-period');
        if (periodEl) periodEl.textContent = isArabic ? project.periodAr : project.period;

        const locationEl = document.getElementById('project-detail-location');
        if (locationEl) locationEl.textContent = isArabic ? project.locationAr : project.locationEn;

        const valueEl = document.getElementById('project-detail-value');
        if (valueEl) valueEl.textContent = isArabic ? (project.valueAr || 'N/A') : (project.valueEn || 'N/A');

        const clientEl = document.getElementById('project-detail-client');
        if (clientEl) clientEl.textContent = isArabic ? (project.clientAr || 'N/A') : (project.clientEn || 'N/A');

        const roleEl = document.getElementById('project-detail-role');
        if (roleEl) roleEl.textContent = isArabic ? project.roleAr : project.roleEn;

        // Description
        const descEl = document.getElementById('project-detail-desc');
        if (descEl) descEl.textContent = isArabic ? project.descriptionAr : project.descriptionEn;

        // 3. Render MEP Scope Breakdown
        const scopeContainer = document.getElementById('project-mep-scope-container');
        if (scopeContainer && project.mepScope) {
            scopeContainer.innerHTML = '';
            project.mepScope.forEach(item => {
                const card = document.createElement('div');
                card.style.cssText = `
                    background: rgba(10, 25, 47, 0.6);
                    border: 1px solid rgba(196, 163, 90, 0.2);
                    border-radius: var(--radius-sm);
                    padding: 20px;
                    margin-bottom: 16px;
                `;
                card.innerHTML = `
                    <h4 style="color: var(--gold-primary); font-size: 1.1rem; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
                        <i class="fas fa-check-circle" style="color: var(--accent-teal);"></i>
                        ${isArabic ? item.nameAr : item.nameEn}
                    </h4>
                    <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.6; margin: 0;">
                        ${isArabic ? (item.descAr || item.descEn) : item.descEn}
                    </p>
                `;
                scopeContainer.appendChild(card);
            });
        }

        // 4. Render Stakeholders List
        const stakeholdersContainer = document.getElementById('project-stakeholders-container');
        if (stakeholdersContainer && project.stakeholders) {
            stakeholdersContainer.innerHTML = '';
            project.stakeholders.forEach(st => {
                const item = document.createElement('div');
                item.style.cssText = `
                    padding: 12px 16px;
                    background: rgba(196, 163, 90, 0.06);
                    border-radius: var(--radius-sm);
                    margin-bottom: 10px;
                    border: 1px solid rgba(196, 163, 90, 0.15);
                `;
                item.innerHTML = `
                    <div style="font-size: 0.78rem; color: var(--gold-light); text-transform: uppercase; font-weight: 600;">
                        ${isArabic ? st.roleAr : st.roleEn}
                    </div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: var(--text-primary); margin-top: 2px;">
                        ${st.name}
                    </div>
                `;
                stakeholdersContainer.appendChild(item);
            });
        }

        // 5. Pagination Buttons
        const prevBtn = document.getElementById('prev-project-btn');
        if (prevBtn) {
            prevBtn.href = `project-detail.html?id=${prevProject.id}`;
            const prevTitle = isArabic ? prevProject.titleAr : prevProject.titleEn;
            prevBtn.querySelector('.proj-btn-label').textContent = `${isArabic ? 'المشروع السابق:' : 'Previous:'} ${prevTitle}`;
        }

        const nextBtn = document.getElementById('next-project-btn');
        if (nextBtn) {
            nextBtn.href = `project-detail.html?id=${nextProject.id}`;
            const nextTitle = isArabic ? nextProject.titleAr : nextProject.titleEn;
            nextBtn.querySelector('.proj-btn-label').textContent = `${isArabic ? 'المشروع التالي:' : 'Next:'} ${nextTitle}`;
        }
    };

    // 6. Interactive Gallery Logic
    const mainImg = document.getElementById('gallery-main-img');
    const thumbsContainer = document.getElementById('gallery-thumbs-container');
    const prevPhotoBtn = document.getElementById('gallery-prev-btn');
    const nextPhotoBtn = document.getElementById('gallery-next-btn');
    const fullscreenBtn = document.getElementById('gallery-fullscreen-btn');
    const lightboxModal = document.getElementById('lightbox-modal');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxClose = document.getElementById('lightbox-close-btn');

    const updateGalleryPhoto = (index) => {
        if (!project.images || project.images.length === 0) return;
        currentPhotoIndex = (index + project.images.length) % project.images.length;
        const photoSrc = project.images[currentPhotoIndex];

        if (mainImg) {
            mainImg.style.opacity = '0';
            setTimeout(() => {
                mainImg.src = photoSrc;
                mainImg.style.opacity = '1';
            }, 150);
        }

        if (thumbsContainer) {
            const allThumbs = thumbsContainer.querySelectorAll('.gallery-thumb');
            allThumbs.forEach((thumb, i) => {
                thumb.classList.toggle('active', i === currentPhotoIndex);
            });
        }
    };

    // Render Thumbnails
    if (thumbsContainer && project.images) {
        thumbsContainer.innerHTML = '';
        project.images.forEach((imgSrc, idx) => {
            const thumb = document.createElement('div');
            thumb.className = `gallery-thumb ${idx === 0 ? 'active' : ''}`;
            thumb.innerHTML = `<img src="${imgSrc}" alt="${project.titleEn} Thumbnail ${idx + 1}" loading="lazy">`;
            thumb.addEventListener('click', () => updateGalleryPhoto(idx));
            thumbsContainer.appendChild(thumb);
        });
    }

    if (prevPhotoBtn) prevPhotoBtn.addEventListener('click', () => updateGalleryPhoto(currentPhotoIndex - 1));
    if (nextPhotoBtn) nextPhotoBtn.addEventListener('click', () => updateGalleryPhoto(currentPhotoIndex + 1));

    // Lightbox modal trigger
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

    if (fullscreenBtn) fullscreenBtn.addEventListener('click', openLightbox);
    if (mainImg) mainImg.addEventListener('click', openLightbox);
    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    if (lightboxModal) {
        lightboxModal.addEventListener('click', (e) => {
            if (e.target === lightboxModal) closeLightbox();
        });
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowRight') updateGalleryPhoto(currentPhotoIndex + 1);
        if (e.key === 'ArrowLeft') updateGalleryPhoto(currentPhotoIndex - 1);
    });

    // Initial setup
    renderProjectDetails();
    updateGalleryPhoto(0);

    // Language change listener
    window.addEventListener('languageChanged', renderProjectDetails);
});
