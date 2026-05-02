from sqlmodel import SQLModel, Field
from datetime import datetime

class History(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    file_name: str
    gender: str
    confidence: float
    created_at: datetime = Field(default_factory=datetime.utcnow)