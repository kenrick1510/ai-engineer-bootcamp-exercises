"""Play the assistant that was asked for one small thing and changed everything.

Run: python session-04/rollback/apply_bad_change.py

The ask was: "Add a discount code to my receipt." This script overwrites
receipt.py and prices.py with what came back.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).parent
MARKERS = Path.home() / ".gauntlet"

for name in ["receipt.py", "prices.py"]:
    shutil.copy(HERE / "bad_change" / name, HERE / name)

MARKERS.mkdir(exist_ok=True)
(MARKERS / "rollback_applied").write_text("applied\n")

print('The assistant says: "Done! I added discount codes, and I also restructured')
print('the code and improved the menu so it is easier to extend."')
print("\nNow run the receipt again.")
