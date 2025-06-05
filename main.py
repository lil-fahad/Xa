
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router as api_router
from generator import router as generator_router
from planner import router as planner_router
from evaluator import router as evaluator_router
from ar_module import streamlit_combined_viewer

app = FastAPI(title="Furniture Broker AI ∞X")

# إعدادات CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# نقطة اختبار أساسية
@app.get("/")
def home():
    return {"message": "Furniture Broker AI ∞X is live."}

# نقاط النهاية الخاصة بالمشروع
app.include_router(api_router, prefix="/api", tags=["API"])
app.include_router(generator_router, prefix="/generate", tags=["Generator"])
app.include_router(planner_router, prefix="/plan", tags=["Planner"])
app.include_router(evaluator_router, prefix="/evaluate", tags=["Evaluator"])

# إضافة نقطة لتكامل AR إذا لزم الأمر (تجريبي)
@app.get("/ar/visualize")
def visualize_ar():
    return {"message": "AR visualization endpoint (to be implemented)"}
