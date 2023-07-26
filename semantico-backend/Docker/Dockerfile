FROM python:3.10 AS base

# python:
ENV NOTHING=0

WORKDIR /sc_backend

### BUILD STAGE ###
FROM base AS builder

# pip:
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
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
COPY --from=builder /sc_backend/.venv ./.venv
COPY --from=builder /sc_backend/dist .
COPY Docker/docker-entrypoint.sh .

# install semantico_backend dependencies
RUN ./.venv/bin/pip install *.whl

EXPOSE 8000
ENTRYPOINT [ "./docker-entrypoint.sh" ]