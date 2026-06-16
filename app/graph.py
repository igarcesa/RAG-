from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from query import retrieve_context, generate_answer

class GraphState(TypedDict):
    question: str
    context: List[str]
    answer: str

def build_graph():
    workflow = StateGraph(GraphState)

    # Add nodes
    workflow.add_node("retrieve", retrieve_context)
    workflow.add_node("generate", generate_answer)

    # Set edges
    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()

# Compile the graph once and export it
app_graph = build_graph()