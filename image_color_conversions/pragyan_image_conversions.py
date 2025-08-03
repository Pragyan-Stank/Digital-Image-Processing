import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
I = cv2.imread('auto.jpg')  # Reads in BGR format

# Convert to RGB for correct display in matplotlib
I_rgb = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

# Show original image
plt.figure()
plt.imshow(I_rgb)
plt.title('Original Image')
plt.axis('off')


# Convert to Grayscale (manual)
def to_grayscale(img):
    gray = (0.2989 * img[:, :, 2] + 0.5870 * img[:, :, 1] + 0.1140 * img[:, :, 0]).astype(np.uint8)
    return gray

gray_image = to_grayscale(I)
plt.figure()
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Convert to Black and White (thresholding)
def to_black_white(gray_img, threshold):
    bw = (gray_img > threshold).astype(np.uint8) * 255
    return bw

bw_image = to_black_white(gray_image, 128)
plt.figure()
plt.imshow(bw_image, cmap='gray')
plt.title('Black and White Image')
plt.axis('off')

# Remove one color channel
def remove_channel(img, channel):
    modified = img.copy()
    if channel == 'R':
        modified[:, :, 2] = 0
    elif channel == 'G':
        modified[:, :, 1] = 0
    elif channel == 'B':
        modified[:, :, 0] = 0
    modified_rgb = cv2.cvtColor(modified, cv2.COLOR_BGR2RGB)
    plt.figure()
    plt.imshow(modified_rgb)
    plt.title(f'Image without {channel} channel')
    plt.axis('off')

remove_channel(I, 'R')
remove_channel(I, 'G')
remove_channel(I, 'B')

plt.show()
