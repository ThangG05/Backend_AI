from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from db import engine
from routes import router
from models import History

app = FastAPI()

# Cấu hình CORS để Frontend (cổng 3000) gọi được vào Backend (cổng 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    # Tạo các bảng trong cơ sở dữ liệu nếu chưa tồn tại
    SQLModel.metadata.create_all(engine)

# Nhúng các đường dẫn từ file routes.py
app.include_router(router)