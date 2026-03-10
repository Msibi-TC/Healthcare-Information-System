from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Hospitals(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    license_number = Column(String, unique=True)
    established_date = Column(Date)
    total_beds = Column(Integer, default=0)
    available_beds = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # relationships
    doctors = relationship("Doctor", back_populates="hospital")
    appointments = relationship("Appointment", back_populates="hospital")
    surgeries = relationship("Surgery", back_populates="hospital")
    departments = relationship("Department", back_populates="hospital")
