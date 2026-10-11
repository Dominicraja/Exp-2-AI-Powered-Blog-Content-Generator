"""Reusable helpers: configuration, Ollama access, formatting and file handling."""

import json
import os
import re

import ollama

# ----------------------------------------------------------------- config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
MODEL_DIR = os.path.join(BASE_DIR, "models")

BLOG_FILE = os.path.join(OUTPUT_DIR, "generated_blog.txt")
CONFIG_FILE = os.path.join(OUTPUT_DIR, "blog_config.json")

OLLAMA_MODEL = "llama3.2:latest"

LINE = "=" * 62
DASH = "-" * 62

_client = ollama.Client()


class OllamaError(Exception):
    """Raised when the local Ollama server cannot serve the request."""


# ----------------------------------------------------------------- Ollama
def check_ollama():
    """Verify the Ollama server is reachable and the model is installed."""
    try:
        models = _client.list()
    except Exception:
        raise OllamaError(
            "Cannot reach Ollama. Start it with:  ollama serve")

    names = [m.get("model") or m.get("name") for m in models.get("models", [])]
    if OLLAMA_MODEL not in names:
        raise OllamaError(
            "Model {} is not installed. Install it with:  ollama pull {}".format(
                OLLAMA_MODEL, OLLAMA_MODEL.split(":")[0]))
    return names


def ask(system_prompt, user_prompt, temperature=0.7):
    """Send a prompt to Llama 3.2 running locally through Ollama."""
    try:
        response = _client.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "system", "content": system_prompt},
                      {"role": "user", "content": user_prompt}],
            options={"temperature": temperature},
        )
    except Exception as exc:
        raise OllamaError("Ollama request failed: {}".format(exc))

    text = response["message"]["content"].strip()
    if not text:
        raise OllamaError("Ollama returned an empty response.")
    return text


# -------------------------------------------------------------- formatting
def banner(title):
    print(LINE)
    print(title)
    print(LINE)


def numbered(text, limit=None):
    """Turn a model reply into a clean numbered list."""
    items = []
    for raw in text.splitlines():
        item = re.sub(r"^\s*(?:\d+[\.\)]|[-*•])\s*", "", raw).strip()
        item = item.strip('"').strip()
        if item and not item.endswith(":"):
            items.append(item)
    return items[:limit] if limit else items


# ------------------------------------------------------------------- files
def save_blog(text):
    """Save the generated blog to outputs/generated_blog.txt."""
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(BLOG_FILE, "w") as f:
            f.write(text)
    except OSError as exc:
        raise OllamaError("Could not save the blog: {}".format(exc))
    return BLOG_FILE


def load_blog():
    if not os.path.exists(BLOG_FILE):
        return None
    with open(BLOG_FILE) as f:
        return f.read().strip()


def save_details(details):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(details, f, indent=2)


def load_details():
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE) as f:
        return json.load(f)


def require_blog():
    """Return the stored blog, or None with a message if none exists yet."""
    blog = load_blog()
    if blog is None:
        print("No blog found. Please generate a blog first.")
    return blog
