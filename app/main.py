from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.features import hash_feature

app = FastAPI()

class PredictionRequest(BaseModel):
    feature: str

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        # Part 1 Integration: Using the feature logic
        bucket_index = hash_feature(request.feature)
        return {"bucket_index": bucket_index, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
