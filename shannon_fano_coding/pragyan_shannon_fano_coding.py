import cv2
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import os

# Recursive function to assign Shannon–Fano codes
def shannon_fano_recursive(symbols, codes):
    """
    symbols: List of (pixel_value, frequency) sorted in descending frequency
    codes: Dictionary mapping pixel values to binary codes
    """
    if len(symbols) <= 1:  # Base case: 1 or 0 symbols
        return

    # Step 1: Find total frequency
    total = sum(freq for _, freq in symbols)

    # Step 2: Find split point where total frequency is ~half
    acc = 0
    split_index = 0
    for i, (_, freq) in enumerate(symbols):
        acc += freq
        if acc >= total / 2:  # Close to half total frequency
            split_index = i + 1
            break

    # Step 3: Assign '0' to first half and '1' to second half
    for i in range(split_index):
        codes[symbols[i][0]] += '0'
    for i in range(split_index, len(symbols)):
        codes[symbols[i][0]] += '1'

    # Step 4: Recurse for both halves
    shannon_fano_recursive(symbols[:split_index], codes)
    shannon_fano_recursive(symbols[split_index:], codes)

# Function to encode pixels into Shannon–Fano bitstring
def shannon_fano_encode(pixels, codes):
    return ''.join(codes[p] for p in pixels)

# Function to decode Shannon–Fano bitstring back to pixel values
def shannon_fano_decode(encoded_str, codes):
    reverse_codes = {v: k for k, v in codes.items()}  # Reverse mapping
    current_code = ""
    decoded_pixels = []

    for bit in encoded_str:
        current_code += bit
        if current_code in reverse_codes:
            decoded_pixels.append(reverse_codes[current_code])
            current_code = ""  # Reset for next symbol

    return decoded_pixels

# ---------- Main ----------
image_path = "./input_img.jpg"  # Image file path
if not os.path.exists(image_path):
    raise FileNotFoundError("Image not found!")

# Step 1: Read the image in grayscale mode
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Flatten image into 1D array of pixels
pixels = img.flatten()

# Step 3: Count frequency of each pixel value
freq_dict = Counter(pixels)

# Step 4: Sort symbols by frequency (highest first)
symbols = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

# Step 5: Initialize empty code dictionary
codes = {sym: '' for sym, _ in symbols}

# Step 6: Generate Shannon–Fano codes
shannon_fano_recursive(symbols, codes)

# Step 7: Encode image
encoded_str = shannon_fano_encode(pixels, codes)

# Step 8: Decode bitstring back into pixels
decoded_pixels = shannon_fano_decode(encoded_str, codes)

# Step 9: Convert list back into image shape
decoded_img = np.array(decoded_pixels, dtype=np.uint8).reshape(img.shape)

# Step 10: Display original and decoded images
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(decoded_img, cmap='gray')
plt.title("Decoded Image (Shannon–Fano)")
plt.axis('off')
plt.show()

# Step 11: Print compression statistics
print("Original size (bits):", len(pixels) * 8)  # Each pixel is 8 bits
print("Compressed size (bits):", len(encoded_str))
print("Compression ratio:", round(len(pixels)*8 / len(encoded_str), 2))
