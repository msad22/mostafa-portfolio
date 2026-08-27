/**
 * Projects Hub Page Script (projects.html)
 * Dynamically renders all 14 projects using high-end editorial cards,
 * handles live search, country pills, and seamless navigation to project-detail.html?id=...
 */

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('projects-grid-container');
    const searchInput = document.getElementById('project-search');
    const countryPills = document.querySelectorAll('#country-pills .filter-pill');

    if (!container || typeof PROJECTS_DATA === 'undefined') return;

    let activeCountry = 'all';
    let searchQuery = '';

    const renderProjects = () => {
        const isAr = document.documentElement.getAttribute('lang') === 'ar';
        container.innerHTML = '';

        const filtered = PROJECTS_DATA.filter(p => {
            // Country filter
            if (activeCountry !== 'all' && p.category !== activeCountry) return false;
            // Search filter
            if (searchQuery.trim() !== '') {
                const q = searchQuery.toLowerCase();
                const matchEn = (p.titleEn + ' ' + p.companyEn + ' ' + p.locationEn + ' ' + p.sectorEn + ' ' + p.descriptionEn).toLowerCase();
                const matchAr = (p.titleAr + ' ' + p.companyAr + ' ' + p.locationAr + ' ' + p.sectorAr + ' ' + p.descriptionAr).toLowerCase();
                if (!matchEn.includes(q) && !matchAr.includes(q)) return false;
            }
            return true;
        });

        if (filtered.length === 0) {
            container.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 80px 20px; color: var(--ink-dim);">
                    <i class="fas fa-search" style="font-size: 2.5rem; color: var(--accent); margin-bottom: 16px;"></i>
                    <h3 style="color: var(--ink); margin-bottom: 8px;">${isAr ? 'لم يتم العثور على مشاريع مطابقة' : 'No matching projects found'}</h3>
                    <p style="font-size: 0.9rem;">${isAr ? 'جرب البحث بكلمات أخرى أو تغيير الدولة' : 'Try adjusting your search criteria or country filter'}</p>
                </div>
            `;
            return;
        }

        filtered.forEach((p, idx) => {
            const title = isAr ? p.titleAr : p.titleEn;
            const company = isAr ? p.companyAr : p.companyEn;
            const location = isAr ? p.locationAr : p.locationEn;
            const value = isAr ? (p.valueAr || '') : (p.valueEn || '');
            const isFlagship = idx === 0 && activeCountry === 'all' && searchQuery === '';

            const card = document.createElement('a');
            card.href = `project-detail.html?id=${p.id}`;
            card.className = `editorial-project-card ${isFlagship ? 'editorial-card-flagship' : 'editorial-card-standard'}`;
            
            card.innerHTML = `
                <div class="editorial-img-box">
                    <img src="${p.coverImage}" alt="${title}" loading="lazy">
                    <div class="editorial-card-scrim"></div>
                </div>
                <div class="editorial-card-content">
                    <span class="label" style="color:var(--accent);">${company} ${value ? '· ' + value : ''}</span>
                    <h3 class="editorial-card-title">${title}</h3>
                    <span class="editorial-card-location">${location} · ${p.images.length} ${isAr ? 'صور موثقة' : 'Photos'}</span>
                </div>
            `;

            container.appendChild(card);
        });

        if (window.ScrollReveal) window.ScrollReveal.init(container);
    };

    // Initial render
    renderProjects();

    // Re-render on language change
    window.addEventListener('languageChanged', renderProjects);

    // Country pill click
    countryPills.forEach(pill => {
        pill.addEventListener('click', () => {
            countryPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            activeCountry = pill.getAttribute('data-filter');
            renderProjects();
        });
    });

    // Search input listener
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            searchQuery = e.target.value;
            renderProjects();
        });
    }
});

/**
 * Home page "Featured Projects" preview grid (index.html).
 * Renders the featured:true entries so real project photos and
 * results are visible while scrolling the home page, instead of
 * living only behind the Projects nav tab.
 */
document.addEventListener('DOMContentLoaded', () => {
    const homeGrid = document.getElementById('home-featured-projects-grid');
    if (!homeGrid || typeof PROJECTS_DATA === 'undefined') return;

    const renderHomeFeatured = () => {
        const isAr = document.documentElement.getAttribute('lang') === 'ar';
        homeGrid.innerHTML = '';

        PROJECTS_DATA.filter(p => p.featured).forEach((p, idx) => {
            const title = isAr ? p.titleAr : p.titleEn;
            const company = isAr ? p.companyAr : p.companyEn;
            const location = isAr ? p.locationAr : p.locationEn;
            const value = isAr ? (p.valueAr || '') : (p.valueEn || '');

            const card = document.createElement('a');
            card.href = `project-detail.html?id=${p.id}`;
            card.className = `editorial-project-card ${idx === 0 ? 'editorial-card-flagship' : 'editorial-card-standard'}`;
            card.innerHTML = `
                <div class="editorial-img-box">
                    <img src="${p.coverImage}" alt="${title}" loading="lazy">
                    <div class="editorial-card-scrim"></div>
                </div>
                <div class="editorial-card-content">
                    <span class="label" style="color:var(--accent);">${company} ${value ? '· ' + value : ''}</span>
                    <h3 class="editorial-card-title">${title}</h3>
                    <span class="editorial-card-location">${location}</span>
                </div>
            `;
            homeGrid.appendChild(card);
        });

        if (window.ScrollReveal) window.ScrollReveal.init(homeGrid);
    };

    renderHomeFeatured();
    window.addEventListener('languageChanged', renderHomeFeatured);
});
