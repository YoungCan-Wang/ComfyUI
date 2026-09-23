#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "======================================================="
echo "   Starting ComfyUI (Apple Silicon M5 / MPS)"
echo "   Model: Qwen-Image-2.1-GGUF"
echo "   URL: http://127.0.0.1:8188"
echo "======================================================="

# Run ComfyUI with standard MPS acceleration
exec "$DIR/.venv/bin/python" main.py --listen 127.0.0.1 --port 8188 "$@"
