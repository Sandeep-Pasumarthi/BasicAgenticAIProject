from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

import streamlit as st


class GetLLM:
    def __init__(self, user_controls):
        self.user_controls = user_controls
        self.selected_llm_provider = user_controls["selected_llm_provider"]
        self.model_api_key = user_controls["LLM_API_KEY"]
        self.model_name = user_controls["selected_model"]
    
    def get_llm(self):
        try:
            match self.selected_llm_provider:
                case "GROQ":
                    return ChatGroq(model=self.model_name, api_key=self.model_api_key)
                case "OPENAI":
                    return ChatOpenAI(model=self.model_name, api_key=self.model_api_key)
                case _:
                    st.error(f"{self.model_name} is not supported")
        except Exception as e:
            st.error(f"Error: {e}")
