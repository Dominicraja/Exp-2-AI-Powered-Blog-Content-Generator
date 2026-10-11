"""Part D - SEO keyword generator (Q6)."""

import utils

SYSTEM = ("You are an SEO specialist. Reply with 8 to 10 SEO keywords for the given "
          "blog, one keyword per line. No numbering, no explanation, nothing else.")

MAX_KEYWORDS = 10


def generate_keywords(blog, verbose=True):
    """Q6 - generate SEO-friendly keywords for the generated blog."""
    reply = utils.ask(SYSTEM, "Generate SEO keywords for this blog:\n\n" + blog[:1500],
                      temperature=0.5)
    keywords = utils.numbered(reply, MAX_KEYWORDS)

    if verbose:
        print("SEO Keywords")
        print()
        for i, kw in enumerate(keywords, 1):
            print("{}. {}".format(i, kw))
        print()
        print("Keywords generated : {}".format(len(keywords)))
    return keywords


if __name__ == "__main__":
    utils.banner("SEO KEYWORD GENERATOR")
    b = utils.require_blog()
    if b:
        generate_keywords(b)
