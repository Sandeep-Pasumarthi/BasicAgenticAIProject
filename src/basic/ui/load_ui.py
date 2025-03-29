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
    
    def _setup_sidebar(self) -> None:
        with st.sidebar:
            st.markdown("### 🛠️ Configure Your Assistant")

            llm_options = self.config.get_llms_details()

            llm_provider = self.user_controls["selected_llm_provider"] = st.selectbox("Select LLM", list(llm_options.keys()))
            self.user_controls["enable_search"] = st.toggle("Enable Online Search", value=False)
            
            if self.user_controls["selected_llm_provider"]:
                if self.user_controls["enable_search"]:
                    model_options = llm_options[llm_provider]["models_with_tools"]
                else:
                    model_options = llm_options[llm_provider]["models"]
                
                if model_options:
                    self.user_controls["selected_model"] = st.selectbox("Select Model", model_options)
                else:
                    st.warning(f"No models available for {self.user_controls['selected_llm_provider']}")
                
                if llm_options[llm_provider]["is_api_key_required"]:
                    self.user_controls[f"{llm_provider}_API_KEY"] = st.session_state[f"{llm_provider}_API_KEY"] = st.text_input(f"{llm_provider} API Key", type="password")
                    if not self.user_controls[f"{llm_provider}_API_KEY"]:
                        st.warning(f"⚠️ Enter your {llm_provider} API key to continue.")

            usecase_options = self.config.get_usecase_options()
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)
    
    def render_ui(self) -> dict:
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        self._setup_sidebar()
        return self.user_controls
