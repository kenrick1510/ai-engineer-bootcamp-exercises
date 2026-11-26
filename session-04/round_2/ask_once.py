"""Ask the model one question.

Run it from the top folder of the repository:
    python session-04/round_2/ask_once.py
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

# Read the key, the address and the model name from the nearest .env file.
# None of the three appears in this file.
load_dotenv()
client = OpenAI(
    base_url=os.environ["LLM_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
)

response = client.chat.completions.create(
    model=os.environ["LLM_MODEL"],
    messages=[{"role": "user", "content": "In one sentence: what is a terminal?"}],
    max_tokens=100,
)

print(response.choices[0].message.content)
