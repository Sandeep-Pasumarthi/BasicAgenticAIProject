from langgraph.graph import START, END, StateGraph
from src.basic.state.basic_graph_state import BasicGraphState
from src.basic.nodes.basic_graph_node import BasicGraphNode


class GraphBuilder:
    def __init__(self, model):
        self.model = model
    
    def _build_basic_chatbot(self):
        self._basic_graph_builder = StateGraph(BasicGraphState)
        self.basic_node = BasicGraphNode(self.model)
        self._basic_graph_builder.add_node("chatbot", self.basic_node.process)
        self._basic_graph_builder.add_edge(START, "chatbot")
        self._basic_graph_builder.add_edge("chatbot", END)
        return self._basic_graph_builder.compile()
    
    def get_usecase_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            return self._build_basic_chatbot()
