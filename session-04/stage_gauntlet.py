"""Set up the Session 4 rounds.

Run it once before you start, from the top folder of the repository:
    python session-04/stage_gauntlet.py

Run it again any time to start rounds 2, 3 and 5 and the rollback
exercise over. It never changes or prints your real API key.

Reading the rest of this file spoils the rounds. Run it now, read it later.
"""

import shutil
import subprocess
import sys
from pathlib import Path

from dotenv import dotenv_values

HERE = Path(__file__).parent
ROOT = HERE.parent
MARKERS = Path.home() / ".gauntlet"

# Both of these are made up. Neither one has ever worked anywhere.
DEAD_KEY = "sk-or-v1-0000-this-key-was-revoked-0000"
OLD_PRACTICE_KEY = "practice-key-OLD-4471-not-a-real-key"


def check_env():
    """The rounds need the three values that setup_check.py saves in .env."""
    saved = dotenv_values(ROOT / ".env")
    missing = [name for name in ("LLM_API_KEY", "LLM_BASE_URL", "LLM_MODEL") if not saved.get(name)]
    if missing:
        print("Not ready yet. Your .env file is missing: " + ", ".join(missing))
        print("From the top folder of the repository, run this first, then run me again:")
        print("    python setup_check.py")
        sys.exit(1)


def stage_round_2():
    """Leave an old settings file in the round's folder."""
    lines = [
        f"LLM_API_KEY={DEAD_KEY}",
        "LLM_BASE_URL=https://openrouter.ai/api/v1",
        "LLM_MODEL=google/gemma-4-26b-a4b-it:floor",
    ]
    (HERE / "round_2" / ".env").write_text("\n".join(lines) + "\n")
    print("Round 2 is set up.")


def stage_round_3():
    """Play the teammate who installed a package by hand and never wrote it down."""
    for extra in ([], ["--break-system-packages"]):
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet", "tabulate", *extra],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("Round 3 is set up.")
            return
    print("Round 3 could NOT be set up: installing a package failed. Tell your instructor.")


def git(folder, *args):
    subprocess.run(
        ["git", "-c", "user.name=Practice Student", "-c", "user.email=student@example.com", *args],
        cwd=folder,
        check=True,
        capture_output=True,
    )


def stage_round_5():
    """Build a small practice repository with five commits."""
    repo = HERE / "round_5" / "practice_repo"
    shutil.rmtree(repo, ignore_errors=True)
    repo.mkdir()
    git(repo, "init", "--quiet", "--initial-branch=main")

    bot = '"""A tiny study bot."""\n\nfrom pathlib import Path\n\n'
    bot += 'settings = dict(line.split("=", 1) for line in Path(".env").read_text().split())\n'
    bot += 'print("Study bot ready. Key ends in", settings["STUDY_BOT_KEY"][-8:] or "(no key)")\n'

    (repo / "README.md").write_text("# Study bot\n\nA practice project.\n")
    (repo / "study_bot.py").write_text(bot)
    git(repo, "add", "-A")
    git(repo, "commit", "--quiet", "-m", "Start the study bot")

    (repo / ".env").write_text(f"STUDY_BOT_KEY={OLD_PRACTICE_KEY}\nSTUDY_BOT_NAME=Sage\n")
    git(repo, "add", "-A")
    git(repo, "commit", "--quiet", "-m", "Add settings")

    (repo / ".env").write_text("STUDY_BOT_KEY=\nSTUDY_BOT_NAME=Sage\n")
    git(repo, "add", "-A")
    git(repo, "commit", "--quiet", "-m", "Remove the key from the settings")

    (repo / "README.md").write_text("# Study bot\n\nA practice project for Session 4.\n\nRun it with: python study_bot.py\n")
    git(repo, "add", "-A")
    git(repo, "commit", "--quiet", "-m", "Tidy the README")

    (repo / "study_bot.py").write_text(bot + 'print("Goodbye!")\n')
    git(repo, "add", "-A")
    git(repo, "commit", "--quiet", "-m", "Add a goodbye message")
    print("Round 5 is set up.")


def stage_rollback():
    """Forget that the bad change was ever applied."""
    marker = MARKERS / "rollback_applied"
    if marker.exists():
        marker.unlink()
    print("The rollback exercise is set up.")


def main():
    check_env()
    MARKERS.mkdir(exist_ok=True)
    print("\nRound 1 is set up.")
    stage_round_2()
    stage_round_3()
    stage_rollback()
    print("\nRound 4 is set up.")
    stage_round_5()
    print("Each round has a card. Round 1's is session-04/round_1/CARD.md")
    print("\nReady.")


if __name__ == "__main__":
    main()
