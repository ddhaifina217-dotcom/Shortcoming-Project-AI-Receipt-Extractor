# AI Receipt Information Extractor

This project provides a Streamlit web application that leverages Google's Gemini AI to extract key information (merchant name, date, total amount, currency) from receipt images.

## Features
- **Upload:** Upload a receipt image (`.jpg`, `.jpeg`, `.png`).
- **AI Engine:** Use Gemini AI to automatically extract information.
- **Verification:** Review and edit the extracted data in an interactive form.

## Setup and Installation

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd ai-receipt-extractor
```

### 2. Prepare your Python environment
It's recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install streamlit google-genai pyngrok pillow
```
