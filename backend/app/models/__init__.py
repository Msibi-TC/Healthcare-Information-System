"""Registration boundary for the currently implemented ORM models."""

from app.models.department import Department
from app.models.hospital import Hospital
from app.models.patient import Patient
from app.models.user import User, UserRole

__all__ = ["Department", "Hospital", "Patient", "User", "UserRole"]
