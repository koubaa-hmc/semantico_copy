from fastapi import APIRouter
from fastapi import HTTPException

from semantico_backend.collector.pdf_analyzer.segmenter import Segmentation

routerSegmentToJson = APIRouter(
    prefix="/segment",
)

segmentation = Segmentation()


@routerSegmentToJson.get("/paragraphs/count/{pdfDesc}")
async def count_paragraphs(pdf_desc: str):
    if pdf_desc == "test":
        raise HTTPException(status_code=404, detail=f"'{pdf_desc}' document not found")
    else:
        return segmentation.count_paragraphs(pdf_desc)
