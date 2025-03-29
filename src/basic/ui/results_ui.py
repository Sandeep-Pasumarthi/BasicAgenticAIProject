import streamlit as st


class DisplayResultsStreamLitUI:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message  = user_message
    
    def render_ui(self):
        if self.usecase == "Basic Chatbot":
            for event in self.graph.stream({"messages": {"role": "user", "content": self.user_message}}):
                for value in event.values():
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
