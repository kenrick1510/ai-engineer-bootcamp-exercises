# Commit and roll back

This is the reason Git is taught in an AI course. A commit is a checkpoint. With a checkpoint behind you, you can let an assistant make a big change, look at what it did, and undo all of it in one command.

**The app.** A receipt printer in two small files. It works.

```
python session-04/rollback/receipt.py
```

**Your task.** Six steps.

1. Open `receipt.py` and change `SHOP_NAME` to a name of your own. Run it again.
2. Commit that change: the Source Control icon, a short message, **Commit**. This is your checkpoint.
3. Let the "assistant" loose. It was asked for one thing: add a discount code.

   ```
   python session-04/rollback/apply_bad_change.py
   ```

4. Run the receipt again. Then look at how much was touched:

   ```
   git status
   git diff --stat
   git diff
   ```

5. Roll back to your checkpoint:

   ```
   git restore session-04/rollback
   ```

6. Run the receipt one more time. Your shop name is back, and so is the right total.

**Done when** this prints PASS:

```
python session-04/rollback/check.py
```

## My notes

- How many files changed, and how many lines (from `git diff --stat`):
- Two things the change did that nobody asked for:
- Would I have found all of it by reading? How long would that take?
- The rule, in my own words:

## Hints

<details>
<summary>Hint 1</summary>

`git restore` only undoes changes you have not committed. That is why step 2 comes first: the commit is what you roll back to.

</details>

<details>
<summary>Hint 2</summary>

Run the git commands from the top folder of the repository. Not sure where you are? `pwd` tells you, and `cd /workspaces/` followed by your repository's name takes you back.

</details>

<details>
<summary>Hint 3</summary>

In the editor you can do the same thing with the mouse: open Source Control, and next to "Changes" click the curved arrow, **Discard All Changes**.

</details>
