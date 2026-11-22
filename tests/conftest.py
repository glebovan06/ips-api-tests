import pytest
from src.api_client import PumpApiClient


@pytest.fixture(scope="session")
def api_client() -> PumpApiClient:
    return PumpApiClient()


@pytest.fixture(scope="session")
def valid_pump_id() -> str:
    return "pump-001"


@pytest.fixture(scope="session")
def invalid_pump_id() -> str:
    return "invalid-pump-999"