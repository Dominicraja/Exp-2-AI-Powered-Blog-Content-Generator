"""Part C - Blog title generator (Q5) - always exactly five titles."""

import utils

SYSTEM = ("You suggest blog titles. Reply with exactly five titles, one per line, "
          "numbered 1 to 5. No introduction, no explanation, nothing else.")

WANTED = 5


def generate_titles(blog, verbose=True):
    """Q5 - generate exactly five attractive blog titles using Ollama."""
    reply = utils.ask(SYSTEM, "Suggest five attractive titles for this blog:\n\n"
                              + blog[:1500], temperature=0.8)
    titles = utils.numbered(reply, WANTED)

    # Ask again for any missing title so exactly five are always shown.
    attempts = 0
    while len(titles) < WANTED and attempts < 2:
        attempts += 1
        extra = utils.ask(SYSTEM, "Suggest {} more titles for this blog:\n\n{}".format(
            WANTED - len(titles), blog[:1500]), temperature=0.9)
        for t in utils.numbered(extra):
            if t not in titles:
                titles.append(t)
            if len(titles) == WANTED:
                break

    titles = titles[:WANTED]

    if verbose:
        print("Suggested Titles")
        print()
        for i, title in enumerate(titles, 1):
            print("{}. {}".format(i, title))
        print()
        print("Titles generated : {}".format(len(titles)))
    return titles


if __name__ == "__main__":
    utils.banner("BLOG TITLE GENERATOR")
    b = utils.require_blog()
    if b:
        generate_titles(b)
