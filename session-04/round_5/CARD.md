# Round 5

**What you see.** A message from your provider:

> We found one of your API keys in a public repository. We have turned it off.

The repository it names is the study bot. That project is its own small Git repository inside this round's folder. Move into it first; every git command in this round runs there.

```
cd session-04/round_5/practice_repo
pwd
ls -a
```

Every key in this round is made up. You never handle a real secret here.

## Part 1: find it (five minutes)

Look through the files for the key. Then work out where a scanner could have found it, and find it yourself.

Then stop, and say where it was. Working from the recording? Watch the next two slides, then come back.

## Part 2: respond, in this order

1. **Replace the key first.** On a real service you would do this on its website. Here, one command plays that part:

   ```
   python ../rotate_key.py
   ```

2. **Stop tracking the file.** Git is still following `.env`, so your new key would be committed next.
3. **Ignore it.** Tell Git never to pick `.env` up again, then commit.

**Done when** this prints PASS:

```
python ../check.py
```

## My notes

- Where the key was (the commit's short code and its message):
The key was stored in an earlier Git commit that contained changes to .env. Run git log --oneline to identify the exact commit ID and message.
- The command that showed me the key:
git log -p -- .env
- Why deleting the line did not fix it:
Deleting the API key from the current file did not remove it from Git history. Anyone with access to the repository could still retrieve the key from an earlier commit.
- The three steps of the response, in order:
1.Rotate the API key to revoke the compromised key and generate a replacement using python ../rotate_key.py.
2.Stop Git from tracking .env using git rm --cached .env.
3.Add .env to .gitignore and commit the changes to prevent future accidental exposure.
- Did the assistant finish the job, or send me to check something?
The assistant instructed me to inspect Git history, rotate the compromised key, stop tracking .env, and update .gitignore. I had to execute the commands and verify the repository's status myself.

## Hints

Try for three minutes before you open one.

<details>
<summary>Hint 1</summary>

The key is in none of today's files. Git remembers more than today. `git log --oneline` lists every commit, newest first, and `git show` followed by a commit's short code shows what that commit changed. One of the messages mentions settings.

</details>

<details>
<summary>Hint 2</summary>

This shows every change ever made to the file, old key included:

```
git log -p -- .env
```

Press `q` to leave the view. That is part 1. For part 2, replace the key with `python ../rotate_key.py`.

</details>

<details>
<summary>Hint 3</summary>

Stop tracking the file without deleting it, ignore it, and commit:

```
git rm --cached .env
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Stop tracking .env and ignore it"
```

Then run `python ../check.py`.

</details>
