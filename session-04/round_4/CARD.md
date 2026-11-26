# Round 4

**What you see.** The quiz bot asks five questions. It answers two, and then says "Something went wrong." three times.

```
python session-04/round_4/quiz_bot.py
```

Do not open or change `practice_api.py`. It stands in for a service you do not control, and you cannot read a real service's code.

## Part 1: find out what went wrong (four minutes)

Try. Your assistant is allowed. Write down what you pasted, and what it asked you for.

Then stop. Part 2 uses a tool we look at together first. Working from the recording? Watch the two slides on logging, then come back.

## Part 2: make the bot say what happened

1. In `quiz_bot.py`, replace the `print("Something went wrong.")` line with a log line that records the real error. Run the bot and read the log.
2. Fix what the log shows, so that all five questions get answers.

**Done when** this prints PASS:

```
python session-04/round_4/check.py
```

## My notes

- In part 1, what did I paste, and what did the assistant ask me for?
- The log line that named the cause (copy it here):
- The status code in it, and what it means:
- What I changed to fix it:
- One thing that must never appear in a log line:
- Did the assistant finish the job, or send me to check something?

## Hints

These are for part 2. Try for three minutes before you open one.

<details>
<summary>Hint 1</summary>

The `except` block catches the error and throws it away. Give the error a name so you can look at it: `except Exception as error:`.

</details>

<details>
<summary>Hint 2</summary>

Set up logging near the top of `quiz_bot.py`, then log the error where the print was:

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
```

```python
    except Exception as error:
        logging.error("ask failed: question=%r error=%s", question, error)
```

Run the bot again. What number is in the log?

</details>

<details>
<summary>Hint 3</summary>

429 means slow down: the service allows 2 requests every 4 seconds. The fix is to wait. Add `import time` at the top, and pause at the end of each turn of the loop, at the same indent as the `try`:

```python
    time.sleep(2.5)
```

Session 7 replaces this fixed wait with automatic retries.

</details>
