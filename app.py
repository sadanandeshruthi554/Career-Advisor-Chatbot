import streamlit as st
from backend.gemini_api import get_response

st.set_page_config(page_title="Career Advisor Chatbot")

st.title("💼 Career Advisor Chatbot")

user_input = st.text_input("Ask your career question:")

if user_input:
    response = get_response(user_input)
    st.write(f"🤖 Bot: {response}")