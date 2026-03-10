from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Hospital Management System"
    VERAION: str = "1.0.0"

    # security
    SECRET_KEY: str = "Thando2001"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "hospital_db"
    POSTGRES_PORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000", "hhtp://localhost:5173"]

    # First superuser
    FIRST_SUPERUSER_EMAIL: str = "admin@hospital.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin123"

    # Email
    SMTP_TLS: bool = True
    SMTP_PORT: int = 587
    SMTP_HOST: str = ""
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    EMAILS_FROM_EMAIL: str = ""
    EMAILS_FROM_NAME: str = PROJECT_NAME

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
