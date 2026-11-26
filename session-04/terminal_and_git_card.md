# Terminal and Git card

The slides name the questions. This card has the commands.

## The terminal answers questions

| The question | The command | What you get |
| --- | --- | --- |
| Where am I? | `pwd` | The folder the terminal is in right now |
| What is here? | `ls` | The files and folders in this folder |
| What is hidden here? | `ls -a` | The same, plus names that start with a dot |
| Go somewhere else | `cd session-04` and `cd ..` | Move into a folder; move up one folder |
| Run this | `python some_file.py` | Runs a Python file |
| Install this | `pip install some_package` | Adds a package to this environment |
| What is this variable? | `echo $HOME` or `printenv` | The value of one environment variable; all of them |

Two more that help tonight: `cat some_file` prints a file, and `rm some_file` deletes one. There is no undo for `rm`.

"Command not found" or "No such file or directory" usually means the wrong folder. Ask the first two questions before anything else.

## Git: three places

Your folder, your commits (snapshots with messages), and GitHub (a copy of the snapshots).

| | The command | What it does |
| --- | --- | --- |
| Read | `git status` | What has changed since the last commit |
| Read | `git log --oneline` | The list of commits, newest first |
| Read | `git diff` | The exact lines that changed |
| Read | `git show abc1234` | What one commit changed. Use a short code from the log |
| Write | `git add some_file.py` | Choose what goes in the next commit |
| Write | `git commit -m "A short message"` | Save a snapshot |
| Write | `git push` | Copy your commits to GitHub. The Sync button does this |
| Undo | `git restore some_file.py` | Throw away changes you have not committed |

In the editor, **Commit** is `add` and `commit` together, and **Sync Changes** is `push` (and `pull`). Commit alone does not reach GitHub, which is why a live app does not change until you sync.

Check before every commit: `git status`. If `.env` is in the list, stop.
