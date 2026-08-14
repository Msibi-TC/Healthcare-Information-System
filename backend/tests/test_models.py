from sqlalchemy import inspect
from sqlalchemy.orm import configure_mappers

from app.core.database import Base
from app.models import Department, Hospital, Patient, User, UserRole


def test_implemented_models_are_registered_and_configurable() -> None:
    configure_mappers()

    assert set(Base.metadata.tables) == {
        "departments",
        "hospitals",
        "patients",
        "users",
    }
    assert {Department, Hospital, Patient, User}


def test_all_foreign_keys_resolve_within_registered_metadata() -> None:
    foreign_keys = {
        foreign_key.target_fullname
        for table in Base.metadata.tables.values()
        for foreign_key in table.foreign_keys
    }

    assert foreign_keys == {"hospitals.id", "users.id"}
    for table in Base.metadata.tables.values():
        for foreign_key in table.foreign_keys:
            assert foreign_key.column.table in Base.metadata.tables.values()


def test_user_patient_relationship_is_one_to_one_and_bidirectional() -> None:
    user_relationship = inspect(User).relationships.patient
    patient_relationship = inspect(Patient).relationships.user

    assert user_relationship.uselist is False
    assert user_relationship.back_populates == "user"
    assert patient_relationship.back_populates == "patient"
    assert Patient.__table__.c.user_id.unique is True


def test_hospital_department_relationship_is_bidirectional() -> None:
    hospital_relationship = inspect(Hospital).relationships.departments
    department_relationship = inspect(Department).relationships.hospital

    assert hospital_relationship.uselist is True
    assert hospital_relationship.back_populates == "hospital"
    assert department_relationship.back_populates == "departments"


def test_user_role_enum_persists_documented_values() -> None:
    role_type = User.__table__.c.role.type

    assert role_type.enums == [role.value for role in UserRole]
