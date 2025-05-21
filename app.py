import streamlit as st
import pytesseract
from PIL import Image
import os
from datetime import datetime

# Configure path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ensure 'output' directory exists
os.makedirs("output", exist_ok=True)

# Set page config
st.set_page_config(page_title="OCR Image Text Extractor", layout="centered")

# Title and description
st.title("🖼️ OCR Image Text Extractor")
st.markdown("Extract text from images in **English** and **Hindi** using Tesseract OCR.")

# Choose input method
input_method = st.radio("Choose input method:", ["Upload Image", "Enter Image Path"])

image = None
file_name = None

# Upload option
if input_method == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            file_name = uploaded_file.name
        except Exception as e:
            st.error(f"Error opening uploaded file: {e}")

# Path option
elif input_method == "Enter Image Path":
    image_path = st.text_input("Enter full path to the image")
    if image_path:
        if not os.path.exists(image_path):
            st.error("❌ File does not exist. Please check the path.")
        else:
            try:
                image = Image.open(image_path)
                file_name = os.path.basename(image_path)
            except Exception as e:
                st.error(f"Error opening image: {e}")

# Process and display
if image:
    st.image(image, caption="Selected Image", use_column_width=True)

    # OCR
    extracted_text = pytesseract.image_to_string(image, lang="eng+hin")

    # Display result
    st.subheader("📜 Extracted Text")
    st.text_area("Text", extracted_text, height=250)

    # Save to file
    if st.button("💾 Save to File"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = os.path.splitext(file_name)[0].replace(" ", "_")
        output_path = f"output/ocr_output_{safe_name}_{timestamp}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(extracted_text)
        st.success(f"✅ Text saved to `{output_path}`")
