# Semantico Backend

to build the docker of this project

```docker build -f Docker/Dockerfile -t sem_backend .```

to run the docker

```docker run sem_backend```

to run the app on local host

```poetry build```

```poetry run uvicorn semantico_backend.controller.baseController:app --reload```

The API is then usable under [http://localhost:8000/docs]
