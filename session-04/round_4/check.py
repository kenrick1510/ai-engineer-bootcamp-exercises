"""Round 4 check. Run: python session-04/round_4/check.py

It runs quiz_bot.py once, so it takes as long as your bot does.
"""

import hashlib
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
PRACTICE_API_SHA = "e97b654dc4ccf5eb5db7c85f71f93073d09889a1823b207aee4a6535d0ed18bb"

source = (HERE / "quiz_bot.py").read_text()
api_unchanged = hashlib.sha256((HERE / "practice_api.py").read_bytes()).hexdigest() == PRACTICE_API_SHA

print("Running quiz_bot.py ...")
result = subprocess.run([sys.executable, str(HERE / "quiz_bot.py")], capture_output=True, text=True)
output = result.stdout + result.stderr
answered = output.count("A: ")
uses_logging = "import logging" in source and ("logging." in source.replace("import logging", "") or "logger." in source)

if not api_unchanged:
    print("NOT YET: practice_api.py was changed. It stands in for a service you do not control.")
    print("Put it back with: git restore session-04/round_4/practice_api.py")
elif not uses_logging:
    print("NOT YET: the bot still does not log. Replace the print in the except block with a log line")
    print("that records the real error. Then run the bot and read what the log says.")
elif result.returncode != 0:
    print("NOT YET: the bot stopped with an error:")
    print("   ", (result.stderr.strip().splitlines() or ["(no message)"])[-1])
elif answered < 5:
    print(f"NOT YET: {answered} of 5 questions were answered. Your log should now say why.")
    print("What does that status code ask you to do?")
else:
    print("PASS: Round 4. Copy the log line that named the cause onto your card.")
