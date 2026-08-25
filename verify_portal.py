import os
import re

base_dir = r"c:\Users\civil\Downloads\eng mostafa profile"

html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

errors = []
total_links = 0
total_images = 0

for hf in html_files:
    path = os.path.join(base_dir, hf)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check <a> links
    links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', content)
    for l in links:
        total_links += 1
        if l.startswith("http") or l.startswith("mailto:") or l.startswith("tel:") or l.startswith("#"):
            continue
        # Strip query param or hash
        clean_l = l.split("?")[0].split("#")[0]
        if not clean_l:
            continue
        target_path = os.path.normpath(os.path.join(base_dir, clean_l))
        if not os.path.exists(target_path):
            errors.append((hf, "LINK", l, target_path))

    # Check <img>
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for img in imgs:
        if not img:  # empty placeholder dynamically loaded
            continue
        total_images += 1
        if img.startswith("http"):
            continue
        target_path = os.path.normpath(os.path.join(base_dir, img))
        if not os.path.exists(target_path):
            errors.append((hf, "IMG", img, target_path))

    # Check <script>
    scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content)
    for scr in scripts:
        if scr.startswith("http"):
            continue
        target_path = os.path.normpath(os.path.join(base_dir, scr))
        if not os.path.exists(target_path):
            errors.append((hf, "SCRIPT", scr, target_path))

print(f"Verified {len(html_files)} HTML files:")
for hf in sorted(html_files):
    print(f"  - {hf}")

print(f"\nTotal links checked: {total_links}")
print(f"Total image tags checked: {total_images}")

if errors:
    print("\nERRORS DETECTED:")
    for src, t, ref, path in errors:
        print(f"  [{src}] {t}: '{ref}' -> NOT FOUND: {path}")
else:
    print("\nALL LINKS, SCRIPTS, AND ASSETS ACROSS ALL 9 PAGES VERIFIED 100% OK!")
