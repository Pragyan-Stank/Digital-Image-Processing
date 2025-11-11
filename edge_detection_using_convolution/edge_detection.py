import numpy as np
from PIL import Image

# 1) load and convert to grayscale
img = Image.open("/content/lenna.jpg").convert("L")   # "L" = grayscale
a = np.array(img)                           # 'a' is the image array

a.shape

# 2) choose a kernel (edge detection here)
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

kh, kw = kernel.shape
pad = kh // 2

# 3) pad the image so kernel fits at edges (zero padding)
p = np.pad(a, ((pad, pad), (pad, pad)), mode='constant')

# 4) output array (same size as original)
out = np.zeros_like(a, dtype=np.float32)

# 5) nested loops — apply kernel at every pixel
h, w = a.shape
for y in range(h):
    for x in range(w):
        region = p[y:y+kh, x:x+kw]   # same size as kernel
        out[y, x] = np.sum(region * kernel)

# 6) normalize / clip to valid pixel range 0..255
# If kernel sums to 1 (like blur), you may divide by kernel.sum() before clip.
out = np.clip(out, 0, 255).astype(np.uint8)

# 7) save and show
res = Image.fromarray(out)
res.save("output_convolved.jpg")
res.show()
