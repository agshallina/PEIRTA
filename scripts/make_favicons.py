from PIL import Image
import os

root = os.path.dirname(os.path.dirname(__file__))
# Prefer an uploaded `favicon.png` in LOGO/, otherwise fall back to IMG_5570.PNG
fav_candidate = os.path.join(root, "LOGO", "favicon.png")
fallback = os.path.join(root, "LOGO", "IMG_5570.PNG")
src = fav_candidate if os.path.exists(fav_candidate) else fallback

out16 = os.path.join(root, "favicon-16.png")
out32 = os.path.join(root, "favicon-32.png")
out64 = os.path.join(root, "favicon-64.png")
out96 = os.path.join(root, "favicon-96.png")
out128 = os.path.join(root, "favicon-128.png")
ico = os.path.join(root, "favicon.ico")

img = Image.open(src).convert("RGBA")

for size, path in ((16, out16), (32, out32), (64, out64), (96, out96), (128, out128)):
    im = img.copy()
    im = im.resize((size, size), Image.LANCZOS)
    im.save(path)

# save multi-resolution ico with larger sizes
img.save(ico, format='ICO', sizes=[(16,16),(32,32),(64,64),(96,96),(128,128)])

print('Created files:', out16, out32, out64, out96, out128, ico)
