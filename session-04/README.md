# Session 4: five broken apps

Five small broken apps, and one exercise in rolling back. Nobody tells you what is wrong with an app before you run it. Finding out is the round.

## Before you start

From the top folder of the repository, type these two commands, one at a time:

```
python setup_check.py
python session-04/stage_gauntlet.py
```

The first checks that your key still works and brings your `.env` file up to date. Wait for "All set!" The second sets up the rounds. Wait for "Ready." Run the second one again any time to start the rounds over.

The Round 2 check makes one real call to your model, which costs a tiny fraction of a cent. Nothing else in this folder uses your real key.

## The rounds

| Order | Folder | What you see |
| --- | --- | --- |
| Round 1 | `round_1` | The report stops with an error |
| Round 2 | `round_2` | The script cannot get an answer |
| Round 3 | `round_3` | Works here, crashes there |
| Round 4 | `round_4` | "Something went wrong." |
| Exercise | `rollback` | Commit, apply a big bad change, roll back |
| Round 5 | `round_5` | A key got out |

## How each round works

1. Open the round's `CARD.md`. Right-click it and choose **Open Preview** to hide the hints until you want them.
2. Read what you see and the task. Run it. Try to find out what is wrong.
3. Stuck for three minutes? Open hint 1. The third hint is nearly the answer. Nobody should lose more than ten minutes to one round.
4. Run the round's check. It prints PASS when you are done.
5. Fill in "My notes" on the card.

Assistants are allowed in every round. One rule has no exceptions: never paste a key into an assistant.

One question goes with every round, and it is the last note on every card: did the assistant finish the job, or did it send you to check something?

## Working from the recording

Each round has its own slide. Pause the recording there, do the round, and come back when the check prints PASS, or after ten minutes. The walkthrough comes right after the pause.

## Also in this folder

- `terminal_and_git_card.md`: the commands
- `sorting_sheet.md`: for the end of the session, after Round 5

## Hand it in

1. Commit your cards and the sorting sheet, then click **Sync Changes**.
2. Post three lines in the Session 4 thread in Discord:
   - the link to your fork
   - your model, its provider, and that provider's data policy
   - one failure tonight that an assistant could not have seen, and what it would have needed
