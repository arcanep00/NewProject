from sqlalchemy import Integer, String, Float, Boolean, Date, Column, ForeignKey
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    txn_id = Column(String(100), nullable=True)
    date = Column(Date, nullable=False)
    merchant = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String(10), nullable=False)
    status = Column(String(20), nullable=False)
    category = Column(String(100), nullable=True)
    account_id = Column(String(100), nullable=False)
    is_anomaly = Column(Boolean, default=False, nullable=False)
    anomaly_reason = Column(String(255), nullable=True)
    llm_category = Column(String(100), nullable=True)
    llm_raw_response = Column(String(1000), nullable=True)
    llm_failed = Column(Boolean, default=False, nullable=False)
