/**
 * Interactive Leaflet Map for Project Locations
 * Features: Dark CartoDB Tiles, Custom Gold SVG Markers, Hover Popups,
 *           Smooth Region Fly-to, and Bi-directional Synchronization with Project Tabs
 */

window.addEventListener('load', () => {
    const mapContainer = document.getElementById('project-map');
    if (!mapContainer || typeof L === 'undefined') return;

    // 1. Initialize Map centered between KSA and Egypt
    const map = L.map('project-map', {
        scrollWheelZoom: false,
        zoomControl: true,
        attributionControl: false
    }).setView([26.0, 39.0], 5);

    // Dark tiles from CartoDB
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        subdomains: 'abcd',
        maxZoom: 19
    }).addTo(map);

    // 2. Project Locations Data (14 Projects)
    const projects = [
        // KSA Projects (Riyadh)
        { id: 1, name: 'King Abdullah International Gardens (KAIG)', nameAr: 'حدائق الملك عبدالله الدولية', lat: 24.7136, lng: 46.6753, value: 'SAR 2.63 Billion', company: 'Zaid Al Hussain Group', year: '2024 — Present', category: 'ksa', featured: true },
        { id: 2, name: 'Riyadh Metro Project', nameAr: 'مشروع مترو الرياض', lat: 24.7236, lng: 46.6953, value: '', company: 'EDC Expertise', year: '2016 — 2017', category: 'ksa' },
        { id: 3, name: 'Radisson Blu Hotel', nameAr: 'فندق راديسون بلو الرياض', lat: 24.7336, lng: 46.6553, value: '', company: 'EDC Expertise', year: '2018', category: 'ksa' },
        { id: 4, name: 'Hilton Riyadh Hotel & Residences', nameAr: 'فندق هيلتون الرياض', lat: 24.6936, lng: 46.7053, value: '', company: 'EDC Expertise', year: '2018', category: 'ksa' },
        { id: 5, name: 'King Fahd Medical City', nameAr: 'مدينة الملك فهد الطبية', lat: 24.6636, lng: 46.7153, value: '', company: 'EDC Expertise', year: '2017', category: 'ksa' },
        { id: 6, name: 'Haifa Compound', nameAr: 'مجمع حيفا السكني', lat: 24.7436, lng: 46.7253, value: '', company: 'EDC Expertise', year: '2017', category: 'ksa' },

        // Egypt Projects
        { id: 7, name: 'Noor City Mega Compound', nameAr: 'مدينة نور (مجموعة طلعت مصطفى)', lat: 30.0200, lng: 31.7600, value: 'Mega Project', company: 'Atrium (Talaat Moustafa Group)', year: '2023 — 2024', category: 'egypt', featured: true },
        { id: 8, name: 'Zewail City of Science & Technology', nameAr: 'مدينة زويل للعلوم والتكنولوجيا', lat: 30.0131, lng: 30.9806, value: '', company: 'Hassan Allam Construction', year: '2019', category: 'egypt' },
        { id: 9, name: 'Aeon Towers (20 Floors)', nameAr: 'أبراج إيون (20 طابق)', lat: 30.0231, lng: 30.9706, value: '', company: 'Hassan Allam Construction', year: '2020 — 2021', category: 'egypt' },
        { id: 10, name: 'Egypt International Exhibition Center', nameAr: 'مركز مصر الدولي للمعارض', lat: 30.0350, lng: 31.4700, value: '', company: 'Hassan Allam Construction', year: '2016', category: 'egypt' },
        { id: 11, name: 'Berenice Civil Airport', nameAr: 'مطار برنيس المدني', lat: 23.9631, lng: 35.4688, value: '', company: 'Hassan Allam Construction', year: '2019', category: 'egypt' },
        { id: 12, name: 'Berenice Military Air Base', nameAr: 'قاعدة برنيس الجوية العسكرية', lat: 23.9531, lng: 35.4588, value: '', company: 'Pillars Construction', year: '2020', category: 'egypt' },
        { id: 13, name: 'Zagazig University Campus', nameAr: 'حرم جامعة الزقازيق', lat: 30.5877, lng: 31.5020, value: '', company: 'Pillars Construction', year: '2023', category: 'egypt' },
        { id: 14, name: 'La Verde Compound', nameAr: 'كمبوند لا فيردي بالعاصمة الإدارية', lat: 30.0100, lng: 31.7500, value: '', company: 'Pillars Construction', year: '2021 — 2022', category: 'egypt' }
    ];

    const markers = [];

    // 3. Create Circle Markers with Gold Styling
    projects.forEach(p => {
        const marker = L.circleMarker([p.lat, p.lng], {
            radius: p.featured ? 10 : 7,
            fillColor: '#C4A35A',
            color: '#FFFFFF',
            weight: p.featured ? 3 : 1.5,
            opacity: 0.9,
            fillOpacity: 0.9
        });

        // Popup Content
        const createPopupContent = () => {
            const isAr = document.documentElement.getAttribute('lang') === 'ar';
            const title = isAr ? p.nameAr : p.name;
            return `
                <div style="font-family: 'Inter', 'Cairo', sans-serif; min-width: 180px; padding: 4px;">
                    <div style="font-weight: 700; color: #C4A35A; font-size: 13px; margin-bottom: 4px;">${title}</div>
                    <div style="color: #E6F1FF; font-size: 11px; margin-bottom: 2px;">🏢 ${p.company}</div>
                    <div style="color: #8892B0; font-size: 11px;">📅 ${p.year}</div>
                    ${p.value ? `<div style="color: #64FFDA; font-weight: 600; font-size: 11px; margin-top: 4px;">💰 ${p.value}</div>` : ''}
                </div>
            `;
        };

        marker.bindPopup(createPopupContent(), {
            closeButton: false,
            className: 'custom-dark-popup'
        });

        // Hover events
        marker.on('mouseover', function () {
            this.setPopupContent(createPopupContent());
            this.openPopup();
        });
        marker.on('mouseout', function () {
            this.closePopup();
        });

        // Click to trigger project modal or scroll to card
        marker.on('click', () => {
            const card = document.querySelector(`.project-card[data-id="${p.id}"]`);
            if (card) {
                card.scrollIntoView({ behavior: 'smooth', block: 'center' });
                card.click();
            }
        });

        marker.category = p.category;
        markers.push(marker);
        marker.addTo(map);
    });

    // 4. Invalidate size when container enters view
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(() => map.invalidateSize(), 150);
            }
        });
    }, { threshold: 0.1 });
    observer.observe(mapContainer);

    // 5. Global Filter Functionality
    window.filterMapMarkers = function(category) {
        markers.forEach(marker => {
            if (category === 'all' || marker.category === category) {
                if (!map.hasLayer(marker)) map.addLayer(marker);
            } else {
                if (map.hasLayer(marker)) map.removeLayer(marker);
            }
        });

        // Sync Map Filter Buttons
        const mapFilterBtns = document.querySelectorAll('.map-filter-btn');
        mapFilterBtns.forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-filter') === category);
        });

        // Region Fly-To
        if (category === 'ksa') {
            map.flyTo([24.7136, 46.6753], 9, { duration: 1.5 });
        } else if (category === 'egypt') {
            map.flyTo([29.0, 32.0], 6, { duration: 1.5 });
        } else {
            map.flyTo([26.0, 39.0], 5, { duration: 1.5 });
        }
    };

    // 6. Map filter buttons event listeners
    const mapFilterBtns = document.querySelectorAll('.map-filter-btn');
    mapFilterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const category = e.currentTarget.getAttribute('data-filter');
            window.filterMapMarkers(category);

            // Sync with main project filter tabs
            const mainFilterTab = document.querySelector(`.filter-tab[data-filter="${category}"]`);
            if (mainFilterTab) {
                document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
                mainFilterTab.classList.add('active');

                // Filter cards in projects section
                document.querySelectorAll('.project-card').forEach(card => {
                    const cardCat = card.getAttribute('data-category');
                    if (category === 'all' || cardCat === category) {
                        card.classList.remove('hide');
                    } else {
                        card.classList.add('hide');
                    }
                });
            }
        });
    });
});
