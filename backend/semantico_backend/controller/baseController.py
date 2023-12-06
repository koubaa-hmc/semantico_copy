from fastapi import FastAPI
import logging

from semantico_backend.controller.segmentationController import routerSegmentToJson

app = FastAPI()
app.include_router(routerSegmentToJson)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.get('/')
async def root():
    return dict(message="Hello World")