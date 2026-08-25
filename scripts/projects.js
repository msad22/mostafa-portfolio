/**
 * Projects Hub Page Script (projects.html)
 * Dynamically renders all 14 projects, handles live search, country filter,
 * sector pills, and seamless navigation to project-detail.html?id=...
 */

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('projects-grid-container');
    const searchInput = document.getElementById('project-search-input');
    const countryTabs = document.querySelectorAll('.filter-tab[data-filter]');
    const sectorPills = document.querySelectorAll('.sector-pill[data-sector]');
    const resultsCountEl = document.getElementById('projects-count-display');

    if (!container || typeof PROJECTS_DATA === 'undefined') return;

    let activeCountry = 'all';
    let activeSector = 'all';
    let searchQuery = '';

    const renderProjects = () => {
        const isAr = document.documentElement.getAttribute('lang') === 'ar';
        container.innerHTML = '';

        const filtered = PROJECTS_DATA.filter(p => {
            // Country filter
            if (activeCountry !== 'all' && p.category !== activeCountry) return false;
            // Sector filter
            if (activeSector !== 'all' && p.sector !== activeSector) return false;
            // Search filter
            if (searchQuery.trim() !== '') {
                const q = searchQuery.toLowerCase();
                const matchEn = (p.titleEn + ' ' + p.companyEn + ' ' + p.locationEn + ' ' + p.sectorEn + ' ' + p.descriptionEn).toLowerCase();
                const matchAr = (p.titleAr + ' ' + p.companyAr + ' ' + p.locationAr + ' ' + p.sectorAr + ' ' + p.descriptionAr).toLowerCase();
                if (!matchEn.includes(q) && !matchAr.includes(q)) return false;
            }
            return true;
        });

        if (resultsCountEl) {
            resultsCountEl.textContent = filtered.length;
        }

        if (filtered.length === 0) {
            container.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; color: var(--text-secondary);">
                    <i class="fas fa-search" style="font-size: 3rem; color: var(--gold-primary); margin-bottom: 15px;"></i>
                    <h3 style="color: var(--text-primary); margin-bottom: 8px;">${isAr ? 'لم يتم العثور على مشاريع' : 'No projects found'}</h3>
                    <p>${isAr ? 'جرب البحث بكلمات أخرى أو اختر قطاعاً مختلفاً' : 'Try adjusting your search criteria or filter options'}</p>
                </div>
            `;
            return;
        }

        filtered.forEach(p => {
            const title = isAr ? p.titleAr : p.titleEn;
            const company = isAr ? p.companyAr : p.companyEn;
            const sector = isAr ? p.sectorAr : p.sectorEn;
            const period = isAr ? p.periodAr : p.period;
            const location = isAr ? p.locationAr : p.locationEn;
            const value = isAr ? (p.valueAr || '') : (p.valueEn || '');
            const role = isAr ? p.roleAr : p.roleEn;

            const card = document.createElement('div');
            card.className = `project-card ${p.featured ? 'featured' : ''} animate-on-scroll is-visible`;
            card.innerHTML = `
                <div class="card-image">
                    <img src="${p.coverImage}" alt="${title}" loading="lazy">
                    <div class="card-overlay"></div>
                    ${p.featured ? `<span class="card-badge featured-badge">${isAr ? 'مشروع ريادي' : 'Flagship Project'}</span>` : ''}
                    <span class="card-country"><i class="fas fa-flag"></i> ${p.category.toUpperCase()}</span>
                </div>
                <div class="card-content">
                    <div class="card-accent"></div>
                    <div style="font-size: 0.75rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">${sector}</div>
                    <h3 class="card-title">${title}</h3>
                    <p class="card-company"><i class="fas fa-building"></i> ${company}</p>
                    <div class="card-meta">
                        <span><i class="fas fa-calendar"></i> ${period}</span>
                        <span><i class="fas fa-map-marker-alt"></i> ${location}</span>
                    </div>
                    ${value ? `<div class="card-value">${value}</div>` : ''}
                </div>
                <div class="card-hover-info">
                    <p class="hover-role">${role}</p>
                    <p class="hover-client">${isAr ? 'عدد الصور المتاحة:' : 'Available photos:'} ${p.images.length} 📸</p>
                    <a href="project-detail.html?id=${p.id}" class="btn-view-details">
                        <span>${isAr ? 'عرض تفاصيل المشروع الكاملة والجاليري' : 'View Full Details & Gallery'}</span>
                        <i class="fas fa-arrow-right"></i>
                    </a>
                </div>
            `;

            // Card click to navigate
            card.addEventListener('click', (e) => {
                // Avoid double trigger if clicking link directly
                if (e.target.tagName !== 'A') {
                    window.location.href = `project-detail.html?id=${p.id}`;
                }
            });

            container.appendChild(card);
        });
    };

    // Initial render
    renderProjects();

    // Re-render on language change
    window.addEventListener('languageChanged', renderProjects);

    // Country tab click
    countryTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            countryTabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            activeCountry = tab.getAttribute('data-filter');
            renderProjects();
        });
    });

    // Sector pills click
    sectorPills.forEach(pill => {
        pill.addEventListener('click', () => {
            sectorPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            activeSector = pill.getAttribute('data-sector');
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
