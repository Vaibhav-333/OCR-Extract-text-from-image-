# 🖼️ OCR Image Text Extractor

A simple Streamlit web app that extracts text from images using Tesseract OCR with support for English and Hindi.

How to run streamlit app?---->
streamlit run app.py

How to run main file?---->
python main.py image


## 🚀 Features

- Upload an image or enter a local image path
- Extracts text using Tesseract OCR (`eng` + `hin`)
- View the extracted text in the browser
- Save output as a `.txt` file
- Supports `.png`, `.jpg`, `.jpeg`

## 📦 Requirements

Make sure the following are installed:

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to system path
  - For Windows, install from: https://github.com/UB-Mannheim/tesseract/wiki
  - Ensure Hindi (`hin`) language data is installed (can be selected during install or added manually)
- pip packages from `requirements.txt`

## 🔧 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Vaibhav-333/OCR-Extract-text-from-image-
cd OCR-Extract-text-from-image-
