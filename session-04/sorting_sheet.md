# Sorting sheet: two territories

For the end of the session, after Round 5.

Name:

Every failure tonight belongs in one of two places.

- **Inside the paste.** The cause is in the code or the error you can show an assistant. Paste it, judge the diagnosis, apply the smallest fix.
- **Around the code.** The cause is in the world the code runs in: a key, an account, a package, a folder, another machine, the Git history. An assistant cannot see it unless you show it or check it yourself.

## Sort tonight's failures

For each one, write **inside** or **around**, and what the assistant would have needed to see.

| Failure | Inside or around? | What would an assistant have needed to see? |
| --- | --- | --- |
| Round 1: the report stops with `ValueError` | | |
| Round 2: the script stops with a 401 | | |
| Round 3: works in the Codespace, crashes on the clean machine | | |
| Round 4: "Something went wrong." | | |
| Round 5: the key that was deleted but not gone | | |
| The bad change in the rollback exercise | | |

## The first check on each side

Inside the paste:

1.
2.
3.

Around the code (which folder, which environment, which key, which status code, what Git says):

1.
2.
3.
4.
5.

## The question to ask before you paste anything

Write it in your own words:

## To keep

Three status codes:

| Code | It means | Whose problem |
| --- | --- | --- |
| 401 | The service does not know who you are | Your key. Never your code |
| 429 | Slow down | Too many requests too quickly. Wait |
| 500 | Something broke on their side | The service. Try again later |

A committed secret, in order:

1. Replace the key. It is burned, even if the line was deleted.
2. Stop tracking the file: `git rm --cached .env`
3. Ignore it: add `.env` to `.gitignore`, and commit.

Check before every commit: `git status`. If `.env` is in the list, stop.

## Hand it in

1. Commit this file and your cards, then click **Sync Changes**.
2. Post three lines in the Session 4 thread in Discord:
   - the link to your fork
   - your model, its provider, and that provider's data policy
   - one failure tonight that an assistant could not have seen, and what it would have needed
