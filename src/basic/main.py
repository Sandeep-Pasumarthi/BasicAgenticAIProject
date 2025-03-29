from src.basic.ui.load_ui import LoadStreamLitUI
from src.basic.ui.results_ui import DisplayResultsStreamLitUI
from src.basic.llms.groq import GroqLLM
from src.basic.graph.basic_graph_builder import GraphBuilder

import streamlit as st


def load_ui():
    ui = LoadStreamLitUI()
    user_input = ui.render_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")
    
    if user_message:
        llm = GroqLLM(user_controls=user_input)
        llm = llm.get_llm()

        if not llm:
            st.error("Error: LLM model could not be initialized")
            return
        
        usecase = user_input.get("selected_usecase")

        if not usecase:
            st.error("Error: No usecase selected")
        
        graph_builder = GraphBuilder(llm)
        graph = graph_builder.get_usecase_graph(usecase=usecase)
        results = DisplayResultsStreamLitUI(usecase=usecase, graph=graph, user_message=user_message)
        results.render_ui()
