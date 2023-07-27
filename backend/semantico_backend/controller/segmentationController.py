from fastapi import APIRouter
from fastapi import HTTPException
from semantico_backend.collector.pdf_analyzer.segmenter import segmentToJson

routerSegmentToJson = APIRouter(
    prefix="/segment",
)

segmenter = segmentToJson()

@routerSegmentToJson.get("/paragraphs/count/{pdfPath}")
async def count_paragraphs(pdfPath: str):
    if pdfPath == "test":
        raise HTTPException(status_code=404, detail=f"'{pdfPath}' document not found")
    else:
        return segmenter.countParagraphs(pdfPath)
