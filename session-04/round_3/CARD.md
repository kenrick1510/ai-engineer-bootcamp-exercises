# Round 3

**What you see.** The app runs in your Codespace:

```
python session-04/round_3/usage_table.py
```

It crashes on a clean machine. This script plays a deploy host: it builds an empty environment, installs only what `requirements.txt` lists, and runs the app there. It takes about half a minute.

```
python session-04/round_3/deploy_check.py
```

**Your task.** Find out why one machine can run the app and the other cannot. Then make it run in both places. Do not change `usage_table.py`.

**Done when** `deploy_check.py` prints PASS.

## My notes

- The error type and message on the clean machine:
- Why the app works in my Codespace:
- What I changed, and in which file:
- The two environments in this round are:
- Did the assistant finish the job, or send me to check something?

## Hints

Try for three minutes before you open one.

<details>
<summary>Hint 1</summary>

The last line of the error names a module that is missing. It is not missing in your Codespace. So the two machines do not have the same packages.

</details>

<details>
<summary>Hint 2</summary>

Someone installed that package in the Codespace by hand and never wrote it down. See for yourself, then open `requirements.txt` in this round's folder:

```
pip show tabulate
```

The clean machine only installs what `requirements.txt` lists.

</details>

<details>
<summary>Hint 3</summary>

Add one line to `session-04/round_3/requirements.txt`:

```
tabulate
```

Save the file and run `deploy_check.py` again.

</details>
