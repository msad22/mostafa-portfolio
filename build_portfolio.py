<!DOCTYPE html>
<html lang="en" dir="ltr" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mostafa Abdelghany | MEP Procurement Section Head</title>
<meta name="description" content="Mostafa Abdelghany - MEP Procurement Section Head in Riyadh. 12+ years of engineering leadership across SAR 2.63B Vision 2030 mega-projects in KSA & Egypt.">

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">

<!-- FontAwesome Icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

<!-- Leaflet GIS Map CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />

<style>
/* =========================================================
   DESIGN SYSTEM - EXECUTIVE OBSIDIAN & ELECTRIC GLOW PALETTE
   ========================================================= */
:root {
  --bg-primary: #07090e;
  --bg-secondary: #0d121d;
  --bg-surface: #121927;
  --bg-surface-hover: #1a2438;
  --border-color: #1e293b;
  --border-color-light: #334155;
  
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-dark: #64748b;
  
  --accent-cyan: #00f2fe;
  --accent-emerald: #10b981;
  --accent-emerald-dark: #059669;
  --accent-gold: #f59e0b;
  --accent-glow: rgba(0, 242, 254, 0.15);
  
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 24px;
  --radius-full: 9999px;
  
  --transition-fast: 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-normal: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 0 25px rgba(16, 185, 129, 0.2);
}

:root[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-secondary: #f1f5f9;
  --bg-surface: #ffffff;
  --bg-surface-hover: #f8fafc;
  --border-color: #e2e8f0;
  --border-color-light: #cbd5e1;
  
  --text-main: #0f172a;
  --text-muted: #475569;
  --text-dark: #64748b;
  
  --accent-cyan: #0284c7;
  --accent-emerald: #059669;
  --accent-emerald-dark: #047857;
  --accent-gold: #d97706;
  --accent-glow: rgba(2, 132, 199, 0.12);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  background-color: var(--bg-primary);
  color: var(--text-main);
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  line-height: 1.6;
}

html[dir="rtl"] body {
  font-family: 'Tajawal', 'Segoe UI', Tahoma, sans-serif;
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb { background: var(--border-color-light); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent-emerald); }

/* Selection */
::selection { background: var(--accent-emerald); color: #000; }

/* Dynamic Background Glow */
.bg-grid-overlay {
  position: fixed;
  inset: 0;
  background-image: radial-gradient(rgba(16, 185, 129, 0.06) 1px, transparent 1px);
  background-size: 32px 32px;
  pointer-events: none;
  z-index: 0;
}

.bg-blur-glow-1 {
  position: fixed;
  top: -10%;
  right: 10%;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(0, 242, 254, 0.08) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.bg-blur-glow-2 {
  position: fixed;
  bottom: 10%;
  left: 20%;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(16, 185, 129, 0.07) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

/* =========================================================
   TOP EXECUTIVE STICKY GLASS HEADER (NO SIDEBAR GAP)
   ========================================================= */
.top-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(13, 18, 29, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-color);
  padding: 12px 30px;
  transition: var(--transition-fast);
}

.header-container {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.brand-identity {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
}

.profile-avatar-header {
  position: relative;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid var(--accent-emerald);
  box-shadow: 0 0 15px rgba(16, 185, 129, 0.3);
  flex-shrink: 0;
}

.profile-avatar-header img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.brand-info h1 {
  font-size: 16px;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.2;
}

.brand-info p {
  font-size: 11px;
  font-weight: 700;
  color: var(--accent-emerald);
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.header-nav {
  display: flex;
  align-items: center;
  gap: 6px;
}

.nav-link-btn {
  padding: 8px 14px;
  border-radius: var(--radius-full);
  text-decoration: none;
  color: var(--text-muted);
  font-size: 13px;
  font-weight: 600;
  transition: var(--transition-fast);
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-link-btn:hover {
  background: var(--bg-surface);
  color: var(--accent-cyan);
}

.nav-link-btn.active {
  background: var(--accent-glow);
  color: var(--accent-emerald);
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.control-btn {
  padding: 8px 14px;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-full);
  color: var(--text-main);
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: var(--transition-fast);
}

.control-btn:hover {
  border-color: var(--accent-emerald);
  color: var(--accent-emerald);
}

.control-btn.active {
  background: var(--accent-emerald);
  color: #000;
  border-color: var(--accent-emerald);
}

.mobile-burger {
  display: none;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-main);
  font-size: 20px;
  width: 42px;
  height: 42px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  align-items: center;
  justify-content: center;
}

/* =========================================================
   MAIN LAYOUT (FULL SCREEN WIDTH - NO GAP)
   ========================================================= */
.main-wrapper {
  position: relative;
  z-index: 1;
  width: 100%;
}

.content-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 30px 80px;
}

.section-block {
  margin-bottom: 60px;
  scroll-margin-top: 90px;
}

.section-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 26px;
  flex-wrap: wrap;
}

.section-header h2 {
  font-size: clamp(26px, 3.2vw, 38px);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--text-main);
  line-height: 1.1;
}

.section-header h2 em {
  font-style: normal;
  background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.section-header p {
  font-size: 14px;
  color: var(--text-muted);
  max-width: 65ch;
  margin-top: 6px;
}

/* Glass Panel Card */
.glass-panel {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 30px;
  box-shadow: var(--shadow-card);
  transition: var(--transition-fast);
}

.glass-panel:hover {
  border-color: var(--border-color-light);
}

/* =========================================================
   HERO BANNER
   ========================================================= */
.hero-banner {
  position: relative;
  background: linear-gradient(135deg, rgba(13, 18, 29, 0.95), rgba(18, 25, 39, 0.98));
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 44px 50px;
  overflow: hidden;
  box-shadow: var(--shadow-card);
}

.hero-banner::before {
  content: '';
  position: absolute;
  top: -20%;
  right: -10%;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(0, 242, 254, 0.12) 0%, transparent 70%);
  pointer-events: none;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 40px;
  align-items: center;
  position: relative;
  z-index: 2;
}

.hero-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border-radius: var(--radius-full);
  background: var(--accent-glow);
  border: 1px solid rgba(0, 242, 254, 0.3);
  color: var(--accent-cyan);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 18px;
}

.hero-title {
  font-size: clamp(32px, 4.2vw, 52px);
  font-weight: 900;
  line-height: 1.08;
  letter-spacing: -0.04em;
  margin-bottom: 18px;
}

.hero-title .gradient-text {
  background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-desc {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
  max-width: 58ch;
  margin-bottom: 28px;
}

.hero-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 26px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, var(--accent-emerald), var(--accent-emerald-dark));
  color: #000;
  font-size: 13px;
  font-weight: 800;
  text-decoration: none;
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);
  transition: var(--transition-fast);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(16, 185, 129, 0.4);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 26px;
  border-radius: var(--radius-full);
  background: var(--bg-surface);
  color: var(--text-main);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  border: 1px solid var(--border-color-light);
  transition: var(--transition-fast);
}

.btn-secondary:hover {
  border-color: var(--accent-cyan);
  color: var(--accent-cyan);
  transform: translateY(-2px);
}

.hero-photo-card {
  position: relative;
  width: 250px;
  height: 250px;
  border-radius: var(--radius-md);
  padding: 6px;
  background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
  box-shadow: var(--shadow-glow);
}

.hero-photo-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: calc(var(--radius-md) - 4px);
}

/* =========================================================
   KPI METRICS GRID
   ========================================================= */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 20px;
}

.kpi-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 24px;
  position: relative;
  overflow: hidden;
  transition: var(--transition-normal);
  border-inline-start: 4px solid var(--accent-emerald);
}

.kpi-card:hover {
  transform: translateY(-4px);
  border-color: var(--accent-emerald);
  box-shadow: var(--shadow-card);
}

.kpi-value {
  font-size: clamp(30px, 3vw, 42px);
  font-weight: 900;
  line-height: 1;
  color: var(--text-main);
  margin-bottom: 8px;
  font-variant-numeric: tabular-nums;
}

.kpi-value small {
  font-size: 0.5em;
  color: var(--accent-emerald);
  margin-inline-start: 4px;
}

.kpi-title {
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent-cyan);
  font-weight: 800;
  margin-bottom: 6px;
}

.kpi-desc {
  font-size: 12px;
  color: var(--text-muted);
  line-height: 1.4;
}

/* =========================================================
   REALISTIC LEAFLET GIS MAP & INTERACTIVE TABS (#footprint)
   ========================================================= */
.map-filter-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.map-country-tabs {
  display: flex;
  gap: 8px;
}

