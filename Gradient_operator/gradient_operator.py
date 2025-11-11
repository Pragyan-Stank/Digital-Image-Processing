import numpy as np
from PIL import Image

# load grayscale image
img = Image.open("/content/lenna.jpg.webp").convert("L")
I = np.array(img, dtype=np.float32)

# horizontal gradient (difference along x)
gx = I[:, 1:] - I[:, :-1]

# vertical gradient (difference along y)
gy = I[1:, :] - I[:-1, :]

# gradient magnitude
mag = np.sqrt(gx[:-1,:]**2 + gy[:,:-1]**2)

# normalize and save
mag = (mag / mag.max() * 255).astype(np.uint8)
Image.fromarray(mag).save("discrete_gradient.jpg")
