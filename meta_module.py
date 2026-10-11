"""Part F - SEO meta description generator (Q8) - guaranteed within 160 characters."""

import utils

LIMIT = 160

SYSTEM = ("You write SEO meta descriptions. Reply with ONE sentence of at most {} "
          "characters. No quotes, no labels, no explanation.".format(LIMIT))


def _clean(text):
    return text.strip().strip('"').replace("\n", " ").strip()


def generate_meta(blog, verbose=True):
    """Q8 - generate an SEO meta description and enforce the 160 character limit."""
    meta = _clean(utils.ask(SYSTEM, "Write an SEO meta description for this blog:\n\n"
                            + blog[:1500], temperature=0.5))

    # If the model exceeds the limit, ask it for a shorter version before trimming.
    attempts = 0
    while len(meta) > LIMIT and attempts < 2:
        attempts += 1
        if verbose:
            print("Response was {} characters - requesting a shorter version ...".format(
                len(meta)))
        meta = _clean(utils.ask(
            SYSTEM,
            "Shorten this meta description to at most {} characters:\n\n{}".format(
                LIMIT, meta), temperature=0.3))

    # Final guarantee: trim on a word boundary if the model still overshoots.
    if len(meta) > LIMIT:
        meta = meta[:LIMIT - 3].rsplit(" ", 1)[0] + "..."

    if verbose:
        print("Meta Description")
        print()
        print(meta)
        print()
        print("Character count : {} / {}".format(len(meta), LIMIT))
        print("Within limit    : {}".format("Yes" if len(meta) <= LIMIT else "No"))
    return meta


if __name__ == "__main__":
    utils.banner("META DESCRIPTION GENERATOR")
    b = utils.require_blog()
    if b:
        generate_meta(b)
