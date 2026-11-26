"""Rollback check. Run: python session-04/rollback/check.py"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
MARKER = Path.home() / ".gauntlet" / "rollback_applied"

changed = subprocess.run(
    ["git", "status", "--porcelain", "--", "."], cwd=HERE, capture_output=True, text=True
).stdout.strip()
result = subprocess.run([sys.executable, str(HERE / "receipt.py")], capture_output=True, text=True)

if not MARKER.exists():
    print("NOT YET: the bad change has not been applied. Follow the card from step 1.")
elif changed:
    print("NOT YET: this folder still has changes that are not committed:")
    print(changed)
    print("Read the diff to see how much was touched, then roll back.")
elif result.returncode != 0 or "14.71" not in result.stdout:
    print("NOT YET: the receipt does not show a total of 14.71.")
else:
    print(result.stdout.strip().splitlines()[0])
    print("PASS: rolled back. Commit before you let an assistant change more than you can read.")
