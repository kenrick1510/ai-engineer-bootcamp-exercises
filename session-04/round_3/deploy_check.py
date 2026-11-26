"""Round 3 check: run the app the way a deploy host would.

Run: python session-04/round_3/deploy_check.py

A deploy host starts with an empty environment, installs only what
requirements.txt lists, and then runs the app. This script does the same
thing in a throwaway environment. It takes about half a minute.
"""

import subprocess
import sys
import venv
from pathlib import Path

HERE = Path(__file__).parent
CLEAN_ENV = Path.home() / ".gauntlet" / "deploy_host"

print("1. Building an empty environment ...")
venv.EnvBuilder(with_pip=True, clear=True).create(CLEAN_ENV)
python = CLEAN_ENV / "bin" / "python"

wanted = [
    line.strip()
    for line in (HERE / "requirements.txt").read_text().splitlines()
    if line.strip() and not line.strip().startswith("#")
]
print("2. Installing what requirements.txt lists:", ", ".join(wanted) or "(nothing)")
if wanted:
    install = subprocess.run(
        [str(python), "-m", "pip", "install", "--quiet", "-r", str(HERE / "requirements.txt")],
        capture_output=True,
        text=True,
    )
    if install.returncode != 0:
        print(install.stderr.strip().splitlines()[-1])
        print("NOT YET: one of the lines in requirements.txt could not be installed. Check the spelling.")
        sys.exit(1)

print("3. Running the app in that environment ...\n")
result = subprocess.run([str(python), str(HERE / "usage_table.py")], capture_output=True, text=True)
print(result.stdout + result.stderr)

if result.returncode == 0 and "Total tokens: 17140" in result.stdout:
    print("PASS: Round 3. It works here, and it works there.")
else:
    print("NOT YET: the app runs in your Codespace but not on the deploy host.")
    print("Read the last line of the error. What does the other machine not have?")
