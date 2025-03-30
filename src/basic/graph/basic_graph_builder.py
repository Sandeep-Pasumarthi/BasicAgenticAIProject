from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from src.basic.state.basic_graph_state import BasicGraphState
from src.basic.nodes.basic_graph_node import BasicGraphNode
from src.basic.nodes.graph_node_with_tools import LLMToolGraphNode
from src.basic.tools.search_tools import get_tavily_search


class GraphBuilder:
    def __init__(self, model):
        self.model = model
    
    def _build_basic_chatbot(self):
        self._basic_graph_builder = StateGraph(BasicGraphState)
        self._basic_node = BasicGraphNode(self.model)
        self._basic_graph_builder.add_node("chatbot", self._basic_node.process)
        self._basic_graph_builder.add_edge(START, "chatbot")
        self._basic_graph_builder.add_edge("chatbot", END)
        return self._basic_graph_builder.compile()
    
    def _build_search_chatbot(self):
        tools = [get_tavily_search()]
        self._search_graph_builder = StateGraph(BasicGraphState)
        self._search_node = LLMToolGraphNode(self.model, tools)
        self._search_graph_builder.add_node("chatbot", self._search_node.process)
        self._search_graph_builder.add_node("tools", ToolNode(tools=tools))
        self._search_graph_builder.add_edge(START, "chatbot")
        self._search_graph_builder.add_conditional_edges("chatbot", tools_condition)
        self._search_graph_builder.add_edge("tools", "chatbot")
        return self._search_graph_builder.compile()

    def get_usecase_graph(self, usecase: str):
        match usecase:
            case "Chatbot":
                return self._build_basic_chatbot()
            case "Chatbot with Tavily Search":
                return self._build_search_chatbot()
