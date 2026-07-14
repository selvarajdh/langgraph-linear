import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from linear import run_workflow

test_cases = [
    # Greeting cases
    ("hello world",             "Greeting"),
    ("hi there",                "Greeting"),
    ("Hi, how are you?",        "Greeting"),
    ("say hello to me",         "General - 'hello' not standalone word... wait, it is"),
    # Weather cases
    ("What is the weather today?",          "Weather"),
    ("weather forecast for tomorrow",       "Weather"),
    ("Is it going to rain? Check weather",  "Weather"),
    # General cases
    ("Tell me something interesting",       "General"),
    ("What is the capital of France?",      "General"),
    ("Explain machine learning",            "General"),
    ("something with hi in the middle",     "General - 'hi' is standalone word here"),
    # Edge cases
    ("",                        "General - empty input"),
    ("HI",                      "Greeting - uppercase"),
    ("HELLO WORLD",             "Greeting - all caps"),
    ("weather hi hello",        "Weather - multiple keywords"),
]

print("\n" + "=" * 70)
print("RUNNING ALL TEST CASES")
print("=" * 70)

for i, (user_input, expected_category) in enumerate(test_cases, 1):
    print(f"\n[Test {i:02d}] Input: '{user_input}'")
    print(f"         Expected Category: {expected_category}")
    try:
        final_state = run_workflow(user_input)
        print(f"         Result: {final_state['result']}")
    except Exception as e:
        print(f"         ERROR: {e}")

print("\n" + "=" * 70)
print("ALL TEST CASES COMPLETED")
print("=" * 70)
