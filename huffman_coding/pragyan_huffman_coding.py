import cv2
import numpy as np
import heapq
from collections import Counter
import matplotlib.pyplot as plt

# Node structure for Huffman Tree
class Node:
    def __init__(self, value, freq):
        self.value = value      # Pixel value (0–255) or None for internal nodes
        self.freq = freq        # Frequency of occurrence
        self.left = None        # Left child
        self.right = None       # Right child

    def __lt__(self, other):
        # This makes Node comparable based on frequency (needed for heapq)
        return self.freq < other.freq

# Function to build Huffman Tree from frequency dictionary
def build_huffman_tree(freq_dict):
    # Create a min-heap of nodes from the frequency dictionary
    heap = [Node(val, freq) for val, freq in freq_dict.items()]
    heapq.heapify(heap)

    # Keep combining two smallest nodes until only one node remains (root)
    while len(heap) > 1:
        left = heapq.heappop(heap)   # Smallest frequency node
        right = heapq.heappop(heap)  # Second smallest frequency node

        # Create a merged node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged) # Push back into the heap

    return heap[0]  # Root node of the Huffman Tree

# Function to generate Huffman codes from the tree
def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    # Leaf node → assign its Huffman code
    if node.value is not None:
        codes[node.value] = current_code
        return

    # Recursive calls for left and right subtrees
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes

# Function to encode image pixels into Huffman bitstring
def huffman_encode(pixels, codes):
    return ''.join(codes[p] for p in pixels)

# Function to decode Huffman bitstring back into pixel values
def huffman_decode(encoded_str, codes):
    # Reverse mapping: code → pixel value
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_pixels = []

    for bit in encoded_str:
        current_code += bit
        # When current code matches, append the pixel value
        if current_code in reverse_codes:
            decoded_pixels.append(reverse_codes[current_code])
            current_code = ""

    return decoded_pixels

# -------------------------------
# Step 1: Read input image
# -------------------------------
img = cv2.imread("./input_img.jpg", cv2.IMREAD_GRAYSCALE)  # Read as grayscale
if img is None:
    raise FileNotFoundError("Image not found!")

# Flatten the image to a 1D array of pixel values
pixels = img.flatten()

# Step 2: Create frequency dictionary for pixel values
freq_dict = Counter(pixels)

# Step 3: Build Huffman Tree and get codes
root = build_huffman_tree(freq_dict)
codes = generate_codes(root)

# Step 4: Encode the image
encoded_str = huffman_encode(pixels, codes)

# Step 5: Decode the bitstring back into pixels
decoded_pixels = huffman_decode(encoded_str, codes)
decoded_img = np.array(decoded_pixels, dtype=np.uint8).reshape(img.shape)

# Step 6: Display original and decoded images
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(decoded_img, cmap='gray')
plt.title("Decoded Image (Huffman)")
plt.axis('off')
plt.show()

# Step 7: Print compression statistics
original_size = len(pixels) * 8  # Each pixel = 8 bits
compressed_size = len(encoded_str)  # Length of encoded bitstring
print("Original size (bits):", original_size)
print("Compressed size (bits):", compressed_size)
print("Compression ratio:", round(original_size / compressed_size, 2))
