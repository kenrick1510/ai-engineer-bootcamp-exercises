# AI Engineer Bootcamp: class exercises

The code we read, run and change together in class, one folder per session. This repository is separate from your Project 1 repository, and it has its own Codespace.

## First time

1. Click **Fork** at the top of this page, then **Create fork**.
2. On your fork, click the green **Code** button, open the **Codespaces** tab, and click **Create codespace on main**.
3. In the terminal at the bottom of the editor, type `python setup_check.py` and press Enter. Paste your own API key when it asks, and wait for "All set!" The class uses OpenRouter. If your key is from somewhere else, see "Using a different provider" below.

## Getting a new session's files

1. On your fork's page on GitHub, click **Sync fork**, then **Update branch**.
2. In your Codespace, click the Source Control icon on the left, then **Sync Changes**.

The new session's folder appears in the file list.

## Handing in your work

1. In your Codespace, click the Source Control icon on the left.
2. Type a short message, click **Commit**, then **Sync Changes**.
3. Post the link to your fork in Discord.

Before you commit, look at the list of changed files. Your key lives in `.env`, which Git ignores, so it should never appear there.

## Using a different provider

Your key, your provider's address and your model name are saved in the `.env` file at the top of this repository. From Session 4 on, every app reads them from there, so this is the only place to change them:

```
LLM_API_KEY=your-key
LLM_BASE_URL=https://openrouter.ai/api/v1
LLM_MODEL=google/gemma-4-26b-a4b-it:floor
```

To switch provider, type `python setup_check.py --switch` and answer the three questions. You can also edit the three lines in `.env` yourself, then type `python setup_check.py` to test them.

- All three change together. A key from one provider does not work at another provider's address, and model names are different at every provider.
- Your provider's documentation gives its base URL for the OpenAI-compatible API, and its model names.
- Git ignores `.env`, so syncing your fork never resets these lines.
- If an app stops with `KeyError: 'LLM_API_KEY'`, `'LLM_BASE_URL'` or `'LLM_MODEL'`, your `.env` is from before Session 4. Type `python setup_check.py` once and it adds the missing lines.

The Session 3 apps are older and always use OpenRouter. They read a key named `OPENROUTER_API_KEY` from `.env`, the address is written in `assistant.py` and `model.py`, and the model name is in each app's `settings.json`.

## Sessions

- `session-03`: reading code you didn't write. App A, App B and its prediction sheets, the path drills, and the syntax card.
- `session-04`: five broken apps to debug. Start with `session-04/README.md`.
