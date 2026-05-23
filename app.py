import streamlit as st
from google import genai
from PIL import Image
import json

# Setup page presentation
st.set_page_config(page_title="AI Receipt Extractor", page_icon="🧾", layout="centered")
st.title("🧾 AI Receipt Information Extractor")
st.write("Upload a receipt to automatically extract and verify details.")

# Sidebar configuration for user control
st.sidebar.header("API Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Keep form memory intact across user updates
if "extracted_data" not in st.session_state:
    st.session_state.extracted_data = {"merchant_name": "", "date": "", "total_amount": "", "currency": ""}

# File Uploader UI
uploaded_file = st.file_uploader("Choose a receipt image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt Source", use_container_width=True)
    
    if st.button("Extract Data using Gemini AI"):
        if not api_key:
            st.error("Please add your Gemini API Key in the sidebar first!")
        else:
            with st.spinner("Analyzing text layout..."):
                try:
                    # Use the official, modern GenAI client
                    client = genai.Client(api_key=api_key)
                    
                    prompt = """
                    Analyze this receipt image and extract the following fields. 
                    Return the result STRICTLY as a raw JSON object with keys: 
                    "merchant_name", "date", "total_amount", and "currency". 
                    Do not wrap the response in markdown code blocks or ```json text strings.
                    If a field cannot be found, leave its value as an empty string.
                    """
                    
                    # Call the stable multimodal model
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    
                    # Clean markdown wrappers out if the model generates them
                    clean_text = response.text.replace("```json", "").replace("```", "").strip()
                    parsed_json = json.loads(clean_text)
                    
                    # Push directly into form memory state
                    st.session_state.extracted_data = parsed_json
                    st.success("Extraction Complete! Review fields below.")
                    
                except Exception as e:
                    st.error(f"Failed to process image: {e}")

# Editable Verification Form (Auto-filled with AI data)
st.header("📋 Review & Edit Extracted Information")

with st.form("receipt_form"):
    merchant = st.text_input("Merchant Name", value=st.session_state.extracted_data.get("merchant_name", ""))
    date = st.text_input("Date", value=st.session_state.extracted_data.get("date", ""))
    total = st.text_input("Total Amount", value=st.session_state.extracted_data.get("total_amount", ""))
    currency = st.text_input("Currency", value=st.session_state.extracted_data.get("currency", ""))
    
    # Form lock & submit mechanism
    submitted = st.form_submit_button("Submit Data")
    
    if submitted:
        saved_record = {
            "merchant_name": merchant,
            "date": date,
            "total_amount": total,
            "currency": currency
        }
        st.success("Data successfully submitted into local session storage!")
        st.json(saved_record)
