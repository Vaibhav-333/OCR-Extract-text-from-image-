import pytesseract
from PIL import Image
import argparse
import os
import sys

# 🔧 Tell pytesseract where the Tesseract-OCR executable is
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    """Extract text from an image file using pytesseract"""
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        sys.exit(1)

    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    text = pytesseract.image_to_string(image lang='eng+hin+deu+fra+ita+spa+por+rus+jpn+kor+chi_sim+chi_tra')
    if not text:
        print("No text found in the image.")
        sys.exit(1)
    return text

def main():
    parser = argparse.ArgumentParser(description="OCR: Extract text from an image")
    parser.add_argument("image_path", help="Path to the image file")
    args = parser.parse_args()

    extracted_text = extract_text_from_image(args.image_path)
    print("\n--- Extracted Text ---\n")
    print(extracted_text)

if __name__ == "__main__":
    main()
