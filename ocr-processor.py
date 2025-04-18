import pytesseract

def process_ocr_data(extracted_text):
    try:
        # Use Tesseract OCR for further processing if needed
        processed_data = pytesseract.image_to_string(extracted_text)
        return processed_data.splitlines()
    except Exception as e:
        print(f"Error processing OCR data: {e}")
        return []
