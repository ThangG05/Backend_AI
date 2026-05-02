from pydantic import BaseModel

class PredictResponse(BaseModel):
    gender: str
    confidence: float