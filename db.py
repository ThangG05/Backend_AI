from sqlmodel import create_engine, Session
from config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"sslmode": "require"}
)

def get_session():
    with Session(engine) as session:
        yield session