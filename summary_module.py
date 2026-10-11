"""Part E - Blog summary generator (Q7) - approximately 100 words."""

import utils

SYSTEM = ("You summarise blogs. Write ONE paragraph of about 100 words using only "
          "information present in the blog. No headings, no bullet points.")

TARGET = 100
TOLERANCE = 40


def generate_summary(blog, verbose=True):
    """Q7 - generate a short summary of approximately 100 words."""
    summary = utils.ask(SYSTEM, "Summarise this blog in about 100 words:\n\n" + blog,
                        temperature=0.4)

    # One corrective attempt if the model drifts far from 100 words.
    if abs(len(summary.split()) - TARGET) > TOLERANCE:
        summary = utils.ask(
            SYSTEM,
            "Rewrite this summary so that it is close to 100 words:\n\n" + summary,
            temperature=0.3)

    if verbose:
        print("Summary")
        print()
        print(summary)
        print()
        print("Summary length : {} words (target ~{})".format(
            len(summary.split()), TARGET))
    return summary


if __name__ == "__main__":
    utils.banner("BLOG SUMMARY GENERATOR")
    b = utils.require_blog()
    if b:
        generate_summary(b)
