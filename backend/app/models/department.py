from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    hospital_id = Column(Integer, ForeignKey("hospitals.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)

    # Retained for the planned Doctor model. A foreign key is unsafe until the
    # doctors table is implemented and registered in this metadata.
    head_doctor_id = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    hospital = relationship("Hospital", back_populates="departments")
