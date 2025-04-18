# Automated-Expense-Detector-from-Bank-Statements
This project converts messy PDF bank statements into clean, categorized expense logs with visual analytics.

## Features
- Extract text from PDF bank statements.
- Categorize transactions based on predefined rules.
- Generate visual analytics.
- Export categorized expenses to Excel.

## Tech Stack
- Python
- PyPDF2 (PDF text extraction)
- Tesseract OCR
- Pandas (data processing)
- Matplotlib (visualization)

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Place your bank statements in `data/raw/`.
4. Run the script: `python src/main.py`

## Advanced Features
- Add new rules in `src/categorizer/rules.json`.
- Modify configuration in `config.yaml`.

## Future Enhancements
- Add support for multi-language OCR.
- Include fraud and recurring expense detection.
