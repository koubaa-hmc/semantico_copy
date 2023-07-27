#!/bin/sh

set -e

. /backend/.venv/bin/activate

exec uvicorn semantico_backend.controller.baseController:app --host 0.0.0.0 --port 8000