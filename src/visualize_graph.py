import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from linear import app

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
OUTPUT_MMD  = os.path.join(BASE_DIR, "graph.mmd")
OUTPUT_HTML = os.path.join(BASE_DIR, "graph.html")

print("\n" + "=" * 70)
print("LANGGRAPH - LINEAR WORKFLOW VISUALIZATION")
print("=" * 70)

# 1. Get Mermaid source from LangGraph
mermaid_source = app.get_graph().draw_mermaid()

print("\n--- Mermaid Diagram (LangGraph) ---\n")
print(mermaid_source)

# 2. Save raw Mermaid source to .mmd file
with open(OUTPUT_MMD, "w") as f:
    f.write(mermaid_source)
print(f"Mermaid source saved to: {os.path.abspath(OUTPUT_MMD)}")

# 3. Save as self-contained HTML with embedded Mermaid JS
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>LangGraph - Linear Workflow</title>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <style>
    body {{
      font-family: Arial, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px;
      background: #f9f9f9;
    }}
    h1 {{ color: #333; }}
    .mermaid {{
      background: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }}
  </style>
</head>
<body>
  <h1>LangGraph Linear Workflow</h1>
  <div class="mermaid">
{mermaid_source}
  </div>
  <script>
    mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
  </script>
</body>
</html>"""

with open(OUTPUT_HTML, "w") as f:
    f.write(html_content)
print(f"HTML visualization saved to: {os.path.abspath(OUTPUT_HTML)}")
print("\nOpen graph.html in a browser to view the interactive diagram.")
