import streamlit as st


class DisplayResultsStreamLitUI:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message  = user_message

        st.session_state.setdefault("chat_history", [])
    
    def render_ui(self):
        if self.usecase == "Basic Chatbot":
            if not st.session_state.chat_history or st.session_state.chat_history[-1]["content"] != self.user_message:
                st.session_state.chat_history.append({"role": "user", "content": self.user_message})

                for event in self.graph.stream({"messages": {"role": "user", "content": self.user_message}}):
                    for value in event.values():
                        st.session_state.chat_history.append({"role": "assistant", "content": value["messages"].content})
            
            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])
