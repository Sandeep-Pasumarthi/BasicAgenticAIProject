from src.basic.state.basic_graph_state import BasicGraphState


class BasicGraphNode:
    def __init__(self, model):
        self.model = model
    
    def process(self, state: BasicGraphState):
        return {"messages": self.model.invoke(state['messages'])}
