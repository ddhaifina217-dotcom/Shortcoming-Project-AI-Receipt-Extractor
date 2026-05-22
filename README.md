# AI Receipt Information Extractor

This project provides a Streamlit web application that leverages Google's Gemini AI to extract key information (merchant name, date, total amount, currency) from receipt images.

## AI Configuration (Assessment Criteria)
- **Model Used:** `gemini-2.5-flash` (Chosen for high-velocity multimodal token processing)
- **Prompt Architecture:** 
  ```text
  Analyze this receipt image and extract the following fields. 
  Return the result STRICTLY as a raw JSON object with keys: 
  "merchant_name", "date", "total_amount", and "currency". 
  Do not wrap the response in markdown code blocks or ```json text strings.
  If a field cannot be found, leave its value as an empty string.
  ```

## Core Features
- **Upload:** Upload a receipt image (`.jpg`, `.jpeg`, `.png`).
- **AI Engine:** Use Gemini AI to automatically extract unstructured financial details.
- **Verification:** Review and manually edit the extracted data in an interactive form.

## Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com
cd Shortcoming-Project-AI-Receipt-Extractor
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
