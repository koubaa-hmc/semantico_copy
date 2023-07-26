from fastapi import FastAPI

from semantico_backend.controller.segmentationController import routerSegmentToJson

app = FastAPI()
app.include_router(routerSegmentToJson)

@app.get("/")
async def root():
    return {"message" : "Hello World"}