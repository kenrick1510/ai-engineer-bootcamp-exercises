"""A pretend model API that runs on your own machine. No key and no cost.

Do not change this file. It stands in for a service you do not control.
"""

import time

LIMIT = 2  # requests allowed ...
WINDOW = 4  # ... in this many seconds

ANSWERS = {
    "What is a token?": "A piece of a word. Models read and write text in tokens.",
    "What is a context window?": "Everything the model can see at once: the prompt and the reply.",
    "What does temperature change?": "How often the model picks a less likely next token.",
    "What is a system prompt?": "The instructions that come first and set the assistant's behavior.",
    "What is a stack trace?": "The list of calls that were running when an error happened.",
}

_recent_requests = []


class PracticeAPIError(Exception):
    """What the pretend service sends back when a request fails."""

    def __init__(self, status_code, message):
        super().__init__(f"Error code: {status_code} - {message}")
        self.status_code = status_code
        self.message = message


def ask(question):
    """Answer one question, unless too many requests arrived too quickly."""
    now = time.monotonic()
    _recent_requests[:] = [t for t in _recent_requests if now - t < WINDOW]

    if len(_recent_requests) >= LIMIT:
        wait = WINDOW - (now - _recent_requests[0])
        raise PracticeAPIError(
            429,
            f"Rate limit exceeded: {LIMIT} requests per {WINDOW} seconds. Try again in {wait:.0f} seconds.",
        )

    _recent_requests.append(now)
    return ANSWERS.get(question, "I don't know that one.")
