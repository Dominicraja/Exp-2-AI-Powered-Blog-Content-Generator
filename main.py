"""Part I - Complete Blog Content Generator (Q11).

Menu driven application that keeps running until the user exits. Free text
requests are routed automatically by the Ollama intent detector.
"""

import blog_module
import input_module
import intent_module
import keyword_module
import meta_module
import summary_module
import title_module
import utils

MENU = """  1. Enter Blog Details
  2. Generate Blog
  3. Generate Blog Titles
  4. Generate Summary
  5. Generate SEO Keywords
  6. Generate Meta Description
  7. Save Blog to File
  8. Detect Intent of a Request
  9. Exit"""


def home_screen():
    print(utils.LINE)
    print("        AI-POWERED BLOG CONTENT GENERATOR")
    print("        Powered by {} running locally on Ollama".format(utils.OLLAMA_MODEL))
    print(utils.LINE)
    print(MENU)
    print(utils.LINE)


def route(intent):
    """Run the module that matches a detected intent."""
    if intent == "BLOG_GENERATION":
        details = utils.load_details()
        if not details:
            print("Please enter the blog details first (option 1).")
            return
        blog_module.generate_blog(details)
        return

    blog = utils.require_blog()
    if not blog:
        return
    if intent == "SUMMARY":
        summary_module.generate_summary(blog)
    elif intent == "KEYWORD_GENERATION":
        keyword_module.generate_keywords(blog)
    elif intent == "META_DESCRIPTION":
        meta_module.generate_meta(blog)


def handle(choice):
    if choice == "1":
        input_module.display_inputs(input_module.collect_inputs())

    elif choice == "2":
        details = utils.load_details()
        if not details:
            print("Please enter the blog details first (option 1).")
        else:
            blog_module.generate_blog(details)

    elif choice in ("3", "4", "5", "6"):
        blog = utils.require_blog()
        if blog:
            {"3": title_module.generate_titles,
             "4": summary_module.generate_summary,
             "5": keyword_module.generate_keywords,
             "6": meta_module.generate_meta}[choice](blog)

    elif choice == "7":
        blog = utils.require_blog()
        if blog:
            path = utils.save_blog(blog)
            print("Blog saved successfully.")
            print("File       : {}".format(path))
            print("Words      : {}".format(len(blog.split())))
            print("Characters : {}".format(len(blog)))

    elif choice == "8":
        request = input("Enter your request : ").strip()
        if not request:
            print("Request cannot be empty.")
            return
        intent = intent_module.detect_intent(request)
        print()
        print("Detected Intent : {}".format(intent))
        print(utils.DASH)
        route(intent)

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")


def main():
    try:
        utils.check_ollama()
    except utils.OllamaError as exc:
        print(utils.LINE)
        print("  AI-POWERED BLOG CONTENT GENERATOR")
        print(utils.LINE)
        print(exc)
        return

    home_screen()

    while True:
        try:
            choice = input("Enter your choice : ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not choice:
            continue
        if choice == "9" or choice.lower() == "exit":
            print("\nThank you for using the Blog Content Generator. Goodbye!")
            break

        print()
        try:
            handle(choice)
        except utils.OllamaError as exc:
            print("Error: {}".format(exc))
        print(utils.LINE)


if __name__ == "__main__":
    main()
