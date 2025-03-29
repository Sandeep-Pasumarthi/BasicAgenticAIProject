from langchain_groq import ChatGroq

import streamlit as st


class GroqLLM:
    def __init__(self, user_controls):
        self.user_controls = user_controls
    
    def get_llm(self):
        try:
            api_key = self.user_controls["GROQ_API_KEY"]
            model = self.user_controls["selected_model"]
            llm = ChatGroq(model=model, api_key=api_key)
            return llm
        except Exception as e:
            st.error(f"Error: {e}")
