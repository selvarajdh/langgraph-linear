import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from linear import app

print("\n" + "=" * 70)
print("LANGGRAPH - LINEAR WORKFLOW VISUALIZATION")
print("=" * 70)

# ASCII diagram
print("""
--- Graph Flow (ASCII) ---

  +-----------+
  |  __start__  |
  +-----+-----+
        |
        v
  +-----+-----+
  |   input   |   input_node: wraps user_input as HumanMessage
  +-----+-----+
        |
        v
  +-----+-------+
  |   analyze   |   analyze_node: detects Weather / Greeting / General
  +-----+-------+
        |
        v
  +-----+-------+
  |   process   |   process_node: generates response, sets result
  +-----+-------+
        |
        v
  +-----+------+
  |   output   |   output_node: finalizes and marks completed
  +-----+------+
        |
        v
  +-----+-----+
  |  __end__  |
  +-----------+
""")

# Mermaid diagram
print("--- Mermaid Diagram ---\n")
print(app.get_graph().draw_mermaid())
