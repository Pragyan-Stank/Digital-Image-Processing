### **📄 Shannon–Fano README.md**
```markdown
# Shannon–Fano Coding for Image Compression

## Overview
Shannon–Fano coding is a lossless compression technique that assigns binary codes to symbols based on their probability. It sorts symbols by frequency and recursively divides them into two groups with equal probability.

This project implements **Shannon–Fano coding from scratch** for grayscale images.

---

## Steps
1. **Read Image**
   - The image is loaded in grayscale using OpenCV.

2. **Calculate Frequency of Pixel Values**
   - Count occurrences of each pixel value (0–255).

3. **Sort by Frequency**
   - Arrange symbols in descending order of frequency.

4. **Recursive Partitioning**
   - Split the list into two parts with roughly equal total probabilities.
   - Assign `0` to the first half and `1` to the second half.

5. **Generate Codes**
   - Repeat the partitioning recursively until all symbols have unique binary codes.

6. **Encode and Decode**
   - Encode the image using generated codes.
   - Decode to reconstruct the original image.

---

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

---

## How to Run
```bash
python shannon_fano_coding.py
