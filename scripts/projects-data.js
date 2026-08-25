/**
 * Comprehensive Database of all 14 Projects for Eng. Mostafa Abdelghany
 * Includes multi-image galleries, Arabic/English bilingual data, MEP scope, and stakeholders.
 */

const PROJECTS_DATA = [
    {
        id: "kaig",
        num: 1,
        titleEn: "King Abdullah International Gardens (KAIG)",
        titleAr: "حدائق الملك عبدالله الدولية (KAIG)",
        category: "ksa",
        sector: "infrastructure",
        sectorEn: "Mega Infrastructure & Landscape",
        sectorAr: "بنية تحتية ومناظر طبيعية عملاقة",
        companyEn: "Zaid Al Hussain Group",
        companyAr: "مجموعة زيد الحصين",
        roleEn: "MEP Procurement Section Head",
        roleAr: "رئيس قسم مشتريات أعمال MEP",
        period: "Oct 2024 — Present",
        periodAr: "أكتوبر 2024 — حتى الآن",
        locationEn: "Riyadh, Saudi Arabia",
        locationAr: "الرياض، المملكة العربية السعودية",
        valueEn: "SAR 2.63 Billion",
        valueAr: "2.63 مليار ريال سعودي",
        clientEn: "Riyadh Municipality (أمانة منطقة الرياض)",
        clientAr: "أمانة منطقة الرياض",
        featured: true,
        coverImage: "assets/images/projects/kaig_6.jpg",
        images: [
            "assets/images/projects/kaig_1.jpg",
            "assets/images/projects/kaig_2.jpg",
            "assets/images/projects/kaig_3.jpg",
            "assets/images/projects/kaig_4.jpg",
            "assets/images/projects/kaig_5.jpg",
            "assets/images/projects/kaig_6.jpg",
            "assets/images/projects/kaig_7.jpg"
        ],
        stakeholders: [
            { roleEn: "Client", roleAr: "المالك", name: "Riyadh Municipality" },
            { roleEn: "Masterplanner", roleAr: "المخطط العام", name: "Barton Willmore" },
            { roleEn: "Structural & Civil Engineering", roleAr: "الاستشاري الإنشائي والمدني", name: "Buro Happold" },
            { roleEn: "Technical Review & Validation", roleAr: "المراجعة والاعتماد الفني", name: "Dar Al-Handasah (دار الهندسة)" },
            { roleEn: "Supervision Consultant", roleAr: "استشاري الإشراف", name: "Omrania & Egis Group" }
        ],
        descriptionEn: "One of the most ambitious eco-tourism and botanical mega-projects in the world, spanning over 2.1 million square meters in Riyadh. The project features massive bioclimatic domes, aviary structures, wadi walkways, and advanced sustainable MEP systems. Eng. Mostafa leads the entire MEP procurement section, managing multi-million SAR packages across HVAC, electrical distribution, advanced water treatment, pumping stations, and specialized environmental control systems.",
        descriptionAr: "واحد من أضخم المشاريع البيئية والسياحية في العالم بمساحة تتجاوز 2.1 مليون متر مربع بالرياض. يضم قباباً نباتية ومناخية عملاقة، ومسارات وادي طبيعية، وشبكات MEP مستدامة متقدمة. يقود المهندس مصطفى قسم مشتريات الـ MEP بالكامل للمشروع، متولياً إدارة حزم تعاقدية ضخمة لأنظمة التكييف المركزي، وشبكات الجهد المتوسط والمنخفض، ومحطات المعالجة والضخ، وأنظمة التحكم البيئي الدقيقة.",
        mepScope: [
            { nameEn: "HVAC Systems", nameAr: "أنظمة التكييف والتهوية", descEn: "Chilled water systems, air handling units, and climatic dome thermal regulation." },
            { nameEn: "Electrical Networks", nameAr: "الشبكات الكهربائية", descEn: "Medium & Low Voltage substations, diesel generators, and architectural lighting." },
            { nameEn: "Plumbing & Irrigation", nameAr: "السباكة والري المركزي", descEn: "Advanced automated irrigation networks, water feature pumps, and filtration systems." },
            { nameEn: "Fire Life Safety", nameAr: "مكافحة الحريق والسلامة", descEn: "Addressable fire alarm, deluge systems, and automated foam fire suppression." }
        ]
    },
    {
        id: "noor-city",
        num: 2,
        titleEn: "Noor City Mega Compound",
        titleAr: "مشروع مدينة نور العملاق (مجموعة طلعت مصطفى)",
        category: "egypt",
        sector: "compounds",
        sectorEn: "Mega Smart City & Residential",
        sectorAr: "مدينة ذكية وتطوير سكني عملاق",
        companyEn: "Atrium Quality Contractors (Talaat Moustafa Group)",
        companyAr: "شركة أتريوم (مجموعة طلعت مصطفى)",
        roleEn: "Procurement Team Lead",
        roleAr: "رئيس فريق المشتريات",
        period: "2023 — 2024",
        periodAr: "2023 — 2024",
        locationEn: "New Administrative Capital, Egypt",
        locationAr: "العاصمة الإدارية الجديدة، مصر",
        valueEn: "Multi-Billion EGP Mega City",
        valueAr: "مشروع مدينة متكاملة بمليارات الجنيهات",
        clientEn: "Talaat Moustafa Group (TMG)",
        clientAr: "مجموعة طلعت مصطفى للتطوير العقاري",
        featured: true,
        coverImage: "assets/images/projects/noor_city_1.jpg",
        images: [
            "assets/images/projects/noor_city_1.jpg",
            "assets/images/projects/noor_city_2.jpeg",
            "assets/images/projects/noor_city_3.jpeg",
            "assets/images/projects/noor_city_4.jpg",
            "assets/images/projects/noor_city_5.jpg",
            "assets/images/projects/noor_city_6.jpg"
        ],
        stakeholders: [
            { roleEn: "Developer & Client", roleAr: "المطور والمالك", name: "Talaat Moustafa Group" },
            { roleEn: "Main Contractor", roleAr: "المقاول الرئيسي", name: "Atrium Quality Contractors" }
        ],
        descriptionEn: "Noor City is a state-of-the-art 5,000-acre smart city in Egypt's Capital region. Eng. Mostafa led the MEP procurement team, managing high-volume supply chains for residential buildings, commercial infrastructure, power stations, and integrated utility networks.",
        descriptionAr: "مدينة نور هي أول مدينة ذكية خضراء متكاملة على مساحة 5000 فدان بشرق القاهرة. قاد المهندس مصطفى فريق مشتريات الـ MEP لإدارة وتأمين توريدات المشروعات السكنية والبنية التحتية والمحطات الكهربائية ومرافق الخدمات الذكية.",
        mepScope: [
            { nameEn: "Substation Packages", nameAr: "حزم محطات المحولات", descEn: "Procurement of transformers, RMUs, and main distribution switchboards." },
            { nameEn: "Water & Sewage Networks", nameAr: "شبكات المياه والصرف", descEn: "HDPE/UPVC piping networks, booster pump packages, and storm drainage." },
            { nameEn: "Smart City Infrastructure", nameAr: "البنية التحتية الذكية", descEn: "Fiber optic conduits, smart metering, and automated building management." }
        ]
    },
    {
        id: "aeon-towers",
        num: 3,
        titleEn: "Aeon Towers (20 Floors High-Rise)",
        titleAr: "أبراج إيون السكنية الفاخرة (20 طابق)",
        category: "egypt",
        sector: "highrise",
        sectorEn: "Luxury High-Rise Residential",
        sectorAr: "أبراج سكنية شاهقة فاخرة",
        companyEn: "Hassan Allam Construction",
        companyAr: "شركة حسن علام للإنشاءات",
        roleEn: "Procurement Engineer",
        roleAr: "مهندس مشتريات",
        period: "2020 — 2021",
        periodAr: "2020 — 2021",
        locationEn: "6th of October City, Giza, Egypt",
        locationAr: "مدينة السادس من أكتوبر، الجيزة، مصر",
        valueEn: "High-Rise Luxury Development",
        valueAr: "مشروع أبراج فندقية وسكنية فاخرة",
        clientEn: "Marakez Real Estate Development",
        clientAr: "شركة مراكز للاستثمار العقاري",
        featured: true,
        coverImage: "assets/images/projects/aeon_towers_1.jpeg",
        images: [
            "assets/images/projects/aeon_towers_1.jpeg",
            "assets/images/projects/aeon_towers_2.jpeg",
            "assets/images/projects/aeon_towers_3.jpeg",
            "assets/images/projects/aeon_towers_4.jpeg"
        ],
        stakeholders: [
            { roleEn: "Developer", roleAr: "المطور", name: "Marakez" },
            { roleEn: "Main Contractor", roleAr: "المقاول الرئيسي", name: "Hassan Allam Construction" }
        ],
        descriptionEn: "The first 20-story high-rise towers in 6th of October city. Procured specialized MEP packages required for high-rise buildings including high-pressure booster systems, VRV/VRF air conditioning, high-speed elevator power feeds, and pressurized stairwell fans.",
        descriptionAr: "أول أبراج سكنية شاهقة بارتفاع 20 طابقاً في مدينة 6 أكتوبر. تولى المهندس مصطفى شراء حزم أنظمة الأبراج العالية من محطات الرفع الهيدروليكية، وأنظمة التكييف VRF/VRV، ومصادر التغذية للمصاعد فائقة السرعة، ومراوح ضغط سلالم الهروب.",
        mepScope: [
            { nameEn: "High-Rise HVAC", nameAr: "تكييف الأبراج الشاهقة", descEn: "VRV multi-split systems with centralized energy management." },
            { nameEn: "Hydraulic Booster Stations", nameAr: "محطات ضخ المياه المضغوطة", descEn: "Multi-stage booster sets with VFD controllers." }
        ]
    },
    {
        id: "zewail-city",
        num: 4,
        titleEn: "Zewail City of Science and Technology",
        titleAr: "مدينة زويل للعلوم والتكنولوجيا",
        category: "egypt",
        sector: "education",
        sectorEn: "Educational & Research Campus",
        sectorAr: "حرم جامعي وبحثي علمي عالمي",
        companyEn: "Hassan Allam Construction",
        companyAr: "شركة حسن علام للإنشاءات",
        roleEn: "Procurement Engineer",
        roleAr: "مهندس مشتريات",
        period: "2019",
        periodAr: "2019",
        locationEn: "6th of October City, Egypt",
        locationAr: "مدينة 6 أكتوبر، مصر",
        valueEn: "National Strategic Project",
        valueAr: "مشروع قومي استراتيجي",
        clientEn: "Zewail City of Science and Technology Foundation",
        clientAr: "مؤسسة مدينة زويل للعلوم والتكنولوجيا",
        featured: true,
        coverImage: "assets/images/projects/zewail_city_1.jpg",
        images: [
            "assets/images/projects/zewail_city_1.jpg",
            "assets/images/projects/zewail_city_2.webp",
            "assets/images/projects/zewail_city_3.jpeg",
            "assets/images/projects/zewail_city_4.jpg"
        ],
        stakeholders: [
            { roleEn: "Client", roleAr: "المالك", name: "Zewail City Foundation" },
            { roleEn: "Contractor", roleAr: "المقاول", name: "Hassan Allam Construction" }
        ],
        descriptionEn: "State-of-the-art research institute and university campus founded by Nobel Laureate Dr. Ahmed Zewail. Procured specialized laboratory MEP utilities, cleanroom HVAC filtration, precision power backup UPS systems, and chemical waste drainage networks.",
        descriptionAr: "صرح بحثي وأكاديمي متقدم أسسه العالم الراحل د. أحمد زويل. شملت المهام شراء حزم المعامل المتخصصة، وأنظمة تهوية وتنقية الهواء للغرف النقية (Cleanrooms)، وشبكات تصريف الكيماويات ومحطات الـ UPS المركزية.",
        mepScope: [
            { nameEn: "Lab Utilities", nameAr: "مرافق المعامل التخصصية", descEn: "Special gases piping, chemical-resistant drainage, and clean air supply." }
        ]
    },
    {
        id: "zagazig-uni",
        num: 5,
        titleEn: "Zagazig University Campus & Substation",
        titleAr: "حرم جامعة الزقازيق ومحطة المحولات الكهربائية",
        category: "egypt",
        sector: "education",
        sectorEn: "Educational & Electrical Substation",
        sectorAr: "منشآت تعليمية ومحطة محولات كبرى",
        companyEn: "Pillars Construction",
        companyAr: "شركة بيلرز للإنشاءات",
        roleEn: "Senior Procurement Engineer",
        roleAr: "مهندس مشتريات أول",
        period: "2023",
        periodAr: "2023",
        locationEn: "Sharqia Governorate, Egypt",
        locationAr: "محافظة الشرقية، مصر",
        valueEn: "Major Educational Expansion",
        valueAr: "توسعات جامعية كبرى",
        clientEn: "Zagazig University",
        clientAr: "جامعة الزقازيق",
        featured: false,
        coverImage: "assets/images/projects/zagazig_uni_1.jpeg",
        images: [
            "assets/images/projects/zagazig_uni_1.jpeg",
            "assets/images/projects/zagazig_uni_2.jpg",
            "assets/images/projects/zagazig_uni_3.jpg",
            "assets/images/projects/zagazig_uni_4.jpg"
        ],
        stakeholders: [
            { roleEn: "Client", roleAr: "المالك", name: "Zagazig University" },
            { roleEn: "Contractor", roleAr: "المقاول", name: "Pillars Construction" }
        ],
        descriptionEn: "Extensive campus facility expansions including lecture complexes, faculty buildings, and dedicated high-capacity electrical transformer stations.",
        descriptionAr: "إنشاء وتجهيز مبانٍ تعليمية ومدرجات كبرى مع محطة محولات كهربائية متكاملة لتغذية الحرم الجامعي بالكامل.",
        mepScope: [
            { nameEn: "Power Substation", nameAr: "محطة المحولات الكهربائية", descEn: "Procurement of MV transformers, switchgear panels, and underground feeder cables." }
        ]
    },
    {
        id: "hilton-riyadh",
        num: 6,
        titleEn: "Hilton Riyadh Hotel & Residences",
        titleAr: "فندق وأجنحة هيلتون الرياض",
        category: "ksa",
        sector: "hospitality",
        sectorEn: "5-Star Luxury Hospitality",
        sectorAr: "فندقة وضيافة عالمية 5 نجوم",
        companyEn: "EDC Expertise",
        companyAr: "شركة EDC للخبرات والمقاولات",
        roleEn: "Junior Procurement Engineer",
        roleAr: "مهندس مشتريات مبتدئ",
        period: "2018",
        periodAr: "2018",
        locationEn: "Riyadh, Saudi Arabia",
        locationAr: "الرياض، المملكة العربية السعودية",
        valueEn: "Luxury Hospitality Project",
        valueAr: "مشروع فندقي عالمي",
        clientEn: "Hilton Worldwide / Private Investment",
        clientAr: "مجموعة هيلتون العالمية",
        featured: false,
        coverImage: "assets/images/projects/hilton_riyadh_3.jpg",
        images: [
            "assets/images/projects/hilton_riyadh_1.webp",
            "assets/images/projects/hilton_riyadh_2.avif",
            "assets/images/projects/hilton_riyadh_3.jpg",
            "assets/images/projects/hilton_riyadh_4.jpg"
        ],
        stakeholders: [
            { roleEn: "Operator", roleAr: "المشغل العالمي", name: "Hilton Worldwide" },
            { roleEn: "Contractor", roleAr: "المقاول", name: "EDC Expertise" }
        ],
        descriptionEn: "High-end luxury hotel and serviced apartments in Riyadh. Managed procurement submittals for acoustic HVAC equipment, guest room automation, sanitary fixtures, and emergency power systems meeting stringent Hilton brand standards.",
        descriptionAr: "فندق وأجنحة فندقية فاخرة في الرياض وفق أعلى معايير هيلتون العالمية لأنظمة الصوتيات المعزولة للتكييف، والأنظمة الكهربائية والتحكم الذكي بالغرف.",
        mepScope: [
            { nameEn: "Hospitality MEP", nameAr: "أنظمة الفنادق المتطورة", descEn: "Low-noise FCUs, guest room management systems (GRMS), and specialized plumbing." }
        ]
    },
    {
        id: "riyadh-metro",
        num: 7,
        titleEn: "Riyadh Metro Transit Network",
        titleAr: "شبكة قطار الرياض (مترو الرياض)",
        category: "ksa",
        sector: "infrastructure",
        sectorEn: "Transit & Mega Transportation",
        sectorAr: "بنية تحتية ونقل عملاق",
        companyEn: "EDC Expertise",
        companyAr: "شركة EDC للخبرات والمقاولات",
        roleEn: "Junior Procurement Engineer",
        roleAr: "مهندس مشتريات مبتدئ",
        period: "2016 — 2017",
        periodAr: "2016 — 2017",
        locationEn: "Riyadh, Saudi Arabia",
        locationAr: "الرياض، المملكة العربية السعودية",
        valueEn: "World's Largest Transit Project",
        valueAr: "أضخم مشروع نقل عام في العالم",
        clientEn: "Royal Commission for Riyadh City (RCRC)",
        clientAr: "الهيئة الملكية لمدينة الرياض",
        featured: false,
        coverImage: "assets/images/projects/riyadh_metro_1.jpg",
        images: [
            "assets/images/projects/riyadh_metro_1.jpg",
            "assets/images/projects/riyadh_metro_2.jpg",
            "assets/images/projects/riyadh_metro_3.webp"
        ],
        stakeholders: [
            { roleEn: "Client", roleAr: "المالك", name: "Royal Commission for Riyadh City" },
            { roleEn: "Contractor", roleAr: "المقاول", name: "EDC Expertise" }
        ],
        descriptionEn: "Procurement coordination for metro station MEP packages, tunnel ventilation support utilities, platform drainage, and emergency power distribution across assigned metro line sectors.",
        descriptionAr: "المشاركة في تنسيق وإدارة مشتريات محطات المترو من أنظمة تهوية الأنفاق، وشبكات الصرف والتغذية، وأنظمة الإنارة ومصادر الطاقة الاحتياطية.",
        mepScope: [
            { nameEn: "Station Infrastructure", nameAr: "مرافق المحطات", descEn: "Heavy-duty pumps, tunnel dampers, smoke extract fans, and durable conduits." }
        ]
    },
    {
        id: "radisson-riyadh",
        num: 8,
        titleEn: "Radisson Blu Hotel Riyadh",
        titleAr: "فندق راديسون بلو الرياض",
        category: "ksa",
        sector: "hospitality",
        sectorEn: "Hospitality & Corporate Suites",
        sectorAr: "ضيافة وفندقة عالمية",
        companyEn: "EDC Expertise",
        companyAr: "شركة EDC للخبرات والمقاولات",
        roleEn: "Junior Procurement Engineer",
        roleAr: "مهندس مشتريات مبتدئ",
        period: "2018",
        periodAr: "2018",
        locationEn: "Riyadh, Saudi Arabia",
        locationAr: "الرياض، المملكة العربية السعودية",
        valueEn: "International Hotel Brand",
        valueAr: "فندق سياحي دولي",
        clientEn: "Radisson Hotel Group",
        clientAr: "مجموعة فنادق راديسون",
        featured: false,
        coverImage: "assets/images/projects/radisson_riyadh_1.jpg",
        images: [
            "assets/images/projects/radisson_riyadh_1.jpg"
        ],
        stakeholders: [
            { roleEn: "Operator", roleAr: "المشغل", name: "Radisson Hotel Group" }
        ],
        descriptionEn: "Procurement of specialized MEP hotel fixtures, central water heating boilers, decorative lighting, and fire pump rooms.",
        descriptionAr: "شراء وتوريد مستلزمات الفندق من غلايات المياه المركزية، ووحدات الإضاءة الديكورية، ومحطات إطفاء الحريق المعتمدة.",
        mepScope: [
            { nameEn: "Hotel Utilities", nameAr: "مرافق الفندق", descEn: "Central boilers, water softening plants, and luxury sanitary fittings." }
        ]
    },
    {
        id: "berenice-airport",
        num: 9,
        titleEn: "Berenice Civil Airport",
        titleAr: "مطار برنيس المدني الدولي",
        category: "egypt",
        sector: "aviation",
        sectorEn: "Aviation & Terminal Infrastructure",
        sectorAr: "مطارات وبنية تحتية للملاحة الجوية",
        companyEn: "Hassan Allam Construction",
        companyAr: "شركة حسن علام للإنشاءات",
        roleEn: "Procurement Engineer",
        roleAr: "مهندس مشتريات",
        period: "2019",
        periodAr: "2019",
        locationEn: "Red Sea Governorate, Egypt",
        locationAr: "محافظة البحر الأحمر، مصر",
        valueEn: "International Airport Project",
        valueAr: "مشروع مطار دولي استراتيجي",
        clientEn: "Egyptian Airports Company / Ministry of Civil Aviation",
        clientAr: "الشركة المصرية للمطارات / وزارة الطيران المدني",
        featured: false,
        coverImage: "assets/images/projects/berenice_airport_1.jpeg",
        images: [
            "assets/images/projects/berenice_airport_1.jpeg"
        ],
        stakeholders: [
            { roleEn: "Authority", roleAr: "الجهة المالكة", name: "Egyptian Airports Company" },
            { roleEn: "Main Contractor", roleAr: "المقاول الرئيسي", name: "Hassan Allam Construction" }
        ],
        descriptionEn: "Procurement of terminal building MEP systems, apron lighting supplies, runway drainage, and emergency backup generator systems in a remote coastal environment.",
        descriptionAr: "شراء أنظمة مبنى الركاب وصالات الوصول، وشبكات إنارة المهبط والممرات، ومحطات المولدات الاحتياطية في بيئة ساحلية نائية.",
        mepScope: [
            { nameEn: "Aviation Utilities", nameAr: "مرافق الطيران", descEn: "Corrosion-resistant terminal HVAC, runway drainage, and airfield ground lighting power feeds." }
        ]
    },
    {
        id: "egyptian-space-agency",
        num: 10,
        titleEn: "Egypt International Exhibition Center / Space Agency",
        titleAr: "مركز مصر الدولي للمعارض / وكالة الفضاء المصرية",
        category: "egypt",
        sector: "infrastructure",
        sectorEn: "Exhibition Halls & Government Facilities",
        sectorAr: "قاعات مؤتمرات ومنشآت حكومية سيادية",
        companyEn: "Hassan Allam Construction",
        companyAr: "شركة حسن علام للإنشاءات",
        roleEn: "Procurement Engineer",
        roleAr: "مهندس مشتريات",
        period: "2016",
        periodAr: "2016",
        locationEn: "New Cairo, Egypt",
        locationAr: "القاهرة الجديدة، مصر",
        valueEn: "National Landmark Project",
        valueAr: "صرح معارض ومؤتمرات كبرى",
        clientEn: "Egyptian Armed Forces Engineering Authority",
        clientAr: "الهيئة الهندسية للقوات المسلحة",
        featured: false,
        coverImage: "assets/images/projects/egyptian_space_agency_1.jpeg",
        images: [
            "assets/images/projects/egyptian_space_agency_1.jpeg"
        ],
        stakeholders: [
            { roleEn: "Authority", roleAr: "الجهة المشرفة", name: "Engineering Authority" },
            { roleEn: "Contractor", roleAr: "المقاول", name: "Hassan Allam Construction" }
        ],
        descriptionEn: "Large-span exhibition halls requiring industrial-scale HVAC ductwork, high-bay LED lighting arrays, and heavy-duty floor power utility boxes.",
        descriptionAr: "قاعات معارض دولية ضخمة تطلبت شراء شبكات تكييف صناعية عملاقة، وإضاءة LED معلقة للاسقف العالية، ونقاط تغذية كهربائية أرضية مجهزة.",
        mepScope: [
            { nameEn: "Large Span MEP", nameAr: "أنظمة الصالات الكبرى", descEn: "Rooftop package AC units, high-bay lighting, and centralized smoke evacuation." }
        ]
    },
    {
        id: "king-fahd-medical-city",
        num: 11,
        titleEn: "King Fahd Medical City Expansion",
        titleAr: "توسعات مدينة الملك فهد الطبية",
        category: "ksa",
        sector: "healthcare",
        sectorEn: "Healthcare & Specialized Medical Units",
        sectorAr: "رعاية صحية ومستشفيات متخصصة",
        companyEn: "EDC Expertise",
        companyAr: "شركة EDC للخبرات والمقاولات",
        roleEn: "Junior Procurement Engineer",
        roleAr: "مهندس مشتريات مبتدئ",
        period: "2017",
        periodAr: "2017",
        locationEn: "Riyadh, Saudi Arabia",
        locationAr: "الرياض، المملكة العربية السعودية",
        valueEn: "Healthcare Infrastructure",
        valueAr: "مرافق ومستشفيات طبية",
        clientEn: "Ministry of Health, KSA",
        clientAr: "وزارة الصحة السعودية",
        featured: false,
        coverImage: "assets/images/project_5.jpg",
        images: [
            "assets/images/project_5.jpg"
        ],
        stakeholders: [
            { roleEn: "Client", roleAr: "المالك", name: "Ministry of Health, KSA" }
        ],
        descriptionEn: "Procurement of specialized healthcare MEP infrastructure, medical gas pipes, isolated power panels (IPS) for operating rooms, and HEPA air filtration.",
        descriptionAr: "شراء أنظمة المستشفيات الحساسة وغازات التخدير والغازات الطبية، واللوحات الكهربائية المعزولة لغرف العمليات وفلاتر HEPA.",
        mepScope: [
            { nameEn: "Medical MEP", nameAr: "أنظمة الرعاية الصحية", descEn: "Medical gas pipelines, surgical room clean air, and emergency power sync panels." }
        ]
    },
    {
        id: "haifa-compound",
        num: 12,
        titleEn: "Haifa Residential Compound",
        titleAr: "مجمع حيفا السكني الراقي",
        category: "ksa",
        sector: "compounds",
        sectorEn: "Residential Gated Compound",
        sectorAr: "مجمع سكني راقٍ متكامل",
        companyEn: "EDC Expertise",
        companyAr: "شركة EDC للخبرات والمقاولات",
        roleEn: "Junior Procurement Engineer",
        roleAr: "مهندس مشتريات مبتدئ",
        period: "2017",
        periodAr: "2017",
        locationEn: "Riyadh, Saudi Arabia",
        locationAr: "الرياض، المملكة العربية السعودية",
        valueEn: "Gated Residential Community",
        valueAr: "مجمع سكني مغلق",
        clientEn: "Private Real Estate Developer",
        clientAr: "مطور عقاري خاص",
        featured: false,
        coverImage: "assets/images/project_6.jpg",
        images: [
            "assets/images/project_6.jpg"
        ],
        stakeholders: [
            { roleEn: "Contractor", roleAr: "المقاول", name: "EDC Expertise" }
        ],
        descriptionEn: "Luxury villas and recreational clubhouses procurement including smart home automation, swimming pool filtration, and energy-efficient heat pumps.",
        descriptionAr: "مشتريات الفلل الفاخرة ومرافق النوادي السكنية من أنظمة المسابح والمضخات الحرارية والإنارة الذكية.",
        mepScope: [
            { nameEn: "Residential MEP", nameAr: "أنظمة سكنية فاخرة", descEn: "Central domestic water heaters, booster pumps, and underground LV distribution." }
        ]
    },
    {
        id: "berenice-military",
        num: 13,
        titleEn: "Berenice Military Air Base Facilities",
        titleAr: "منشآت قاعدة برنيس العسكرية",
        category: "egypt",
        sector: "aviation",
        sectorEn: "Military & Defense Infrastructure",
        sectorAr: "منشآت عسكرية ودفاعية استراتيجية",
        companyEn: "Pillars Construction",
        companyAr: "شركة بيلرز للإنشاءات",
        roleEn: "Senior Procurement Engineer",
        roleAr: "مهندس مشتريات أول",
        period: "2020",
        periodAr: "2020",
        locationEn: "Red Sea Governorate, Egypt",
        locationAr: "محافظة البحر الأحمر، مصر",
        valueEn: "Strategic Defense Project",
        valueAr: "مشروع دفاعي واستراتيجي",
        clientEn: "Engineering Authority of the Armed Forces",
        clientAr: "الهيئة الهندسية للقوات المسلحة",
        featured: false,
        coverImage: "assets/images/project_12.jpg",
        images: [
            "assets/images/project_12.jpg"
        ],
        stakeholders: [
            { roleEn: "Client", roleAr: "المالك", name: "Armed Forces" },
            { roleEn: "Contractor", roleAr: "المقاول", name: "Pillars Construction" }
        ],
        descriptionEn: "Procurement of ruggedized, high-durability MEP systems, blast-resistant dampers, specialized fuel pumping networks, and resilient electrical networks.",
        descriptionAr: "شراء أنظمة الخدمة الشاقة ومضخات الوقود ودمبرات مقاومة الانفجارات وشبكات التغذية الكهربائية الآمنة.",
        mepScope: [
            { nameEn: "Defense Infrastructure", nameAr: "مرافق دفاعية", descEn: "Fuel transfer pumps, secure power distribution, and reinforced HVAC." }
        ]
    },
    {
        id: "la-verde",
        num: 14,
        titleEn: "La Verde Compound",
        titleAr: "كمبوند لا فيردي بالعاصمة الإدارية",
        category: "egypt",
        sector: "compounds",
        sectorEn: "Luxury Residential & Commercial",
        sectorAr: "مجمع سكني وتجاري فاخر",
        companyEn: "Pillars Construction",
        companyAr: "شركة بيلرز للإنشاءات",
        roleEn: "Senior Procurement Engineer",
        roleAr: "مهندس مشتريات أول",
        period: "2021 — 2022",
        periodAr: "2021 — 2022",
        locationEn: "New Administrative Capital, Egypt",
        locationAr: "العاصمة الإدارية الجديدة، مصر",
        valueEn: "Luxury Residential Community",
        valueAr: "مجمع سكني فاخر",
        clientEn: "La Verde Developments",
        clientAr: "شركة لافيردي للتطوير العقاري",
        featured: false,
        coverImage: "assets/images/project_14.jpg",
        images: [
            "assets/images/project_14.jpg"
        ],
        stakeholders: [
            { roleEn: "Developer", roleAr: "المطور", name: "La Verde Developments" },
            { roleEn: "Contractor", roleAr: "المقاول", name: "Pillars Construction" }
        ],
        descriptionEn: "High-end Spanish-inspired residential compound in the New Administrative Capital. Managed procurement for HVAC systems, architectural water features, and energy-saving lighting networks.",
        descriptionAr: "كمبوند سكني فاخر بالطراز الأندلسي في العاصمة الإدارية. شملت المهام شراء حزم التكييف وشبكات المياه والبحيرات الصناعية ووحدات الإضاءة الموفرة للطاقة.",
        mepScope: [
            { nameEn: "Compound Utilities", nameAr: "مرافق المجمع", descEn: "Concealed AC units, automated irrigation, landscape lighting, and fire pump sets." }
        ]
    }
];

// Export to window object
if (typeof window !== 'undefined') {
    window.PROJECTS_DATA = PROJECTS_DATA;
}
