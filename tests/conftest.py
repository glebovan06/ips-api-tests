import uuid
import pytest
from src.api_client import PumpApiClient


@pytest.fixture(scope="session")
def api_client() -> PumpApiClient:
    return PumpApiClient()


@pytest.fixture
def valid_pump_id() -> str:
    """Генерируем уникальный ID для каждого теста, чтобы изолировать данные"""
    return f"pump-{uuid.uuid4().hex[:8]}"


@pytest.fixture
def invalid_pump_id() -> str:
    """Пустая строка — гарантированно невалидный ID"""
    return ""