import os
from src.ocr.pdf_extractor import extract_text_from_pdf
from src.ocr.ocr_processor import process_ocr_data
from src.categorizer.expense_categorizer import categorize_expenses
from src.analytics.visualizer import generate_visuals
from src.analytics.report_generator import export_to_excel

def main():
    # Path to the raw PDF
    pdf_path = "data/raw/sample_statement.pdf"
    processed_path = "data/processed/expenses.xlsx"
    
    # Step 1: Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Process OCR data
    ocr_data = process_ocr_data(extracted_text)
    
    # Step 3: Categorize expenses
    categorized_data = categorize_expenses(ocr_data)
    
    # Step 4: Generate visual analytics
    generate_visuals(categorized_data)
    
    # Step 5: Export to Excel
    export_to_excel(categorized_data, processed_path)
    print(f"Processed file saved at {processed_path}")

if __name__ == "__main__":
    main()
