import codecs
import re
with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

match = re.search(r'With 12\+ years[^>]*data-ar="([^"]*)"', html)
if match:
    print("Found Arabic text:")
    print(match.group(1))
else:
    print("Not found")

print("Checking 'About & Engineering Philosophy':", 'About & Engineering Philosophy' in html)
print("Checking 'data-target=\"12\"':", 'data-target="12"' in html)
