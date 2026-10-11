#!/bin/bash
cd "$(dirname "$0")"
export PATH="/opt/homebrew/bin:/usr/local/bin:/Applications/Ollama.app/Contents/Resources:$PATH"
export PYTHONUNBUFFERED=1
source "$HOME/.ecomgpt-venv/bin/activate"
mkdir -p screenshots outputs models
printf "\e[8;46;100t"
sleep 1

# --- make sure Ollama is running and llama3.2 is present (not recorded) ---
clear
echo "Checking environment ..."
ollama --version
curl -s -m 5 http://localhost:11434/api/version >/dev/null || {
  echo "Starting Ollama ..."; nohup ollama serve >/dev/null 2>&1 & sleep 8; }
curl -s -m 5 http://localhost:11434/api/version >/dev/null && echo "Ollama is running." || {
  echo "ERROR: Ollama is not reachable. Aborting."; exit 1; }
ollama list | grep -q "llama3.2" && echo "llama3.2 is installed." || {
  echo "ERROR: llama3.2 not installed. Run: ollama pull llama3.2"; exit 1; }
echo "Warming the model ..."
python -c "import utils; utils.check_ollama(); utils.ask('You reply briefly.','hi')" || exit 1
echo "Ready. Starting the demos."
sleep 2

exec > >(tee demos.log) 2>&1
shot () { sleep 2; screencapture -x -o "screenshots/$1"; }

clear
printf '9\n' | python main.py
shot 01_home.png

clear
printf '1\nArtificial Intelligence in Education\nProfessional\nFormal\n500\n9\n' | python main.py
shot 02_user_input.png

clear
python blog_module.py
shot 03_blog_generation.png

clear
python title_module.py
shot 04_blog_titles.png

clear
python summary_module.py
shot 05_summary.png

clear
python keyword_module.py
shot 06_seo_keywords.png

clear
python meta_module.py
shot 07_meta_description.png

clear
printf '7\n9\n' | python main.py
shot 08_blog_saved.png

clear
python intent_module.py
shot 09_intent_detection.png

clear
echo "=== verification ==="
ls -l screenshots/
echo
echo "generated_blog.txt:"
wc -w outputs/generated_blog.txt
head -3 outputs/generated_blog.txt
echo
echo "DEMOS2_FINISHED_OK"
