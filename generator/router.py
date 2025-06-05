
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random

router = APIRouter()

# نموذج البيانات لطلب التوليد
class GenerationRequest(BaseModel):
    style: str
    room_type: str
    budget: float

# نموذج البيانات للرد
class GeneratedFurniture(BaseModel):
    name: str
    price: float
    style: str
    room_type: str

# نقطة النهاية الفعلية لتوليد الأثاث
@router.post("/", response_model=GeneratedFurniture)
def generate_furniture(request: GenerationRequest):
    if request.budget < 50:
        raise HTTPException(status_code=400, detail="Budget too low to generate meaningful furniture.")

    sample_names = ["Elegant Sofa", "Modern Chair", "Classic Table", "Minimalist Shelf"]
    selected_name = random.choice(sample_names)

    return GeneratedFurniture(
        name=selected_name,
        price=min(request.budget, round(random.uniform(49.99, request.budget), 2)),
        style=request.style,
        room_type=request.room_type
    )
