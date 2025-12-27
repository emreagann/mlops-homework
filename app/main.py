from fastapi import FastAPI
from pydantic import BaseModel
from app.features import hash_feature

app = FastAPI()

class PredictionRequest(BaseModel):
    feature: str

@app.post("/predict")
def predict(request: PredictionRequest):
    result = hash_feature(request.feature)
    return {"result": result}
