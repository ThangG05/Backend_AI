from fastapi import APIRouter, UploadFile, File, Depends
from sqlmodel import Session, select # Thêm select để query chuẩn SQLModel
from db import get_session
from models import History
from schemas import PredictResponse

from audio_processing import extract_spectrogram
from ai_model import predict

from utils.file_handler import save_temp_file, delete_file

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
async def predict_api(
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    # 1. Lưu file tạm để xử lý
    path = save_temp_file(file)

    try:
        # 2. Trích xuất đặc trưng âm thanh (Spectrogram)
        feature = extract_spectrogram(path)

        # 3. Sử dụng AI để dự đoán giới tính
        gender, confidence = predict(feature)

        # 4. Lưu kết quả vào cơ sở dữ liệu
        record = History(
            file_name=file.filename,
            gender=gender,
            confidence=confidence
        )

        session.add(record)
        session.commit()
        session.refresh(record) # Làm mới object để đảm bảo dữ liệu đã lưu

        # 5. Xóa file tạm sau khi xong việc
        delete_file(path)

        # 6. Trả kết quả về cho Frontend
        return {
            "gender": gender,
            "confidence": confidence
        }
    except Exception as e:
        # Nếu có lỗi, vẫn nên xóa file tạm và báo lỗi
        delete_file(path)
        raise e

@router.get("/history")
def get_history(session: Session = Depends(get_session)):
    # Sử dụng cú pháp select của SQLModel sẽ chuẩn hơn
    statement = select(History)
    results = session.exec(statement).all()
    return results