"""Round 1 check. Run: python session-04/round_1/check.py"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
EXPECTED = ["Prompting: 70 minutes", "Reading code: 50 minutes", "Git: 46 minutes", "Total: 166 minutes"]

result = subprocess.run([sys.executable, str(HERE / "study_report.py")], capture_output=True, text=True)
missing = [line for line in EXPECTED if line not in result.stdout]

if result.returncode != 0:
    print("NOT YET: the report still stops with an error. Read the last line of the trace.")
elif missing:
    print("NOT YET: the report runs, but these lines are missing or wrong:")
    for line in missing:
        print("   ", line)
    print("Change the code, not study_log.json.")
else:
    print("PASS: Round 1. Fill in the notes on your card.")
