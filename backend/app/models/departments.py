from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    hospital_id = Column(Integer, ForeignKey("hospitals.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    head_doctor_id = Column(Integer, ForeignKey("doctors.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    hospital = relationship("Hospital", back_populates="departments")
    head_doctor = relationship("Doctor")
