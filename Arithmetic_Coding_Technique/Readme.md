# Arithmetic Coding for Images (from Scratch)

This repository implements **Arithmetic Coding** for image compression and decompression **from scratch**, without using any specialized compression libraries. The project demonstrates arithmetic coding applied to grayscale images.

## Features
- Pure Python implementation (no external compression libraries).
- Works on grayscale images (PGM or converted JPG → grayscale).
- Arithmetic **encoder** and **decoder** with interval renormalization.
- End-to-end demonstration on uploaded images.
- Compatible with **Google Colab** and Jupyter Notebook.

## How It Works
1. **Upload an image** (`.jpg`, `.png`, etc.).
2. Convert it to **grayscale**.
3. Apply **arithmetic coding** to compress it.
4. Decode it back to reconstruct the original image.
5. Compare original vs reconstructed and calculate compression ratio.

## Files
- `arithmetic_image_coding_implementation.ipynb` → Jupyter Notebook with full implementation.
- `README.md` → Project description.

## Running on Google Colab
1. Open [Google Colab](https://colab.research.google.com/).
2. Upload the `arithmetic_image_coding.ipynb` file.
3. Upload your image file in Colab using:
   ```python
   from google.colab import files
   uploaded = files.upload()
