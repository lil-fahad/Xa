
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import random

router = APIRouter()

# نموذج البيانات للغرفة والأثاث
class RoomLayoutRequest(BaseModel):
    width: float
    height: float
    furniture_items: List[str]

class FurniturePlacement(BaseModel):
    item: str
    x: float
    y: float

class RoomLayoutResponse(BaseModel):
    layout: List[FurniturePlacement]
    message: str

@router.post("/", response_model=RoomLayoutResponse)
def plan_room(request: RoomLayoutRequest):
    if request.width <= 0 or request.height <= 0:
        raise HTTPException(status_code=400, detail="Room dimensions must be positive.")

    layout = []
    for item in request.furniture_items:
        layout.append(FurniturePlacement(
            item=item,
            x=round(random.uniform(0, request.width), 2),
            y=round(random.uniform(0, request.height), 2)
        ))

    return RoomLayoutResponse(
        layout=layout,
        message="Furniture placed using simple randomized logic."
    )
