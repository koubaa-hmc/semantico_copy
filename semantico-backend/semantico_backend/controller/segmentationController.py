from fastapi import APIRouter
from fastapi import HTTPException

routerSegmentToJson = APIRouter(
    prefix="/segment",
    responses={404: {"description": "Not found"}}
)

@routerSegmentToJson.get("/{pdfPath}")
async def read_pdfDocument(pdfPath: str):
    raise HTTPException(status_code=404, detail="pdf document not found")