import enum

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Enum as SQLEnum,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class UserRole(str, enum.Enum):
    PATIENT = "patient"
    DOCTOR = "doctor"
    NURSE = "nurse"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"


def user_role_values(enum_class: type[UserRole]) -> list[str]:
    return [member.value for member in enum_class]


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(
        SQLEnum(
            UserRole,
            name="user_role",
            values_callable=user_role_values,
        ),
        nullable=False,
    )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    address = Column(String)
    national_id = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    patient = relationship("Patient", back_populates="user", uselist=False)
