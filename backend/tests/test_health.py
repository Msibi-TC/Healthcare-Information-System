import os

from fastapi.testclient import TestClient

os.environ.setdefault(
    "SECRET_KEY",
    "test-only-secret-key-at-least-32-characters",
)

from app.main import app  # noqa: E402

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
