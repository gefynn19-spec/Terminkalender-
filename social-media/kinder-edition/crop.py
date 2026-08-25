from PIL import Image
U = '/root/.claude/uploads/6b3c0455-83b5-55c2-b784-2094c7c0553d/'
RATIO = 240 / 340  # Polaroid-Bildflaeche

# (Quelle, Ziel, y-Start, y-Ende, x-Mitte) - alles als Anteil des Bildes
jobs = [
    ('2772eda0-image.jpg', 'kfoto1.jpg', 0.24, 0.71, 0.55),
    ('b3ccfa7c-image.jpg', 'kfoto2.jpg', 0.21, 0.85, 0.50),
    ('f612495c-image.jpg', 'kfoto3.jpg', 0.19, 0.88, 0.57),
]

for src, dst, y0f, y1f, xcf in jobs:
    im = Image.open(U + src).convert('RGB')
    W, H = im.size
    y0, y1 = int(y0f * H), int(y1f * H)
    h = y1 - y0
    w = int(h * RATIO)
    if w > W:
        w = W
        h = int(w / RATIO)
        y1 = y0 + h
    xc = int(xcf * W)
    x0 = max(0, min(W - w, xc - w // 2))
    crop = im.crop((x0, y0, x0 + w, y1))
    crop.thumbnail((640, 640 * 4), Image.LANCZOS)
    crop.save(dst, quality=88, subsampling=1)
    print('%s <- %s  box=(%d,%d,%d,%d)  out=%s' % (dst, src, x0, y0, x0 + w, y1, crop.size))
