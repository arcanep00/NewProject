from sqlalchemy import Integer, JSON, Float, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class JobSummary(Base):
    __tablename__ = "job_summaries"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False, unique=True)
    total_spend_inr = Column(Float, default=0)
    total_spend_usd = Column(Float, default=0)
    top_merchants = Column(JSON, nullable=True)
    anomaly_count = Column(Integer, default=0)
    narrative = Column(String(2000), nullable=True)
    risk_level = Column(String(20), nullable=True)
    job = relationship(
        "Job",
        back_populates="summary"
    )
