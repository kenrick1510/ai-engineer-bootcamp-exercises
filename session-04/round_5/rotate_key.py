"""Replace the study bot's key. This plays the part of the provider's website.

Run: python session-04/round_5/rotate_key.py

On a real service you would delete the leaked key on its website and create
a new one. Here, one command does both, and the keys are made up.
"""

import random
from pathlib import Path

ENV_FILE = Path(__file__).parent / "practice_repo" / ".env"
digits = random.randint(1000, 9999)
new_key = f"practice-key-NEW-{digits}-not-a-real-key"

lines = ENV_FILE.read_text().splitlines() if ENV_FILE.exists() else []
lines = [line for line in lines if not line.startswith("STUDY_BOT_KEY=")]
ENV_FILE.write_text("\n".join([f"STUDY_BOT_KEY={new_key}", *lines]) + "\n")

print("The old key has been revoked. It will never work again.")
print(f"A new key was created and saved to practice_repo/.env (look for {digits} in it).")
