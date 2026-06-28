from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    status = Column(String(20), nullable=False, default="pending")
    row_count_raw = Column(String, nullable=True)
    row_count_clean = Column(String, nullable=True)
    error_message = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    transactions = relationship(
        "Transaction",
        back_populates="job",
        cascade="all, delete-orphan"
    )
    summary = relationship(
        "JobSummary",
        back_populates="job",
        uselist=False,
        cascade="all, delete-orphan"
    )

