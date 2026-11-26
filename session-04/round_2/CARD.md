# Round 2

**What you see.** This script asks the model one question. It stops with an error.

```
python session-04/round_2/ask_once.py
```

**Your task.** Find out why, and get an answer from the model. Your assistant is allowed, and so is the terminal.

**One rule, with no exceptions:** never paste a key into an assistant to help it.

**Done when** this prints PASS:

```
python session-04/round_2/check.py
```

## My notes

- What kind of problem is this, going by the last line of the error? An API authentication problem (HTTP 401), indicating that the service rejected the API key.
- What did my assistant tell me to do? Did that fix it?
The assistant suggested checking for hidden .env files using ls -a, removing the incorrect .env file inside round_2, and rerunning the script. I still need to verify the fix.
- What was really wrong, in one sentence:
The script was loading a local .env file containing an invalid API key instead of the valid .env file at the repository root.
- The command that showed me:
ls -a
- Did the assistant finish the job, or send me to check something?
The assistant sent me to check the local directory because it could not see my hidden configuration files from the stack trace alone
## Hints

Try for three minutes before you open one.

<details>
<summary>Hint 1</summary>

Read the last line of the trace. There is a three-digit number in it. 401 means the service does not know who you are: the key it was sent is not a good one.

But `setup_check.py` said "All set!" a few minutes ago, so your key works. Which key did this script send?

</details>

<details>
<summary>Hint 2</summary>

Read the comment above `load_dotenv()` in `ask_once.py`. The script reads the nearest `.env` file. Nearest to what?

Move into the round's folder and ask the terminal where you are and what is here, hidden files included:

```
cd session-04/round_2
pwd
ls -a
```

Files whose names start with a dot are hidden from a plain `ls`.

</details>

<details>
<summary>Hint 3</summary>

There is a `.env` file in this folder, and it holds a dead key. The script finds this file first, so it never reaches your real `.env` at the top of the repository. Look at it, remove it, go back to the top folder, and run the script again:

```
cat .env
rm .env
cd ../..
python session-04/round_2/ask_once.py
```

</details>
