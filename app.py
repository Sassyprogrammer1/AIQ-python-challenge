# controller.py
from fastapi import APIRouter, Query, HTTPException
from image_service import ImageService

router = APIRouter()
image_service = ImageService()

@router.get("/get-image-frames")
def get_image_frames(depth_min: float = Query(...), depth_max: float = Query(...)):
    try:
        frames = image_service.get_image_frames(depth_min, depth_max)
        return frames
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