.map-tab-btn {
  padding: 8px 16px;
  border-radius: var(--radius-full);
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-muted);
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition-fast);
}

.map-tab-btn:hover {
  border-color: var(--accent-cyan);
  color: var(--text-main);
}

.map-tab-btn.active {
  background: var(--accent-emerald);
  color: #000;
  border-color: var(--accent-emerald);
}

.map-container-box {
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--border-color);
  height: 520px;
  position: relative;
  box-shadow: var(--shadow-card);
}

#leaflet-map {
  width: 100%;
  height: 100%;
  background: var(--bg-secondary);
}

/* Custom Marker Pin Styling */
.custom-map-pin-ksa {
  width: 24px;
  height: 24px;
  background: var(--accent-gold);
  border: 3px solid #000;
  border-radius: 50%;
  box-shadow: 0 0 20px var(--accent-gold);
  animation: pulse-pin 2s infinite;
}

.custom-map-pin-egypt {
  width: 24px;
  height: 24px;
  background: var(--accent-emerald);
  border: 3px solid #000;
  border-radius: 50%;
  box-shadow: 0 0 20px var(--accent-emerald);
  animation: pulse-pin 2s infinite;
}

@keyframes pulse-pin {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.3); }
}

/* Custom Leaflet Tooltip & Popup */
.leaflet-tooltip {
  background: rgba(18, 25, 39, 0.95) !important;
  color: #fff !important;
  border: 1px solid var(--accent-emerald) !important;
  border-radius: var(--radius-sm) !important;
  padding: 8px 12px !important;
  font-family: inherit !important;
  box-shadow: 0 8px 20px rgba(0,0,0,0.6) !important;
}

.leaflet-popup-content-wrapper {
  background: var(--bg-surface) !important;
  color: var(--text-main) !important;
  border: 1px solid var(--border-color-light) !important;
  border-radius: var(--radius-sm) !important;
  box-shadow: 0 10px 30px rgba(0,0,0,0.7) !important;
  font-family: inherit !important;
}

.leaflet-popup-tip { background: var(--bg-surface) !important; }

.map-popup-card h4 {
  font-size: 15px;
  font-weight: 800;
  color: var(--accent-cyan);
  margin-bottom: 6px;
}

.map-popup-card p {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 4px;
}

.map-popup-card .val {
  font-size: 13px;
  font-weight: 800;
  color: var(--accent-emerald);
  margin-top: 8px;
}

/* =========================================================
   PROJECT GALLERY & FILTERS (#projects)
   ========================================================= */
.filter-tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 26px;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 10px 18px;
  border-radius: var(--radius-full);
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-muted);
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition-fast);
}

.tab-btn:hover {
  background: var(--bg-surface-hover);
  color: var(--text-main);
}

.tab-btn.active {
  background: var(--accent-emerald);
  color: #000;
  border-color: var(--accent-emerald);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 24px;
}

.project-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: var(--transition-normal);
  position: relative;
}

.project-card:hover {
  transform: translateY(-6px);
  border-color: var(--accent-cyan);
  box-shadow: 0 15px 35px -10px rgba(0, 242, 254, 0.15);
}

.project-thumb {
  position: relative;
  height: 210px;
  background: var(--bg-secondary);
  overflow: hidden;
}

.project-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.project-card:hover .project-thumb img {
  transform: scale(1.08);
}

.project-badge {
  position: absolute;
  top: 14px;
  inset-inline-end: 14px;
  padding: 6px 12px;
  border-radius: var(--radius-full);
  background: rgba(7, 9, 14, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--accent-cyan);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.project-content {
  padding: 24px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.project-location {
  font-size: 11px;
  color: var(--accent-gold);
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 8px;
}

.project-title {
  font-size: 18px;
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 10px;
  line-height: 1.3;
}

.project-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 18px;
  flex: 1;
}

.project-meta-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 14px;
  border-top: 1px solid var(--border-color);
  font-size: 12px;
  color: var(--text-dark);
}

.project-meta-row b {
  color: var(--accent-emerald);
}

/* =========================================================
   DOCUMENT VAULT SECTION (#documents)
   ========================================================= */
.doc-vault-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}

.doc-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: relative;
  transition: var(--transition-fast);
}

.doc-card:hover {
  border-color: var(--accent-cyan);
  transform: translateY(-4px);
  box-shadow: var(--shadow-card);
}

.doc-card-header {
  display: flex;
  align-items: center;
  gap: 14px;
}

.doc-icon {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-sm);
  background: var(--accent-glow);
  border: 1px solid rgba(0, 242, 254, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: var(--accent-cyan);
  flex-shrink: 0;
}

.doc-info h4 {
  font-size: 15px;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.3;
}

.doc-info p {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 3px;
}

.doc-actions {
  display: flex;
  gap: 10px;
  margin-top: auto;
}

.btn-doc {
  flex: 1;
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 700;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  transition: var(--transition-fast);
}

.btn-doc-view {
  background: var(--bg-surface-hover);
  color: var(--text-main);
  border: 1px solid var(--border-color-light);
}

.btn-doc-view:hover {
  border-color: var(--accent-emerald);
  color: var(--accent-emerald);
}

.btn-doc-download {
  background: var(--accent-emerald);
  color: #000;
  border: 1px solid var(--accent-emerald);
}

.btn-doc-download:hover {
  background: var(--accent-emerald-dark);
}

/* =========================================================
   SKILLS & COMPETENCY MATRIX
   ========================================================= */
.skills-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 36px;
}

.skill-item { padding: 8px 0; }

.skill-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 8px;
}

.skill-header b {
  font-size: 13px;
  font-weight: 700;
  color: var(--text-main);
}

.skill-header span {
  font-size: 12px;
  font-weight: 800;
  color: var(--accent-emerald);
}

.skill-bar-track {
  height: 6px;
  background: var(--bg-secondary);
  border-radius: var(--radius-full);
  overflow: hidden;
  border: 1px solid var(--border-color);
}

.skill-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-cyan), var(--accent-emerald));
  border-radius: var(--radius-full);
  width: 0%;
  transition: width 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}

/* =========================================================
   NEWS & VISION 2030 SECTION (#news)
   ========================================================= */
.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}

.news-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  transition: var(--transition-fast);
}

.news-card:hover {
  border-color: var(--accent-gold);
  transform: translateY(-4px);
}

.news-date {
  font-size: 11px;
  font-weight: 800;
  color: var(--accent-gold);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.news-card h4 {
  font-size: 16px;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.35;
}

.news-card p {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.6;
}

.news-tag {
  align-self: flex-start;
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  background: rgba(245, 158, 11, 0.15);
  color: var(--accent-gold);
  font-size: 10px;
  font-weight: 800;
}

/* =========================================================
   CONTACT SECTION
   ========================================================= */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.contact-row {
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 14px;
  padding: 16px 0;
  border-bottom: 1px solid var(--border-color);
  align-items: center;
}
.contact-row:last-child { border-bottom: none; }

.contact-row .label {
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-dark);
  font-weight: 800;
}

.contact-row a, .contact-row span.val {
  font-size: 14px;
  color: var(--text-main);
  text-decoration: none;
  font-weight: 600;
  transition: var(--transition-fast);
}

.contact-row a:hover {
  color: var(--accent-emerald);
}

/* Footer */
footer {
  padding-top: 30px;
  margin-top: 40px;
  border-top: 1px solid var(--border-color);
  font-size: 12px;
  color: var(--text-dark);
  text-align: center;
}

/* Responsive Styles */
@media (max-width: 1024px) {
  .header-nav { display: none; }
  .mobile-burger { display: flex; }
  .content-container { padding: 30px 20px 60px; }
  .kpi-grid { grid-template-columns: repeat(2, 1fr); }
  .contact-grid { grid-template-columns: 1fr; }
  .skills-grid { grid-template-columns: 1fr; }
}

@media (max-width: 640px) {
  .hero-banner { padding: 28px 20px; }
  .hero-grid { grid-template-columns: 1fr; text-align: center; }
  .hero-photo-card { margin: 0 auto; width: 200px; height: 200px; }
  .hero-actions { justify-content: center; }
  .kpi-grid { grid-template-columns: 1fr; }
  .projects-grid { grid-template-columns: 1fr; }
  .contact-row { grid-template-columns: 1fr; gap: 4px; }
}
</style>
</head>
<body>

<div class="bg-grid-overlay"></div>
<div class="bg-blur-glow-1"></div>
<div class="bg-blur-glow-2"></div>

