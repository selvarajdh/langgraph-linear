# ====================================
# IMPORTS
# ====================================
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
import operator
import re

class AgentState(TypedDict):
    """
    The state schema for our workflow
    The defines what data our graph will work with.
    """

    messages: Annotated[list, operator.add]
    user_input: str
    processing_step: str
    result: str

print(" State schema defined")
print(f" - messages: accumulates conversation history")
print(f" - user_input: stores the original query")
print(f" - processing_step: tracks workflow progress")
print(f" - result: stores the final output\n")

def input_node(state: AgentState) -> AgentState:
    """
    Node 1: Process the input and prepare for analysis
    """
    print(f" INPUT NODE: Received '{state['user_input']}'")

    return {
        "messages": [HumanMessage(content=state["user_input"])],
        "processing_step": "input_received"
    }

def analyze_node(state: AgentState) -> AgentState:
    """
    Node 2: Analyze the input (simplified for demo)
    """
    print(f" ANALYZE NODE: Analyzing input....")

    user_text = state["user_input"].lower()

    words = re.findall(r'\b\w+\b', user_text)
    #simple analysis logic
    if "weather" in user_text:
        analysis = "Weather-related query detected"
    elif "hello" in words or "hi" in words:
        analysis = "Greeting detected"
    else:
        analysis = "General query detected"

    return {
        "messages": [AIMessage(content=f"Analysis: {analysis}")],
        "processing_step": "analyzed"
    }

def process_node(state: AgentState) -> AgentState:
    """
    Node 3: Process based on the analysis
    """
    print(f" PROCESS NODE: Processing...")

    user_text = state["user_input"].lower()
    words = re.findall(r'\b\w+\b', user_text)

    # Generate a response  based on the input

    if "weather" in user_text:
        response = "I would check the weather API for current conditions."
    elif "hello" in words or "hi" in words:
        response = "Hello! How can I help you today?"
    else:
        response = f"I received your message: '{state['user_input']}'"

    return {
        "messages": [AIMessage(content=response)],
        "processing_step": "processed",
        "result": response
    }

def output_node(state: AgentState) -> AgentState:
    """
    Node 4: Prepare final output
    """
    print(f" OUTPUT NODE: Finalizing response...")

    final_message = f"Final Response {state['result']}"

    return {
        "messages": [AIMessage(content=final_message)],
        "processing_step": "completed"
    }

print("./ Node functions defined:")
print(" - input_node: Receives and processes user input")
print(" - analyze_node: Analyzes the input")
print(" - process_node: Generates appropriate response")
print(" - output_node: Finalazes the output\n")


workflow = StateGraph(AgentState)

workflow.add_node("input", input_node)
workflow.add_node("analyze", analyze_node)
workflow.add_node("process", process_node)
workflow.add_node("output", output_node)

print("./ Nodes added to graph\n")

workflow.set_entry_point("input")

workflow.add_edge("input", "analyze")
workflow.add_edge("analyze", "process")
workflow.add_edge("process", "output")
workflow.add_edge("output", END)

print("./ Workflow edges defined:")
print(" START -> input -> analyze -> process -> output -> END \n")

app = workflow.compile()

print("./ Graph compiled and ready to use\n")
print("=" * 70)



def run_workflow(user_input: str):
    """
    Helper function to run the workflow with given input
    """
    print(f"\n{'=' * 70}")
    print(f"RUNNING WORKFLOW")
    print(f"{'=' * 70}")

    initial_state = {
        "messages": [],
        "user_input": user_input,
        "processing_step": "initialized",
        "result": ""
    }

    final_state = app.invoke(initial_state)

    print(f"\n{'=' * 70}")
    print(f"WORKFLOW COMPLETED")
    print(f"{'*' * 70}")
    print(f"\n = Final State:")
    print(f" - Processing Step: {final_state['processing_step']}")
    print(f" - Result: {final_state['result']}")
    print(f" - Total Messages: {len(final_state['messages'])}")

    return final_state