"""Part B - AI blog generation (Q3, Q4)."""

import utils

SYSTEM = ("You are a professional blog writer. Write an original blog with an "
          "Introduction, Main Content with subheadings, and a Conclusion. "
          "Return only the blog itself, with no commentary about the request.")


def build_prompt(details):
    """Q3 - construct the Ollama prompt from the collected user inputs."""
    return ("Write a blog of about {words} words on the topic \"{topic}\".\n"
            "Writing style : {style}\n"
            "Tone          : {tone}\n"
            "Include a title, an Introduction, Main Content and a Conclusion."
            ).format(**details)


def generate_blog(details, verbose=True):
    """Q4 - generate the complete blog using Llama 3.2 through Ollama."""
    prompt = build_prompt(details)

    if verbose:
        print("Prompt sent to Ollama")
        print(utils.DASH)
        print(prompt)
        print(utils.DASH)
        print("\nGenerating Blog using {} ...\n".format(utils.OLLAMA_MODEL))

    blog = utils.ask(SYSTEM, prompt)
    utils.save_blog(blog)

    if verbose:
        print(utils.DASH)
        print(blog)
        print(utils.DASH)
        print("Word count : {} words".format(len(blog.split())))
    return blog


if __name__ == "__main__":
    utils.banner("AI BLOG GENERATION")
    d = utils.load_details()
    if not d:
        print("No blog details found. Run input_module.py first.")
    else:
        generate_blog(d)
