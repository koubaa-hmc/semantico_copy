FROM python:3.10 AS base

# python:
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1

WORKDIR /backend

### BUILD STAGE ###
FROM base AS builder

# pip:
ENV PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_DEFAULT_TIMEOUT=100 \
  PIP_ROOT_USER_ACTION=ignore \
  # poetry:
  POETRY_VERSION=1.5.1

# install poetry
RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock README.md ./
COPY semantico_backend ./semantico_backend

# show poetry version
RUN poetry --version
# show app version
RUN poetry version
# create virtual environment in project directory
RUN poetry config virtualenvs.in-project true
#install dependencies
RUN poetry install --only=main --no-interaction --no-ansi --no-root
# build creates the wheel file of the inforportal_backend app
RUN poetry build

### PRODUCTION STAGE ##
FROM base AS final

# copy virtual environment and wheel file
COPY --from=builder /backend/.venv ./.venv
COPY --from=builder /backend/dist .

# copy entry point: should be executable
COPY --chmod=744 Docker/docker-entrypoint.sh .

# install semantico_backend dependencies
RUN ./.venv/bin/pip install *.whl

EXPOSE 8000
ENTRYPOINT [ "./docker-entrypoint.sh" ]