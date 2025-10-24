#!/usr/bin/env bash
# Simple start script for development
# Usage: scripts/start.sh

set -euo pipefail

# Activate venv if present
if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
fi

# Run uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
