"""Usage table: what did this week's calls to the model cost in tokens?

Run it from the top folder of the repository:
    python session-04/round_3/usage_table.py
"""

import json
from pathlib import Path

from tabulate import tabulate

USAGE_FILE = Path(__file__).parent / "usage.json"

with open(USAGE_FILE) as file:
    calls = json.load(file)

rows = [[call["day"], call["calls"], call["tokens_in"], call["tokens_out"]] for call in calls]
print(tabulate(rows, headers=["Day", "Calls", "Tokens in", "Tokens out"]))
print("Total tokens:", sum(call["tokens_in"] + call["tokens_out"] for call in calls))
