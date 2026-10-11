"""Part H - Intelligent intent detection using Ollama (Q10)."""

import utils

INTENTS = ("BLOG_GENERATION", "SUMMARY", "KEYWORD_GENERATION", "META_DESCRIPTION")

SYSTEM = (
    "You are an intent classifier for a blog writing assistant.\n"
    "Reply with exactly one of these four labels and nothing else:\n"
    "BLOG_GENERATION, SUMMARY, KEYWORD_GENERATION, META_DESCRIPTION\n\n"
    "BLOG_GENERATION    - the user wants a blog or article written\n"
    "SUMMARY            - the user wants the blog summarised or shortened\n"
    "KEYWORD_GENERATION - the user wants SEO keywords or tags\n"
    "META_DESCRIPTION   - the user wants a meta description for search engines\n\n"
    "Examples:\n"
    "Write a blog on Cyber Security -> BLOG_GENERATION\n"
    "Summarize this blog -> SUMMARY\n"
    "Give SEO keywords -> KEYWORD_GENERATION\n"
    "Create a meta description -> META_DESCRIPTION"
)


def detect_intent(query):
    """Q10 - classify the request into exactly one of the four allowed labels.

    Handles replies such as "SUMMARY", "Intent: SUMMARY" or "The intent is summary".
    """
    raw = utils.ask(SYSTEM, "User: {}\nLabel:".format(query), temperature=0.0)
    text = raw.upper().replace("-", "_").replace(" ", "_")

    for intent in INTENTS:
        if intent in text:
            return intent
    if "KEYWORD" in text or "SEO" in text:
        return "KEYWORD_GENERATION"
    if "META" in text:
        return "META_DESCRIPTION"
    if "SUMMAR" in text:
        return "SUMMARY"
    if "BLOG" in text or "ARTICLE" in text:
        return "BLOG_GENERATION"
    return "BLOG_GENERATION"


if __name__ == "__main__":
    utils.banner("INTENT DETECTION  (model: {})".format(utils.OLLAMA_MODEL))
    samples = [
        "Write a blog on Cyber Security",
        "Summarize this blog",
        "Give SEO keywords",
        "Give a meta description",
    ]
    print("{:<38} {}".format("User Request", "Detected Intent"))
    print(utils.DASH)
    for q in samples:
        print("{:<38} {}".format(q, detect_intent(q)))
    print(utils.DASH)
