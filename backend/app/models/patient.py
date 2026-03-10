from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    blood_group = Column(String)
    height  = Column(Float)
    weight = Column(Float)
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String)
    allergies = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    #Relationships
    user = relationship("User", back_populates="patient")
    appointments = relationship("Appointment", back_populates="patient")
    consultations = relationship("Consulation", back_populates="patient")
    surgeries = relationship("Surgery", back_populates="patient")
    medical_records = relationship("MedicalRecord", back_populates="patient")
    