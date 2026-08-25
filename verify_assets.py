import os
import re

base_dir = r"c:\Users\civil\Downloads\eng mostafa profile"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Check img src
srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
# Check data-images
data_imgs = re.findall(r'data-images=["\']([^"\']+)["\']', content)
for di in data_imgs:
    srcs.extend([s.strip() for s in di.split(",") if s.strip()])

# Check a href for assets/docs
hrefs = re.findall(r'<a[^>]+href=["\'](assets/docs/[^"\']+)["\']', content)

missing_files = []
for src in srcs:
    if src.startswith("http"):
        continue
    full_p = os.path.normpath(os.path.join(base_dir, src))
    if not os.path.exists(full_p):
        missing_files.append(("IMG", src, full_p))

for href in hrefs:
    full_p = os.path.normpath(os.path.join(base_dir, href))
    if not os.path.exists(full_p):
        missing_files.append(("DOC", href, full_p))

print(f"Total asset references checked: {len(srcs) + len(hrefs)}")
if missing_files:
    print("MISSING FILES:")
    for t, rel, full in missing_files:
        print(f"  [{t}] {rel}")
else:
    print("ALL ASSETS AND DOCUMENTS EXIST 100% OK!")
