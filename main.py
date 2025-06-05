from fastapi import FastAPI
app = FastAPI(title="Furniture Broker AI ∞X")
@app.get("/")
def home():
    return {"message": "Furniture Broker AI ∞X is live."}
