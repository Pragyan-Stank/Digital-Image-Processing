

import numpy as np
from PIL import Image
import math

# 1) load and grayscale
img = Image.open("/content/lenna.jpg").convert("L")
I = np.array(img, dtype=np.float32)

# 2) Sobel kernels
Gx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]], dtype=np.float32)

Gy = np.array([[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]], dtype=np.float32)

kh, kw = 3, 3
pad = 1

# 3) pad image (zero padding)
P = np.pad(I, ((pad, pad), (pad, pad)), mode='constant')

h, w = I.shape
gx = np.zeros_like(I)
gy = np.zeros_like(I)
mag = np.zeros_like(I)

# 4) convolution with loops
for y in range(h):
    for x in range(w):
        region = P[y:y+kh, x:x+kw]
        s1 = np.sum(region * Gx)   # Gx response
        s2 = np.sum(region * Gy)   # Gy response
        gx[y, x] = s1
        gy[y, x] = s2
        # gradient magnitude
        mag[y, x] = math.sqrt(s1*s1 + s2*s2)

# 5) normalize to 0..255 for saving (avoid divide by zero)
mag = mag / (mag.max() + 1e-8) * 255.0
mag = np.clip(mag, 0, 255).astype(np.uint8)

# optional: simple threshold to create binary edges
threshold = 50  # try values like 30, 50, 100
edges_binary = (mag > threshold).astype(np.uint8) * 255

# save results
Image.fromarray(mag).save("sobel_magnitude.jpg")
Image.fromarray(edges_binary).save("sobel_edges_binary.jpg")
print("Saved: sobel_magnitude.jpg and sobel_edges_binary.jpg")
