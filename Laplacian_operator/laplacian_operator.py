import numpy as np
from PIL import Image

# load grayscale image
img = Image.open("/content/lenna.jpg").convert("L")
I = np.array(img, dtype=np.float32)

# 8-neighbor Laplacian kernel
kernel = np.array([[1, 4, 1],
                   [4,-20, 4],
                   [1, 4, 1]])

h, w = I.shape
out = np.zeros_like(I)

# padding
P = np.pad(I, ((1,1),(1,1)), mode='constant')

# convolution
for y in range(h):
    for x in range(w):
        region = P[y:y+3, x:x+3]
        out[y, x] = np.sum(region * kernel)

# normalize to 0–255
out = np.clip(out, 0, 255).astype(np.uint8)

Image.fromarray(out).save("laplacian_edges.jpg")
