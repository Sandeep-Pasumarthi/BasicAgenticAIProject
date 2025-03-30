from src.basic.state.basic_graph_state import BasicGraphState


class LLMToolGraphNode:
    def __init__(self, model, tools):
        self.__model = model
        self.model_with_tools = self.__model.bind_tools(tools)
    
    def process(self, state: BasicGraphState):
        return {"messages": [self.model_with_tools.invoke(state['messages'])]}
