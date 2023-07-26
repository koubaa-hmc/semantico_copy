#!/bin/sh

set -e

. /sc_backend/.venv/bin/activate

exec uvicorn semantico_backend.Controller.baseController:app --host 0.0.0.0 --port 8000