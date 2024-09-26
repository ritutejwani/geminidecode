from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the API key for google.generativeai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image, prompt):
    # Use the new model 'gemini-1.5-flash'
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content([input_text, image, prompt])
    return response.text

# Set up the Streamlit page
import streamlit as st

st.write("This is a test app")

st.set_page_config(page_title="LangDecode: Multilanguage Document Extraction by Gemini Pro 1.5")
st.header("LangDecode: Multilanguage Document Extraction by Gemini Pro 1.5")

uploaded_file = st.file_uploader("Choose an image of the document", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the document")

input_prompt = """You are an expert in understanding invoices.
We will upload an image as an invoice and you will have to answer any questions based on the uploaded invoice image.
"""

text = """Utilizing Gemini Pro AI, this project effortlessly extracts vital information 
from diverse multilingual documents, transcending language barriers with precision and 
efficiency for enhanced productivity and decision-making."""

styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

if submit and image is not None:
    response = get_gemini_response(input_prompt, image, "")
    st.subheader("The response is")
    st.write(response)
else:
    if submit:
        st.write("Please upload an image before submitting.")