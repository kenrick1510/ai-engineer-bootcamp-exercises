"""Round 5 check. Run: python session-04/round_5/check.py"""

import subprocess
from pathlib import Path

REPO = Path(__file__).parent / "practice_repo"
OLD_KEY = "practice-key-OLD-4471-not-a-real-key"


def git(*args):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True).stdout.strip()


if not (REPO / ".git").exists():
    print("NOT YET: the practice repository is missing. Run: python session-04/stage_gauntlet.py")
    raise SystemExit

env_text = (REPO / ".env").read_text() if (REPO / ".env").exists() else ""
key_line = next((line for line in env_text.splitlines() if line.startswith("STUDY_BOT_KEY=")), "")
key = key_line.split("=", 1)[1] if key_line else ""
tracked = git("ls-files").splitlines()
ignore_text = (REPO / ".gitignore").read_text() if (REPO / ".gitignore").exists() else ""
ignored = ".env" in [line.strip() for line in ignore_text.splitlines()]
uncommitted = git("status", "--porcelain")
leak_commit = git("log", "--format=%h %s", "-S", OLD_KEY, "--", ".env").splitlines()

if not key or key == OLD_KEY:
    print("NOT YET: step 1. The leaked key has not been replaced. A leaked key is burned: replace it first.")
elif ".env" in tracked:
    print("NOT YET: step 2. Git is still tracking .env, so the new key would be committed too.")
elif not ignored:
    print("NOT YET: step 3. .env is not in a .gitignore file, so it could be added again by accident.")
elif ".gitignore" not in tracked or uncommitted:
    print("NOT YET: almost. Commit your changes so the repository remembers them:")
    print(uncommitted or "   (.gitignore is not committed)")
else:
    print("PASS: Round 5. The new key is safe, and Git will not pick up .env again.")
    if leak_commit:
        print(f"The old key is still in the history ({leak_commit[-1]}).")
        print("That is why it had to be replaced: deleting a line does not un-leak it.")