<!-- TOP EXECUTIVE STICKY GLASS HEADER -->
<header class="top-header">
  <div class="header-container">
    <a href="#overview" class="brand-identity">
      <div class="profile-avatar-header">
        <img src="assets/images/headshot.jpg" alt="Mostafa Abdelghany">
      </div>
      <div class="brand-info">
        <h1>Mostafa Abdelghany</h1>
        <p data-i="role_sub">MEP Procurement Section Head</p>
      </div>
    </a>

    <nav class="header-nav" id="mainHeaderNav">
      <a class="nav-link-btn active" href="#overview"><i class="fa-solid fa-chart-line"></i> <span data-i="n_overview">Overview</span></a>
      <a class="nav-link-btn" href="#footprint"><i class="fa-solid fa-map-location-dot"></i> <span data-i="n_footprint">GIS Map</span></a>
      <a class="nav-link-btn" href="#projects"><i class="fa-solid fa-city"></i> <span data-i="n_projects">Projects</span></a>
      <a class="nav-link-btn" href="#flagship"><i class="fa-solid fa-seedling"></i> <span data-i="n_flagship">Flagship KAIG</span></a>
      <a class="nav-link-btn" href="#documents"><i class="fa-solid fa-folder-open"></i> <span data-i="n_documents">Vault</span></a>
      <a class="nav-link-btn" href="#journey"><i class="fa-solid fa-timeline"></i> <span data-i="n_journey">Journey</span></a>
      <a class="nav-link-btn" href="#news"><i class="fa-solid fa-newspaper"></i> <span data-i="n_news">News</span></a>
      <a class="nav-link-btn" href="#skills"><i class="fa-solid fa-list-check"></i> <span data-i="n_skills">Matrix</span></a>
      <a class="nav-link-btn" href="#contact"><i class="fa-solid fa-paper-plane"></i> <span data-i="n_contact">Contact</span></a>
    </nav>

    <div class="header-actions">
      <button class="control-btn active" id="btnLangEn" data-lang="en"><i class="fa-solid fa-globe"></i> EN</button>
      <button class="control-btn" id="btnLangAr" data-lang="ar"><i class="fa-solid fa-language"></i> العربية</button>
      <button class="control-btn" id="btnThemeToggle" aria-label="Toggle Theme"><i class="fa-solid fa-moon"></i></button>
      <button class="mobile-burger" id="burgerBtn" aria-label="Toggle Menu"><i class="fa-solid fa-bars"></i></button>
    </div>
  </div>
</header>

