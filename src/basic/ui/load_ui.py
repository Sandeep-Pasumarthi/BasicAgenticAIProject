from src.basic.ui.config import Config

import streamlit as st


class LoadStreamLitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {
            "selected_llm": None,
            "selected_groq_model": None,
            "GROQ_API_KEY": None,
            "selected_usecase": None
        }
    
    def initialize_session(self) -> dict:
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }

    def _initialize_state(self) -> None:
        st.session_state.update({
            "timeframe": '',
            "IsFetchButtonClicked": False,
            "IsSDLC": False
        })
        st.session_state.setdefault("state", self.initialize_session())
    
    def _setup_sidebar(self) -> None:
        with st.sidebar:
            st.markdown("### 🛠️ Configure Your Assistant")

            llm_options = self.config.get_llm_options()
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_llm_options()
                self.user_controls["selected_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Enter your GROQ API key to continue. Visit: https://console.groq.com/keys")
            
            usecase_options = self.config.get_usecase_options()
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)
    
    def render_ui(self) -> dict:
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        self._setup_sidebar()
        self._initialize_state()
        return self.user_controls
