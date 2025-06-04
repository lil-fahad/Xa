from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI(title="Furniture Broker AI vX")

app.include_router(api_router, prefix="/api", tags=["AI System"])

@app.get("/")
def welcome():
    return {"msg": "Furniture Broker AI vX system is live!"}
