
import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


st.title("ML Batch's Medical Bot")

def createmodel(user):
    API = os.getenv("API_KEY")
    genai.configure(api_key=API)

    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash-lite',
        system_instruction="""
                            You are a medical assistant chatbot.
                            - Provide general medical information only.
                            - Do not diagnose.
                            - Do not prescribe medicines.
                            - Always suggest consulting a doctor.
                            - Reply in a paragraph format.
                            """)
    response = model.generate_content(user)
    cleaned_text = response.candidates[0].content.parts[0].text
    return cleaned_text

user = st.text_input("Ask a question.")

if user:
    result = createmodel(user)
    st.text(result)
