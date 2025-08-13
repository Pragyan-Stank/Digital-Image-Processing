# Huffman Coding for Image Compression

## Overview
Huffman coding is a lossless data compression algorithm that assigns variable-length codes to symbols based on their frequencies. In image processing, it helps reduce storage size without losing information.

This project implements **Huffman coding from scratch** for grayscale images.

---

## Steps
1. **Read Image**
   - The image is loaded in grayscale using OpenCV.
   
2. **Calculate Frequency of Pixel Values**
   - Count how many times each pixel value (0–255) occurs.

3. **Build Huffman Tree**
   - Create a priority queue (min-heap) based on pixel frequencies.
   - Merge nodes until one root node remains.

4. **Generate Huffman Codes**
   - Traverse the Huffman tree to assign binary codes to each pixel value.

5. **Encode Image**
   - Replace each pixel with its corresponding Huffman code.

6. **Decode Image (Optional)**
   - Reverse the process to reconstruct the original image.

---

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

---

## How to Run
```bash
python huffman_coding.py
