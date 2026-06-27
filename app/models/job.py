from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    status = Column(String, nullable=False)
    row_count_raw = Column(String, nullable=True)
    row_count_clean = Column(String, nullable=True)
    error_message = Column(String, nullable=True)
