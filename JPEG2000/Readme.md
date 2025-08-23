# JPEG Compression from Scratch

This project implements a **simplified JPEG compression and decompression pipeline** in Python without relying on built-in image compression libraries. It demonstrates the core concepts of JPEG such as **color space conversion**, **block splitting**, **Discrete Cosine Transform (DCT)**, **quantization**, and **inverse transformation**.

## 🚀 Features
- Convert RGB images to **YCbCr color space**.
- Split image into **8×8 blocks** for processing.
- Apply **2D DCT (Discrete Cosine Transform)**.
- Quantize using **standard JPEG quantization matrices** for luminance and chrominance.
- Reconstruct the image using **inverse DCT and dequantization**.
- Adjustable **compression quality** factor.
- Compare **original vs reconstructed images** and compute size reduction.

## 🛠️ Requirements
Make sure you have Python 3 installed, along with the following libraries:

```bash
   pip install numpy pillow matplotlib scipy
```

## ▶️ Usage
1. Place an image named `input.jpg` in your working directory.  
2. Run the script:
   ```bash
   python JPEG2000_implementation.py
   ```
3. The script will:
   - Compress and decompress the image.
   - Save the result as output.jpeg.
   - Print original and compressed file sizes.
   - Display a side-by-side comparison of the original and reconstructed image.
