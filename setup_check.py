"""Setup check: confirms your dev container can talk to the model.

    python setup_check.py             first time, or to check again
    python setup_check.py --new-key   replace your saved key
    python setup_check.py --switch    change to a different provider

Three values are saved in the .env file at the top of the repository.
That file is the one place to change them:

    LLM_API_KEY     your key
    LLM_BASE_URL    the address requests are sent to
    LLM_MODEL       the model to ask for
"""

import sys
from getpass import getpass
from urllib.parse import urlparse

import openai
from dotenv import dotenv_values, set_key

ENV_FILE = ".env"

# Used only when .env has no value yet. To change provider, change .env
# (or run this file with --switch). Do not edit these two lines.
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "google/gemma-4-26b-a4b-it:floor"


def stop(message):
    print(f"❌ {message}")
    sys.exit(1)


def save(name, value):
    set_key(ENV_FILE, name, value, quote_mode="never")


def save_key(key):
    save("LLM_API_KEY", key)
    # The Session 3 apps still read the key under its old name, and they
    # only talk to OpenRouter. Keep that copy in step with an OpenRouter key.
    if provider == "openrouter.ai":
        save("OPENROUTER_API_KEY", key)


saved = dotenv_values(ENV_FILE)
switching = "--switch" in sys.argv

# 1. Where requests go, and which model to ask for
base_url = saved.get("LLM_BASE_URL") or DEFAULT_BASE_URL
model = saved.get("LLM_MODEL") or DEFAULT_MODEL
if switching:
    print("Changing provider. Press Enter to keep the value shown in [brackets].")
    base_url = input(f"Base URL [{base_url}]: ").strip() or base_url
    model = input(f"Model [{model}]: ").strip() or model
if not base_url.startswith("http"):
    stop(f"A base URL starts with https:// and this one doesn't: {base_url}")
if switching or not saved.get("LLM_BASE_URL") or not saved.get("LLM_MODEL"):
    save("LLM_BASE_URL", base_url)
    save("LLM_MODEL", model)
    print("✅ Base URL and model saved to .env.")
provider = urlparse(base_url).hostname

# 2. Use the saved key, or ask for one and save it to .env
key = saved.get("LLM_API_KEY")
if not key and saved.get("OPENROUTER_API_KEY"):
    # Before Session 4, the key was saved under this older name.
    key = saved["OPENROUTER_API_KEY"]
    save("LLM_API_KEY", key)
    print("✅ Your saved key now has the name LLM_API_KEY in .env.")

if switching and key:
    print(f"Paste your key for {provider} and press Enter, or press Enter alone to keep the saved key.")
    print("(Nothing appears while you paste. That's normal.)")
    key = getpass("Key: ").strip() or key
    save_key(key)
elif not key or "--new-key" in sys.argv:
    print("Paste your API key and press Enter. (Nothing appears while you paste. That's normal.)")
    key = getpass("Key: ").strip()
    if not key:
        stop("No key entered. Run this again and paste the key before pressing Enter.")
    save_key(key)
    print("✅ Key saved to .env. Git ignores this file, so it never gets uploaded.")
print(f"✅ Using the key saved in .env (ends in ...{key[-4:]})")

# What to tell you for each kind of error the provider can send back
SAME_PROVIDER = "The key, the base URL and the model in .env must all come from the same provider."
SWITCH = "To change all three, run: python setup_check.py --switch"
FIXES = {
    401: f"{provider} didn't accept the key. Copy it again and run: python setup_check.py --new-key\n   Is the key from a different provider? {SWITCH}",
    402: f"The key is out of credit or hit its spending limit. Class key: tell your instructor. Your own key: add credit at {provider}.",
    403: f"This key isn't allowed to use {model}. Tell your instructor.",
    404: f"{provider} doesn't recognize the model {model}, or the base URL is wrong.\n   Model names are different at every provider. {SWITCH}",
    429: "The model is busy right now. Wait a minute and run this again.",
}

# 3. Send the model one test message
print(f"Sending a test message to {model} at {provider} ...")
client = openai.OpenAI(base_url=base_url, api_key=key)
try:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Reply with exactly one word: ready"}],
        max_tokens=50,
    )
except openai.APIConnectionError:
    stop(f"Couldn't reach {provider}. Check your internet connection and the LLM_BASE_URL line in .env, then run this again.")
except openai.APIStatusError as error:
    stop(FIXES.get(error.status_code, f"{provider} returned an error. {SAME_PROVIDER}\n   {SWITCH}\n   If they already match, tell your instructor: {error}"))

reply = response.choices[0].message.content
if not reply:
    stop("The model sent back an empty reply. Tell your instructor.")
print(f'✅ The model replied: "{reply.strip()}"')
print("🎉 All set! Your dev container can talk to the model.")
