"""Central configuration for the AI-Powered Blog Content Generator."""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
MODEL_DIR = os.path.join(BASE_DIR, "models")

BLOG_FILE = os.path.join(OUTPUT_DIR, "generated_blog.txt")
CONFIG_FILE = os.path.join(OUTPUT_DIR, "blog_config.json")

# Local LLM served by Ollama
OLLAMA_MODEL = "llama3.2:latest"

LINE = "=" * 70
DASH = "-" * 70
