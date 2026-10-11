"""Part A - User input collection (Q1, Q2)."""

import utils

DEFAULT_STYLE = "Professional"
DEFAULT_TONE = "Formal"
DEFAULT_WORDS = 500


def collect_inputs():
    """Q1 - read the blog topic, writing style, tone and approximate word count."""
    print("Enter Blog Details")
    print(utils.DASH)

    topic = ""
    while not topic:
        topic = input("Enter Blog Topic : ").strip()
        if not topic:
            print("Blog topic cannot be empty. Please enter a topic.")

    style = input("Writing Style    : ").strip() or DEFAULT_STYLE
    tone = input("Tone             : ").strip() or DEFAULT_TONE

    words = None
    while words is None:
        raw = input("Word Count       : ").strip()
        if not raw:
            words = DEFAULT_WORDS
            break
        if raw.isdigit() and 50 <= int(raw) <= 2000:
            words = int(raw)
        else:
            print("Please enter a whole number between 50 and 2000.")

    details = {"topic": topic, "style": style, "tone": tone, "words": words}
    utils.save_details(details)
    return details


def display_inputs(details):
    """Q2 - display the collected information neatly."""
    print()
    print(utils.DASH)
    print("BLOG INPUT")
    print(utils.DASH)
    print("Blog Topic : {}".format(details["topic"]))
    print("Style      : {}".format(details["style"]))
    print("Tone       : {}".format(details["tone"]))
    print("Words      : {}".format(details["words"]))
    print(utils.DASH)


if __name__ == "__main__":
    utils.banner("USER INPUT COLLECTION")
    display_inputs(collect_inputs())
