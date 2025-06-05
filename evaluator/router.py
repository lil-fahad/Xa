
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# نموذج البيانات للتقييم
class EvaluationRequest(BaseModel):
    layout_quality: int  # 1 to 10
    spacing_score: float  # 0.0 to 1.0
    aesthetics_score: float  # 0.0 to 1.0

class EvaluationResult(BaseModel):
    overall_score: float
    rating: str
    feedback: str

@router.post("/", response_model=EvaluationResult)
def evaluate_design(request: EvaluationRequest):
    if not (1 <= request.layout_quality <= 10):
        raise HTTPException(status_code=400, detail="Layout quality must be between 1 and 10.")
    if not (0 <= request.spacing_score <= 1) or not (0 <= request.aesthetics_score <= 1):
        raise HTTPException(status_code=400, detail="Scores must be between 0.0 and 1.0.")

    # تقييم بسيط على أساس متوسط النقاط
    weighted_score = (
        request.layout_quality * 0.5 +
        request.spacing_score * 25 +
        request.aesthetics_score * 25
    ) / 10

    if weighted_score >= 8:
        rating = "Excellent"
        feedback = "Outstanding balance of space, design, and aesthetics."
    elif weighted_score >= 5:
        rating = "Good"
        feedback = "Solid design but can be improved with better spacing or style."
    else:
        rating = "Needs Improvement"
        feedback = "Consider reworking layout and visual design elements."

    return EvaluationResult(
        overall_score=round(weighted_score, 2),
        rating=rating,
        feedback=feedback
    )
