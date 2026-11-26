"""Round 2 check. Run: python session-04/round_2/check.py

This runs ask_once.py for real, so a pass costs a tiny fraction of a cent.
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

result = subprocess.run([sys.executable, str(HERE / "ask_once.py")], capture_output=True, text=True)
last_line = (result.stderr.strip().splitlines() or [""])[-1]

if result.returncode == 0 and result.stdout.strip():
    print("The model said:", result.stdout.strip())
    print("PASS: Round 2. Fill in the notes on your card.")
else:
    print("NOT YET: ask_once.py still stops with an error. Its last line:")
    print("   ", last_line or "(no error message)")
