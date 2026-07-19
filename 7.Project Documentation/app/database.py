from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# We use a local SQLite database named edugenie.db in the project root
DATABASE_URL = "sqlite:///./edugenie.db"

# Create engine. Connect_args={"check_same_thread": False} is required only for SQLite
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependency provider to yield a database session and close it after request completion."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_session():
    db = SessionLocal()
    try:
        return db
    except Exception:
        db.close()
        raise
