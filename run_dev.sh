#!/usr/bin/env bash
set -e
uv run uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
