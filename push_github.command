#!/bin/bash
cd "$(dirname "$0")"
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
exec > >(tee push.log) 2>&1
set -e
REPO="https://github.com/ViknanS/Exp-2-AI-Powered-Blog-Content-Generator.git"
git init -b main 2>/dev/null || git init
git add -A
git status --short
git -c user.name="ViknanS" -c user.email="viknan0082@gmail.com" \
    commit -m "Experiment 2: AI-Powered Blog Content Generator using Ollama" || echo "nothing new to commit"
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO"
if git push -u origin main; then echo "PUSH_OK"; else
  echo "Push rejected. Run: git pull --rebase origin main   then re-run this script."; fi