<!-- MAIN CONTENT -->
<main class="main-wrapper">
<div class="content-container">

  <!-- OVERVIEW SECTION -->
  <section class="section-block" id="overview">
    <div class="hero-banner">
      <div class="hero-grid">
        <div>
          <div class="hero-tag"><i class="fa-solid fa-shield-halved"></i> <span data-i="hero_tag">Procurement & Supply Chain Executive</span></div>
          <h2 class="hero-title">
            <span data-i="hero_t1">Sourcing & Leading</span><br>
            <span class="gradient-text" data-i="hero_t2">SAR 2.63 Billion</span><br>
            <span data-i="hero_t3">Vision 2030 Mega-Projects.</span>
          </h2>
          <p class="hero-desc" data-i="hero_desc">
            MEP Procurement Section Head based in Riyadh. Over twelve years of engineering leadership across Saudi Arabia and Egypt, managing high-value mechanical, electrical, and plumbing supply chains from junior buyer to section head.
          </p>
          <div class="hero-actions">
            <a class="btn-primary" href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download><i class="fa-solid fa-download"></i> <span data-i="dl_cv">Download Official CV</span></a>
            <a class="btn-secondary" href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank" rel="noopener"><i class="fa-brands fa-linkedin"></i> <span>LinkedIn Profile</span></a>
            <a class="btn-secondary" href="#contact"><i class="fa-solid fa-envelope"></i> <span data-i="get_touch">Get In Touch</span></a>
          </div>
        </div>
        <div class="hero-photo-card">
          <img src="assets/images/headshot.jpg" alt="Mostafa Abdelghany Portrait">
        </div>
      </div>
    </div>

    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-value" data-count="12" data-suf="+">0</div>
        <div class="kpi-title" data-i="k1_t">Years Experience</div>
        <div class="kpi-desc" data-i="k1_d">KSA & Egypt engineering leadership across 14 mega projects.</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" data-count="2.63" data-dec="2"><small>B SAR</small></div>
        <div class="kpi-title" data-i="k2_t">Flagship Contract Value</div>
        <div class="kpi-desc" data-i="k2_d">King Abdullah International Gardens (KAIG) Riyadh.</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" data-count="50" data-suf="+">0</div>
        <div class="kpi-title" data-i="k3_t">Qualified MEP Vendors</div>
        <div class="kpi-desc" data-i="k3_d">Directly managed & prequalified supply chain base.</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" data-count="25" data-suf="/mo">0</div>
        <div class="kpi-title" data-i="k4_t">Material Approvals</div>
        <div class="kpi-desc" data-i="k4_d">Monthly technical submittals throughput with consultants.</div>
      </div>
    </div>
  </section>

  <!-- GIS FOOTPRINT MAP SECTION (#footprint) -->
  <section class="section-block" id="footprint">
    <div class="section-header">
      <div>
        <h2 data-i="map_h2">GIS Projects <em>Interactive Map</em></h2>
        <p data-i="map_p">Interactive spatial map of 14 major construction & infrastructure projects across Saudi Arabia & Egypt. Hover over any marker for instant data!</p>
      </div>
      
      <div class="map-country-tabs" id="mapCountryTabs">
        <button class="map-tab-btn active" data-country="all">All Locations (14)</button>
        <button class="map-tab-btn" data-country="ksa">KSA Projects (6)</button>
        <button class="map-tab-btn" data-country="egypt">Egypt Projects (8)</button>
      </div>
    </div>

    <div class="map-container-box">
      <div id="leaflet-map"></div>
    </div>
  </section>

  <!-- PROJECTS GALLERY SECTION (#projects) -->
  <section class="section-block" id="projects">
    <div class="section-header">
      <div>
        <h2 data-i="prj_h2">Selected <em>Projects Portfolio</em></h2>
        <p data-i="prj_p">Comprehensive showcase of 14 engineering projects across residential, infrastructure, hospitality, healthcare & education with real project photos.</p>
      </div>
    </div>

    <div class="filter-tabs" id="projectFilters">
      <button class="tab-btn active" data-filter="all">All Projects (14)</button>
      <button class="tab-btn" data-filter="mega">Mega Projects</button>
      <button class="tab-btn" data-filter="infra">Infrastructure & Aviation</button>
      <button class="tab-btn" data-filter="residential">Residential & Towers</button>
      <button class="tab-btn" data-filter="hospitality">Hospitality & Commercial</button>
      <button class="tab-btn" data-filter="healthcare">Healthcare & Education</button>
    </div>

    <div class="projects-grid" id="projectsGrid">
      <!-- Dynamic Project Cards Rendered Via JS -->
    </div>
  </section>

  <!-- FLAGSHIP KAIG SECTION -->
  <section class="section-block" id="flagship">
    <div class="section-header">
      <div>
        <h2 data-i="flg_h2">Flagship: <em>King Abdullah International Gardens</em></h2>
        <p data-i="flg_p">Botanical mega-park in north-west Riyadh under Saudi Vision 2030. Leading total MEP procurement lifecycle.</p>
      </div>
    </div>

    <div class="kpi-grid" style="margin-bottom: 24px;">
      <div class="kpi-card"><div class="kpi-value">2.2M <small>m²</small></div><div class="kpi-title" data-i="f1_t">Total Site Area</div><div class="kpi-desc">210 Hectares mega-site in Tuwaiq District.</div></div>
      <div class="kpi-card"><div class="kpi-value">90K+ <small>m²</small></div><div class="kpi-title" data-i="f2_t">Climate Crescent Biomes</div><div class="kpi-desc">World's largest covered botanical gardens.</div></div>
      <div class="kpi-card"><div class="kpi-value">2.63B <small>SAR</small></div><div class="kpi-title" data-i="f3_t">Main Contract Value</div><div class="kpi-desc">Riyadh Region Municipality project.</div></div>
      <div class="kpi-card"><div class="kpi-value">50+ <small>Vendors</small></div><div class="kpi-title" data-i="f4_t">Managed MEP Vendors</div><div class="kpi-desc">HVAC, Chillers, Electrical, BMS & Irrigation.</div></div>
    </div>

    <div class="glass-panel">
      <h4 style="font-size: 16px; color: var(--accent-cyan); margin-bottom: 14px;" data-i="flg_parties">Key Project Stakeholders</h4>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px;">
        <div style="padding: 12px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color);"><b style="font-size: 10px; color: var(--accent-emerald); text-transform: uppercase;">Client</b><div style="font-size: 13px; font-weight: 700;">Riyadh Municipality</div></div>
        <div style="padding: 12px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color);"><b style="font-size: 10px; color: var(--accent-emerald); text-transform: uppercase;">Masterplanner</b><div style="font-size: 13px; font-weight: 700;">Barton Willmore</div></div>
        <div style="padding: 12px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color);"><b style="font-size: 10px; color: var(--accent-emerald); text-transform: uppercase;">Structural Eng</b><div style="font-size: 13px; font-weight: 700;">Buro Happold</div></div>
        <div style="padding: 12px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color);"><b style="font-size: 10px; color: var(--accent-emerald); text-transform: uppercase;">Technical Review</b><div style="font-size: 13px; font-weight: 700;">Dar Al-Handasah</div></div>
        <div style="padding: 12px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color);"><b style="font-size: 10px; color: var(--accent-emerald); text-transform: uppercase;">Supervision</b><div style="font-size: 13px; font-weight: 700;">Omrania & Egis Group</div></div>
      </div>
    </div>
  </section>

  <!-- DOCUMENT VAULT SECTION -->
  <section class="section-block" id="documents">
    <div class="section-header">
      <div>
        <h2 data-i="doc_h2">Document & <em>Certificate Vault</em></h2>
        <p data-i="doc_p">Direct access to official CV, Saudi Council of Engineers membership, experience certificates, and academic credentials.</p>
      </div>
    </div>

    <div class="doc-vault-grid">
      <!-- Doc 1: CV -->
      <div class="doc-card">
        <div class="doc-card-header">
          <div class="doc-icon"><i class="fa-solid fa-file-pdf"></i></div>
          <div class="doc-info">
            <h4 data-i="d1_title">Official Procurement CV (2026)</h4>
            <p data-i="d1_sub">PDF • Executive Track • Complete Career Summary</p>
          </div>
        </div>
        <div class="doc-actions">
          <a class="btn-doc btn-doc-view" href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" target="_blank"><i class="fa-solid fa-eye"></i> <span data-i="btn_view">View</span></a>
          <a class="btn-doc btn-doc-download" href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download><i class="fa-solid fa-download"></i> <span data-i="btn_dl">Download</span></a>
        </div>
      </div>

      <!-- Doc 2: Saudi Council of Engineers -->
      <div class="doc-card">
        <div class="doc-card-header">
          <div class="doc-icon"><i class="fa-solid fa-id-card"></i></div>
          <div class="doc-info">
            <h4 data-i="d2_title">Saudi Council of Engineers Letter</h4>
            <p data-i="d2_sub">PDF • Membership #1084929 • Saudi Arabia</p>
          </div>
        </div>
        <div class="doc-actions">
          <a class="btn-doc btn-doc-view" href="assets/docs/Saudi_Council_of_Engineers_Letter.pdf" target="_blank"><i class="fa-solid fa-eye"></i> <span data-i="btn_view">View</span></a>
          <a class="btn-doc btn-doc-download" href="assets/docs/Saudi_Council_of_Engineers_Letter.pdf" download><i class="fa-solid fa-download"></i> <span data-i="btn_dl">Download</span></a>
        </div>
      </div>

      <!-- Doc 3: Atrium Experience Certificate -->
      <div class="doc-card">
        <div class="doc-card-header">
          <div class="doc-icon"><i class="fa-solid fa-award"></i></div>
          <div class="doc-info">
            <h4 data-i="d3_title">Atrium (Talaat Moustafa) Certificate</h4>
            <p data-i="d3_sub">PDF • Procurement Team Lead • Noor City</p>
          </div>
        </div>
        <div class="doc-actions">
          <a class="btn-doc btn-doc-view" href="assets/docs/Atrium_Talaat_Moustafa_Experience_Certificate.pdf" target="_blank"><i class="fa-solid fa-eye"></i> <span data-i="btn_view">View</span></a>
          <a class="btn-doc btn-doc-download" href="assets/docs/Atrium_Talaat_Moustafa_Experience_Certificate.pdf" download><i class="fa-solid fa-download"></i> <span data-i="btn_dl">Download</span></a>
        </div>
      </div>

      <!-- Doc 4: Pillars Certificate -->
      <div class="doc-card">
        <div class="doc-card-header">
          <div class="doc-icon"><i class="fa-solid fa-certificate"></i></div>
          <div class="doc-info">
            <h4 data-i="d4_title">Pillars Constructions Certificate</h4>
            <p data-i="d4_sub">PDF • Senior Procurement Engineer • Egypt</p>
          </div>
        </div>
        <div class="doc-actions">
          <a class="btn-doc btn-doc-view" href="assets/docs/Pillars_Construction_Experience_Certificate.pdf" target="_blank"><i class="fa-solid fa-eye"></i> <span data-i="btn_view">View</span></a>
          <a class="btn-doc btn-doc-download" href="assets/docs/Pillars_Construction_Experience_Certificate.pdf" download><i class="fa-solid fa-download"></i> <span data-i="btn_dl">Download</span></a>
        </div>
      </div>

      <!-- Doc 5: Graduation Certificate -->
      <div class="doc-card">
        <div class="doc-card-header">
          <div class="doc-icon"><i class="fa-solid fa-graduation-cap"></i></div>
          <div class="doc-info">
            <h4 data-i="d5_title">B.Sc. Mechanical Engineering Degree</h4>
            <p data-i="d5_sub">PDF • Benha University • Graduation Certificate</p>
          </div>
        </div>
        <div class="doc-actions">
          <a class="btn-doc btn-doc-view" href="assets/docs/Graduation_Certificate.pdf" target="_blank"><i class="fa-solid fa-eye"></i> <span data-i="btn_view">View</span></a>
          <a class="btn-doc btn-doc-download" href="assets/docs/Graduation_Certificate.pdf" download><i class="fa-solid fa-download"></i> <span data-i="btn_dl">Download</span></a>
        </div>
      </div>

      <!-- Doc 6: Credentials Photos Gallery -->
      <div class="doc-card">
        <div class="doc-card-header">
          <div class="doc-icon"><i class="fa-solid fa-images"></i></div>
          <div class="doc-info">
            <h4 data-i="d6_title">Engineering Photo Credentials</h4>
            <p data-i="d6_sub">Image Assets • Certificates & Badges</p>
          </div>
        </div>
        <div class="doc-actions">
          <a class="btn-doc btn-doc-view" href="assets/images/cert_image_1.jpg" target="_blank"><i class="fa-solid fa-image"></i> <span data-i="btn_img1">Img 1</span></a>
          <a class="btn-doc btn-doc-view" href="assets/images/cert_image_2.jpg" target="_blank"><i class="fa-solid fa-image"></i> <span data-i="btn_img2">Img 2</span></a>
        </div>
      </div>
    </div>
  </section>

  <!-- JOURNEY SECTION -->
  <section class="section-block" id="journey">
    <div class="section-header">
      <div>
        <h2 data-i="j_h2">Career <em>Progression</em></h2>
        <p data-i="j_p">Five top contracting firms, two countries, continuous leadership growth in MEP procurement.</p>
      </div>
    </div>
    <div class="glass-panel">
      <div style="display: flex; flex-direction: column; gap: 20px;">
        <!-- Role 1 -->
        <div style="display: grid; grid-template-columns: 220px 1fr; gap: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 16px;">
          <div>
            <b style="color: var(--accent-cyan); font-size: 15px;">Zaid Al Hussain Group</b>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">Oct 2024 – Present (Riyadh, KSA)</div>
          </div>
          <div>
            <h4 style="font-size: 16px; color: var(--accent-emerald);">MEP Procurement Section Head</h4>
            <p style="font-size: 13px; color: var(--text-muted); margin-top: 6px;">Leading total mechanical & electrical procurement for the SAR 2.63 Billion King Abdullah International Gardens (KAIG). Directing vendor prequalification, RFQs, submittals, and contract negotiations across 50+ vendors.</p>
          </div>
        </div>

        <!-- Role 2 -->
        <div style="display: grid; grid-template-columns: 220px 1fr; gap: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 16px;">
          <div>
            <b style="color: var(--accent-cyan); font-size: 15px;">Atrium Quality Contractors</b>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">2023 – 2024 (Cairo, Egypt)</div>
          </div>
          <div>
            <h4 style="font-size: 16px; color: var(--text-main);">Procurement Team Lead</h4>
            <p style="font-size: 13px; color: var(--text-muted); margin-top: 6px;">Led procurement team for Noor City mega residential compound in Egypt's New Administrative Capital (Talaat Moustafa Group). Managed MEP supply chains, BOQs, and supplier relations.</p>
          </div>
        </div>

        <!-- Role 3 -->
        <div style="display: grid; grid-template-columns: 220px 1fr; gap: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 16px;">
          <div>
            <b style="color: var(--accent-cyan); font-size: 15px;">Pillars Constructions</b>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">2020 – 2022 (Cairo, Egypt)</div>
          </div>
          <div>
            <h4 style="font-size: 16px; color: var(--text-main);">Senior Procurement Engineer</h4>
            <p style="font-size: 13px; color: var(--text-muted); margin-top: 6px;">Managed procurement packages for Berenice Military Airbase, Zagazig University Campus, and La Verde Compound NAC. Handled technical evaluation, pricing negotiations, and consultant approvals.</p>
          </div>
        </div>

        <!-- Role 4 -->
        <div style="display: grid; grid-template-columns: 220px 1fr; gap: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 16px;">
          <div>
            <b style="color: var(--accent-cyan); font-size: 15px;">Hassan Allam Construction</b>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">2018 – 2021 (Cairo, Egypt)</div>
          </div>
          <div>
            <h4 style="font-size: 16px; color: var(--text-main);">Procurement Engineer</h4>
            <p style="font-size: 13px; color: var(--text-muted); margin-top: 6px;">Sourced MEP equipment and materials for 20-story Aeon Towers, Zewail City Science Campus, Berenice Civil Airport, and Egypt International Exhibition Center.</p>
          </div>
        </div>

        <!-- Role 5 -->
        <div style="display: grid; grid-template-columns: 220px 1fr; gap: 20px;">
          <div>
            <b style="color: var(--accent-cyan); font-size: 15px;">EDC Expertise</b>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">2016 – 2018 (Riyadh, KSA)</div>
          </div>
          <div>
            <h4 style="font-size: 16px; color: var(--text-main);">Junior Procurement Engineer</h4>
            <p style="font-size: 13px; color: var(--text-muted); margin-top: 6px;">Prepared BOQs, technical bid comparisons, and material specs for Riyadh Metro, Radisson Blu Hotel, Hilton Riyadh Hotel, and King Fahd Medical City.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- NEWS & INSIGHTS SECTION -->
  <section class="section-block" id="news">
    <div class="section-header">
      <div>
        <h2 data-i="news_h2">Latest Procurement <em>News & Insights</em></h2>
        <p data-i="news_p">Industry updates, Vision 2030 mega-project progress, and MEP supply chain engineering news.</p>
      </div>
    </div>

    <div class="news-grid">
      <div class="news-card">
        <div class="news-date">March 2026 • Riyadh, KSA</div>
        <h4 data-i="n1_title">King Abdullah Gardens (KAGA) Advances Toward 2026 Opening</h4>
        <p data-i="n1_desc">Major structural & MEP biome climate-control systems completed. The 2.2M m² botanical mega-project western Riyadh is entering final commissioning phases under Saudi Vision 2030 Quality of Life Program.</p>
        <div class="news-tag">KAIG / Vision 2030</div>
      </div>

      <div class="news-card">
        <div class="news-date">February 2026 • Riyadh, KSA</div>
        <h4 data-i="n2_title">Riyadh Metro Infrastructure & Transit Expansion Procurement</h4>
        <p data-i="n2_desc">Royal Commission for Riyadh City expands transit network MEP maintenance & technological upgrade contracts, highlighting strategic sourcing requirements for heavy-duty electrical substations.</p>
        <div class="news-tag">Riyadh Metro / Transit</div>
      </div>

      <div class="news-card">
        <div class="news-date">January 2026 • New Capital, Egypt</div>
        <h4 data-i="n3_title">Noor City Smart MEP & Substation Grid Integration</h4>
        <p data-i="n3_desc">Talaat Moustafa Group completes key electrical and HVAC infrastructure packages in Noor City compound, setting new benchmarks for smart city procurement coordination in Egypt.</p>
        <div class="news-tag">Noor City / New Capital</div>
      </div>
    </div>
  </section>

  <!-- SKILLS & COMPETENCY MATRIX SECTION -->
  <section class="section-block" id="skills">
    <div class="section-header">
      <div>
        <h2 data-i="sk_h2">Competency <em>Matrix</em></h2>
        <p data-i="sk_p">Professional engineering proficiency and core procurement skill sets.</p>
      </div>
    </div>

    <div class="glass-panel" style="margin-bottom: 24px;">
      <div class="skills-grid">
        <div class="skill-item"><div class="skill-header"><span>Strategic Sourcing & Prequalification</span><b>95%</b></div><div class="skill-bar-track"><div class="skill-bar-fill" data-w="95"></div></div></div>
        <div class="skill-item"><div class="skill-header"><span>Vendor & Supplier Management</span><b>95%</b></div><div class="skill-bar-track"><div class="skill-bar-fill" data-w="95"></div></div></div>
        <div class="skill-item"><div class="skill-header"><span>RFQ / RFP Lifecycle Management</span><b>92%</b></div><div class="skill-bar-track"><div class="skill-bar-fill" data-w="92"></div></div></div>
        <div class="skill-item"><div class="skill-header"><span>Technical & Commercial Bid Evaluation</span><b>92%</b></div><div class="skill-bar-track"><div class="skill-bar-fill" data-w="92"></div></div></div>
        <div class="skill-item"><div class="skill-header"><span>Material Submittals & Consultant Approval</span><b>90%</b></div><div class="skill-bar-track"><div class="skill-bar-fill" data-w="90"></div></div></div>
        <div class="skill-item"><div class="skill-header"><span>Contract Negotiation & Cost Variation</span><b>88%</b></div><div class="skill-bar-track"><div class="skill-bar-fill" data-w="88"></div></div></div>
        <div class="skill-item"><div class="skill-header"><span>BOQ Estimation & Quantity Reconciliation</span><b>88%</b></div><div class="skill-bar-track"><div class="skill-bar-fill" data-w="88"></div></div></div>
        <div class="skill-item"><div class="skill-header"><span>MEP Systems (HVAC, Electrical, Plumbing)</span><b>90%</b></div><div class="skill-bar-track"><div class="skill-bar-fill" data-w="90"></div></div></div>
      </div>
    </div>

    <div class="glass-panel">
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px;">
        <div><b style="font-size: 11px; color: var(--accent-cyan); text-transform: uppercase;">Licence / Membership</b><div style="font-size: 13px; font-weight: 700;">Saudi Council of Engineers (#1084929)</div></div>
        <div><b style="font-size: 11px; color: var(--accent-cyan); text-transform: uppercase;">Academic Degree</b><div style="font-size: 13px; font-weight: 700;">B.Sc. Mechanical Engineering (Benha Univ)</div></div>
        <div><b style="font-size: 11px; color: var(--accent-cyan); text-transform: uppercase;">Languages</b><div style="font-size: 13px; font-weight: 700;">Arabic (Native) / English (Professional)</div></div>
        <div><b style="font-size: 11px; color: var(--accent-cyan); text-transform: uppercase;">Iqama Status</b><div style="font-size: 13px; font-weight: 700;">Transferable Iqama (Riyadh, KSA)</div></div>
      </div>
    </div>
  </section>

  <!-- CONTACT SECTION -->
  <section class="section-block" id="contact">
    <div class="section-header">
      <div>
        <h2 data-i="c_h2">Get In <em>Touch</em></h2>
        <p data-i="c_p">Available for Procurement Section Head, Senior Manager, and Team Lead opportunities in Saudi Arabia and the region.</p>
      </div>
    </div>

    <div class="contact-grid">
      <div class="glass-panel">
        <div class="contact-row"><span class="label">Email</span><a href="mailto:engmostafamahoud2012@gmail.com">engmostafamahoud2012@gmail.com</a></div>
        <div class="contact-row"><span class="label">Phone (KSA)</span><a href="tel:+966502582122">+966 502 582 122</a></div>
        <div class="contact-row"><span class="label">LinkedIn</span><a href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank" rel="noopener">Mostafa Abdelghany Profile</a></div>
        <div class="contact-row"><span class="label">Location</span><span class="val">Riyadh, Kingdom of Saudi Arabia</span></div>
      </div>

      <div class="glass-panel" style="display: flex; flex-direction: column; justify-content: center; gap: 16px;">
        <h4 style="font-size: 18px; color: var(--text-main); font-weight: 800;" data-i="c_box_title">Request Executive CV & References</h4>
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;" data-i="c_box_desc">Looking to staff a major Vision 2030 infrastructure project or commercial development? Download the complete CV or connect directly on LinkedIn.</p>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <a class="btn-primary" href="assets/docs/Mostafa_Abdelghany_Procurement_CV.pdf" download><i class="fa-solid fa-download"></i> <span data-i="dl_cv">Download CV</span></a>
          <a class="btn-secondary" href="https://www.linkedin.com/in/mostafa-abdelghany-procurement/" target="_blank" rel="noopener"><i class="fa-brands fa-linkedin"></i> <span>LinkedIn Profile</span></a>
        </div>
      </div>
    </div>

    <footer>
      Mostafa Mahmoud Osman Abdelghany • MEP Procurement Section Head • Riyadh, KSA
    </footer>
  </section>

</div>
</main>

<!-- Leaflet GIS Map JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<script>
(function() {
  "use strict";

  /* =========================================================
     PROJECTS DATA ARRAY (14 PROJECTS WITH REAL PHOTOS)
     ========================================================= */
  const projectsData = [
    {
      id: 1,
      title: "King Abdullah International Gardens (KAIG)",
      category: "mega",
      country: "ksa",
      company: "Zaid Al Hussain Group",
      period: "Oct 2024 – Present",
      location: "Riyadh, KSA",
      lat: 24.6288, lng: 46.5401,
      value: "2.63 Billion SAR",
      desc: "Botanical mega-park (2.2M m²). Leading total mechanical & electrical procurement across 50+ qualified suppliers for climate-controlled biomes, HVAC, and power substations.",
      image: "assets/images/project_1.jpg"
    },
    {
      id: 2,
      title: "Riyadh Metro Project",
      category: "infra",
      country: "ksa",
      company: "EDC Expertise",
      period: "2016 – 2017",
      location: "Riyadh, KSA",
      lat: 24.7136, lng: 46.6753,
      value: "Transit Infrastructure",
      desc: "Owner: Royal Commission for Riyadh City. Prepared BOQs and material specifications for metro station MEP systems.",
      image: "assets/images/project_2.jpg"
    },
    {
      id: 3,
      title: "Radisson Blu Hotel",
      category: "hospitality",
      country: "ksa",
      company: "EDC Expertise",
      period: "2018",
      location: "Riyadh, KSA",
      lat: 24.7000, lng: 46.6800,
      value: "Hospitality Package",
      desc: "Sourced luxury hotel MEP systems, chillers, AHUs, and high-end plumbing & electrical fixtures.",
      image: "assets/images/project_3.jpg"
    },
    {
      id: 4,
      title: "Hilton Riyadh Hotel & Residences",
      category: "hospitality",
      country: "ksa",
      company: "EDC Expertise",
      period: "2018",
      location: "Riyadh, KSA",
      lat: 24.7500, lng: 46.7200,
      value: "Hospitality Package",
      desc: "Mechanical & electrical procurement for 5-star hotel towers and grand ballroom MEP infrastructure.",
      image: "assets/images/project_4.jpg"
    },
    {
      id: 5,
      title: "King Fahd Medical City",
      category: "healthcare",
      country: "ksa",
      company: "EDC Expertise",
      period: "2017",
      location: "Riyadh, KSA",
      lat: 24.6892, lng: 46.7020,
      value: "Healthcare Package",
      desc: "Specialized medical gas systems, HVAC isolation room units, and hospital electrical supply chain.",
      image: "assets/images/project_5.jpg"
    },
    {
      id: 6,
      title: "Haifa Compound",
      category: "residential",
      country: "ksa",
      company: "EDC Expertise",
      period: "2017",
      location: "Riyadh, KSA",
      lat: 24.7800, lng: 46.6500,
      value: "Residential Package",
      desc: "Residential compound MEP sourcing, power distribution substations, and plumbing packages.",
      image: "assets/images/project_6.jpg"
    },
    {
      id: 7,
      title: "Noor City Mega Compound",
      category: "mega",
      country: "egypt",
      company: "Atrium (Talaat Moustafa Group)",
      period: "2023 – 2024",
      location: "New Capital, Egypt",
      lat: 30.0100, lng: 31.6500,
      value: "Smart Residential City",
      desc: "Procurement Team Lead directing MEP subcontracts, electrical networks, and supply chains across smart compound phases.",
      image: "assets/images/project_7.jpg"
    },
    {
      id: 8,
      title: "Zewail City of Science & Technology",
      category: "healthcare",
      country: "egypt",
      company: "Hassan Allam Technology",
      period: "2019",
      location: "6th October, Egypt",
      lat: 29.9600, lng: 30.9200,
      value: "Education & Data Center",
      desc: "Procurement quantity reconciliation and sourcing for Main Data Center & academic research labs.",
      image: "assets/images/project_8.jpg"
    },
    {
      id: 9,
      title: "Aeon Towers (20 Floors)",
      category: "residential",
      country: "egypt",
      company: "Hassan Allam Construction",
      period: "2020 – 2021",
      location: "6th October, Egypt",
      lat: 29.9800, lng: 30.9400,
      value: "Luxury Towers",
      desc: "20-story luxury turnkey residential tower. Sourced HVAC, fire-fighting, and plumbing submittals and vendor management.",
      image: "assets/images/project_9.jpg"
    },
    {
      id: 10,
      title: "Egypt International Exhibition Center",
      category: "hospitality",
      country: "egypt",
      company: "Hassan Allam Technology",
      period: "2016",
      location: "New Cairo, Egypt",
      lat: 30.0300, lng: 31.4200,
      value: "Commercial Halls",
      desc: "Mega exhibition halls MEP procurement, heavy-duty electrical distribution, and HVAC systems.",
      image: "assets/images/project_10.jpg"
    },
    {
      id: 11,
      title: "Berenice Civil Airport",
      category: "infra",
      country: "egypt",
      company: "Hassan Allam Technology",
      period: "2019",
      location: "Berenice, Red Sea, Egypt",
      lat: 23.9700, lng: 35.4600,
      value: "Civil Aviation",
      desc: "Civil airport MEP procurement, airfield lighting systems, passenger terminal MEP packages.",
      image: "assets/images/project_11.jpg"
    },
    {
      id: 12,
      title: "Berenice Military Air Base",
      category: "infra",
      country: "egypt",
      company: "Pillars Construction",
      period: "2020",
      location: "Berenice, Red Sea, Egypt",
      lat: 23.9500, lng: 35.4800,
      value: "Defense Infrastructure",
      desc: "Defense air base infrastructure MEP procurement, emergency generator plants, airfield electrical.",
      image: "assets/images/project_12.jpg"
    },
    {
      id: 13,
      title: "Zagazig University Campus",
      category: "healthcare",
      country: "egypt",
      company: "Pillars Construction",
      period: "2023",
      location: "Sharqia, Egypt",
      lat: 30.5870, lng: 31.5020,
      value: "Medical & Education",
      desc: "Educational hospital MEP packages, medical equipment supply chain, central cooling plants.",
      image: "assets/images/project_13.jpg"
    },
    {
      id: 14,
      title: "La Verde Compound",
      category: "residential",
      country: "egypt",
      company: "Pillars Construction",
      period: "2021 – 2022",
      location: "New Capital, Egypt",
      lat: 30.0050, lng: 31.6400,
      value: "Luxury Residential",
      desc: "High-end residential compound MEP procurement, solar lighting, smart irrigation MEP.",
      image: "assets/images/project_14.jpg"
    }
  ];

  /* =========================================================
     DICTIONARY TRANSLATIONS (EN / AR)
     ========================================================= */
  const translations = {
    en: {
      role_sub: "MEP Procurement Section Head",
      n_overview: "Overview",
      n_footprint: "GIS Map",
      n_projects: "Projects",
      n_flagship: "Flagship KAIG",
      n_documents: "Vault",
      n_journey: "Journey",
      n_news: "News",
      n_skills: "Matrix",
      n_contact: "Contact",
      hero_tag: "Procurement & Supply Chain Executive",
      hero_t1: "Sourcing & Leading",
      hero_t2: "SAR 2.63 Billion",
      hero_t3: "Vision 2030 Mega-Projects.",
      hero_desc: "MEP Procurement Section Head based in Riyadh. Over twelve years of engineering leadership across Saudi Arabia and Egypt, managing high-value mechanical, electrical, and plumbing supply chains from junior buyer to section head.",
      dl_cv: "Download Official CV",
      get_touch: "Get In Touch",
      k1_t: "Years Experience",
      k1_d: "KSA & Egypt engineering leadership across 14 mega projects.",
      k2_t: "Flagship Contract Value",
      k2_d: "King Abdullah International Gardens (KAIG) Riyadh.",
      k3_t: "Qualified MEP Vendors",
      k3_d: "Directly managed & prequalified supply chain base.",
      k4_t: "Material Approvals",
      k4_d: "Monthly technical submittals throughput with consultants.",
      doc_h2: "Document & <em>Certificate Vault</em>",
      doc_p: "Direct access to official CV, Saudi Council of Engineers membership, experience certificates, and academic credentials.",
      d1_title: "Official Procurement CV (2026)",
      d1_sub: "PDF • Executive Track • Complete Career Summary",
      d2_title: "Saudi Council of Engineers Letter",
      d2_sub: "PDF • Membership #1084929 • Saudi Arabia",
      d3_title: "Atrium (Talaat Moustafa) Certificate",
      d3_sub: "PDF • Procurement Team Lead • Noor City",
      d4_title: "Pillars Constructions Certificate",
      d4_sub: "PDF • Senior Procurement Engineer • Egypt",
      d5_title: "B.Sc. Mechanical Engineering Degree",
      d5_sub: "PDF • Benha University • Graduation Certificate",
      d6_title: "Engineering Photo Credentials",
      d6_sub: "Image Assets • Certificates & Badges",
      btn_view: "View",
      btn_dl: "Download",
      btn_img1: "Image 1",
      btn_img2: "Image 2",
      j_h2: "Career <em>Progression</em>",
      j_p: "Five top contracting firms, two countries, continuous leadership growth in MEP procurement.",
      map_h2: "GIS Projects <em>Interactive Map</em>",
      map_p: "Interactive spatial map of 14 major construction & infrastructure projects across Saudi Arabia & Egypt. Hover over any marker for instant data!",
      flg_h2: "Flagship: <em>King Abdullah International Gardens</em>",
      flg_p: "Botanical mega-park in north-west Riyadh under Saudi Vision 2030. Leading total MEP procurement lifecycle.",
      f1_t: "Total Site Area",
      f2_t: "Climate Crescent Biomes",
      f3_t: "Main Contract Value",
      f4_t: "Managed MEP Vendors",
      flg_parties: "Key Project Stakeholders",
      prj_h2: "Selected <em>Projects Portfolio</em>",
      prj_p: "Comprehensive showcase of 14 engineering projects across residential, infrastructure, hospitality, healthcare & education with real project photos.",
      news_h2: "Latest Procurement <em>News & Insights</em>",
      news_p: "Industry updates, Vision 2030 mega-project progress, and MEP supply chain engineering news.",
      n1_title: "King Abdullah Gardens (KAGA) Advances Toward 2026 Opening",
      n1_desc: "Major structural & MEP biome climate-control systems completed. The 2.2M m² botanical mega-project western Riyadh is entering final commissioning phases under Saudi Vision 2030 Quality of Life Program.",
      n2_title: "Riyadh Metro Infrastructure & Transit Expansion Procurement",
      n2_desc: "Royal Commission for Riyadh City expands transit network MEP maintenance & technological upgrade contracts, highlighting strategic sourcing requirements for heavy-duty electrical substations.",
      n3_title: "Noor City Smart MEP & Substation Grid Integration",
      n3_desc: "Talaat Moustafa Group completes key electrical and HVAC infrastructure packages in Noor City compound, setting new benchmarks for smart city procurement coordination in Egypt.",
      sk_h2: "Competency <em>Matrix</em>",
      sk_p: "Professional engineering proficiency and core procurement skill sets.",
      c_h2: "Get In <em>Touch</em>",
      c_p: "Available for Procurement Section Head, Senior Manager, and Team Lead opportunities in Saudi Arabia and the region.",
      c_box_title: "Request Executive CV & References",
      c_box_desc: "Looking to staff a major Vision 2030 infrastructure project or commercial development? Download the complete CV or connect directly on LinkedIn."
    },
    ar: {
      role_sub: "رئيس قسم مشتريات MEP",
      n_overview: "نظرة عامة",
      n_footprint: "خريطة المشاريع",
      n_projects: "المشاريع",
      n_flagship: "حدائق الملك عبدالله",
      n_documents: "الوثائق",
      n_journey: "المسيرة المهنية",
      n_news: "الأخبار",
      n_skills: "المهارات",
      n_contact: "التواصل",
      hero_tag: "قيادي المشتريات وسلاسل الإمداد الهندسية",
      hero_t1: "إدارة وتوريد مشاريع ضخمة",
      hero_t2: "بقيمة 2.63 مليار ريال",
      hero_t3: "ضمن رؤية المملكة 2030.",
      hero_desc: "رئيس قسم مشتريات الكهروميكانيك (MEP) بالرياض. أكثر من 12 عاماً من القيادة الهندسية في السعودية ومصر، في إدارة وتوريد الشبكات الكهربائية والميكانيكية والمرافق للمشاريع الكبرى.",
      dl_cv: "تحميل السيرة الذاتية الرسمية",
      get_touch: "تواصل معي",
      k1_t: "سنوات الخبرة",
      k1_d: "قيادة هندسية في السعودية ومصر عبر 14 مشروعاً ضخماً.",
      k2_t: "قيمة المشروع الرئيسي",
      k2_d: "مشروع حدائق الملك عبد الله العالمية بالرياض.",
      k3_t: "مورد كهروميكانيك معتمد",
      k3_d: "إدارة وتأهيل قاعدة الموردين والمقاولين الباطن.",
      k4_t: "اعتمادات مواد شهرياً",
      k4_d: "معدل اعتماد الاعتمادات الفنية للمواد مع الاستشاريين.",
      doc_h2: "مركز الوثائق <em>والشهادات الرسمية</em>",
      doc_p: "معاينة وتحميل السيرة الذاتية، خطاب الهيئة السعودية للمهندسين، شهادات الخبرة، والشهادات الأكاديمية مباشرة.",
      d1_title: "السيرة الذاتية الرسمية (2026)",
      d1_sub: "PDF • مسار تنفيذي • ملخص مهني شامل",
      d2_title: "خطاب الهيئة السعودية للمهندسين",
      d2_sub: "PDF • رقم العضوية #1084929 • المملكة العربية السعودية",
      d3_title: "شهادة خبرة أتريم (طلعت مصطفى)",
      d3_sub: "PDF • قائد فريق المشتريات • مشروع مدينة نور",
      d4_title: "شهادة خبرة بيلرز للمقاولات",
      d4_sub: "PDF • مهندس مشتريات أول • مصر",
      d5_title: "شهادة التخرج (بكالوريوس هندسة ميكانيكية)",
      d5_sub: "PDF • جامعة بنها • شهادة التخرج الرسمية",
      d6_title: "الشهادات والوثائق المصورة",
      d6_sub: "صور عالية الجودة • شهادات وتراخيص",
      btn_view: "معاينة",
      btn_dl: "تحميل",
      btn_img1: "صورة 1",
      btn_img2: "صورة 2",
      j_h2: "المسيرة <em>المهنية</em>",
      j_p: "خمس شركات كبرى، دولتان، وتطور قيادي مستمر في قطاع مشتريات MEP.",
      map_h2: "خريطة المشاريع <em>التفاعلية GIS</em>",
      map_p: "خريطة تفاعلية لـ 14 مشروعاً هندسياً في السعودية ومصر. مرر الماوس (Hover) على أي نقطة لعرض التفاصيل فوراً!",
      flg_h2: "المشروع الرئيسي: <em>حدائق الملك عبد الله العالمية</em>",
      flg_p: "مشروع البيئة العالمي بشمال غرب الرياض ضمن رؤية 2030. قيادة دورة المشتريات الكهروميكانيكية بالكامل.",
      f1_t: "إجمالي مساحة المشروع",
      f2_t: "مساحة البيئات المغلقة",
      f3_t: "قيمة العقد الرئيسي",
      f4_t: "الموردين المعتمدين",
      flg_parties: "أطراف المشروع الرئيسية",
      prj_h2: "معرض <em>المشاريع المختارة</em>",
      prj_p: "عرض شامل لـ 14 مشروعاً هندسياً تتنوع بين السكني، البنية التحتية، الضيافة، الرعاية الصحية، والتعليم مع صور حقيقية للمشاريع.",
      news_h2: "أحدث الأخبار <em>ومستجدات القطاع</em>",
      news_p: "متابعة تسارع الأعمال في مشاريع رؤية 2030 ومستجدات سلاسل إمداد الكهروميكانيك.",
      n1_title: "تسارع الأعمال في حدائق الملك عبد الله (KAGA) للافتتاح في 2026",
      n1_desc: "إنجاز الأعمال الهيكلية وأنظمة التكييف والتحكم المناخي للبيئات المغلقة بالمشروع البالغ مساحته 2.2 مليون م² غرب الرياض.",
      n2_title: "توسعات عقود مشتريات البنية التحتية لمترو الرياض",
      n2_desc: "الهيئة الملكية لمدينة الرياض تتوسع في تحديث أنظمة الصيانة والتجهيزات الكهروميكانيكية لمحطات المترو.",
      n3_title: "ربط شبكات الكهروميكانيك والمحطات الذكية بمدينة نور",
      n3_desc: "مجموعة طلعت مصطفى تنهي حزم البنية التحتية الكهربائية والتكييف بمدينة نور بالعاصمة الإدارية.",
      sk_h2: "مصفوفة <em>المهارات والكفاءات</em>",
      sk_p: "الكفاءة الهندسية والتنفيذية في إدارة سلاسل الإمداد والمشتريات.",
      c_h2: "معلومات <em>التواصل</em>",
      c_p: "متاح للفرص القيادية كرئيس قسم مشتريات أو مدير مشتريات في المملكة العربية السعودية والمنطقة.",
      c_box_title: "طلب السيرة الذاتية والتوصيات",
      c_box_desc: "هل تبحث عن قيادي هندسي لإدارة مشتريات مشروع ضخم ضمن رؤية 2030؟ حمّل السيرة الذاتية أو تواصل عبر LinkedIn."
    }
  };

  /* =========================================================
     LANGUAGE & THEME LOGIC
     ========================================================= */
  let currentLang = 'en';

  function applyLanguage(lang) {
    currentLang = lang;
    document.documentElement.setAttribute('lang', lang);
    document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

    document.querySelectorAll('[data-i]').forEach(el => {
      const key = el.getAttribute('data-i');
      if (translations[lang] && translations[lang][key]) {
        el.innerHTML = translations[lang][key];
      }
    });

    document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');
    document.getElementById('btnLangAr').classList.toggle('active', lang === 'ar');
  }

  document.getElementById('btnLangEn').addEventListener('click', () => applyLanguage('en'));
  document.getElementById('btnLangAr').addEventListener('click', () => applyLanguage('ar'));

  const btnThemeToggle = document.getElementById('btnThemeToggle');
  btnThemeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    btnThemeToggle.innerHTML = newTheme === 'dark' ? '<i class="fa-solid fa-moon"></i>' : '<i class="fa-solid fa-sun"></i>';
  });

  /* Mobile Burger Menu */
  const burgerBtn = document.getElementById('burgerBtn');
  const mainHeaderNav = document.getElementById('mainHeaderNav');
  burgerBtn.addEventListener('click', () => {
    mainHeaderNav.style.display = mainHeaderNav.style.display === 'flex' ? 'none' : 'flex';
  });

  /* =========================================================
     RENDER PROJECTS GALLERY
     ========================================================= */
  const projectsGrid = document.getElementById('projectsGrid');
  
  function renderProjects(filter = 'all') {
    projectsGrid.innerHTML = '';
    
    const filtered = filter === 'all' 
      ? projectsData 
      : projectsData.filter(p => p.category === filter);

    filtered.forEach(p => {
      const card = document.createElement('div');
      card.className = 'project-card';
      card.innerHTML = `
        <div class="project-thumb">
          <img src="${p.image}" alt="${p.title}">
          <span class="project-badge">${p.company}</span>
        </div>
        <div class="project-content">
          <div class="project-location"><i class="fa-solid fa-location-dot"></i> ${p.location} • ${p.period}</div>
          <h3 class="project-title">${p.title}</h3>
          <p class="project-desc">${p.desc}</p>
          <div class="project-meta-row">
            <span>Scope: <b>MEP Procurement</b></span>
            <span>Value: <b>${p.value}</b></span>
          </div>
        </div>
      `;
      projectsGrid.appendChild(card);
    });
  }

  renderProjects();

  /* Project Filter Tabs */
  document.querySelectorAll('#projectFilters .tab-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('#projectFilters .tab-btn').forEach(b => b.classList.remove('active'));
      e.target.classList.add('active');
      renderProjects(e.target.getAttribute('data-filter'));
    });
  });

  /* =========================================================
     REALISTIC LEAFLET GIS MAP WITH HOVER DATA & COUNTRY TABS
     ========================================================= */
  const map = L.map('leaflet-map', {
    center: [26.8, 38.5],
    zoom: 5,
    zoomControl: true
  });

  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
    maxZoom: 18
  }).addTo(map);

  let mapMarkers = [];

  function renderMapMarkers(countryFilter = 'all') {
    // Clear existing
    mapMarkers.forEach(m => map.removeLayer(m));
    mapMarkers = [];

    const filtered = countryFilter === 'all' 
      ? projectsData 
      : projectsData.filter(p => p.country === countryFilter);

    const bounds = [];

    filtered.forEach(p => {
      const pinClass = p.country === 'ksa' ? 'custom-map-pin-ksa' : 'custom-map-pin-egypt';
      
      const customIcon = L.divIcon({
        className: pinClass,
        iconSize: [24, 24],
        iconAnchor: [12, 12]
      });

      const tooltipContent = `
        <div style="font-weight: 800; color: var(--accent-cyan); font-size: 13px;">${p.title}</div>
        <div style="font-size: 11px; color: #cbd5e1;">${p.company} • ${p.location}</div>
        <div style="font-size: 11px; color: var(--accent-emerald); font-weight: 700; margin-top: 2px;">Value: ${p.value}</div>
      `;

      const popupContent = `
        <div class="map-popup-card">
          <h4>${p.title}</h4>
          <p><b>Company:</b> ${p.company}</p>
          <p><b>Location:</b> ${p.location} (${p.period})</p>
          <p>${p.desc}</p>
          <div class="val">Contract Value: ${p.value}</div>
        </div>
      `;

      const marker = L.marker([p.lat, p.lng], { icon: customIcon })
        .addTo(map)
        .bindTooltip(tooltipContent, { sticky: true, direction: 'top' })
        .bindPopup(popupContent);

      mapMarkers.push(marker);
      bounds.push([p.lat, p.lng]);
    });

    if (bounds.length > 0) {
      map.fitBounds(bounds, { padding: [50, 50] });
    }
  }

  renderMapMarkers('all');

  /* Invalidate size on load */
  setTimeout(() => map.invalidateSize(), 300);

  /* Map Tabs */
  document.querySelectorAll('#mapCountryTabs .map-tab-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('#mapCountryTabs .map-tab-btn').forEach(b => b.classList.remove('active'));
      e.target.classList.add('active');
      renderMapMarkers(e.target.getAttribute('data-country'));
    });
  });

  /* =========================================================
     SCROLL OBSERVER FOR COUNTERS & SKILLS
     ========================================================= */
  const observerOptions = { threshold: 0.2 };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('.skill-bar-fill').forEach(bar => {
          bar.style.width = bar.getAttribute('data-w') + '%';
        });

        entry.target.querySelectorAll('[data-count]').forEach(counter => {
          if (counter.classList.contains('counted')) return;
          counter.classList.add('counted');
          
          const target = parseFloat(counter.getAttribute('data-count'));
          const suf = counter.getAttribute('data-suf') || '';
          const dec = parseInt(counter.getAttribute('data-dec')) || 0;
          
          let count = 0;
          const speed = target / 30;
          
          const updateCount = () => {
            count += speed;
            if (count < target) {
              counter.innerHTML = (dec > 0 ? count.toFixed(dec) : Math.ceil(count)) + suf;
              setTimeout(updateCount, 40);
            } else {
              counter.innerHTML = (dec > 0 ? target.toFixed(dec) : target) + suf;
            }
          };
          updateCount();
        });
      }
    });
  }, observerOptions);

  document.querySelectorAll('.section-block').forEach(sec => observer.observe(sec));

})();
</script>

</body>
</html>
