import allure
from src.models import PumpStatusResponse


@allure.feature("Pumps")
@allure.story("GET /status")
class TestPumpStatus:

    @allure.title("Успешное получение статуса помпы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_status_positive(self, api_client, valid_pump_id):
        response = api_client.get_status(valid_pump_id)
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: {response.text}"
        )
        data = PumpStatusResponse(**response.json())
        assert data.alerts_count >= 0, (
            f"Количество алертов не может быть отрицательным: {data.alerts_count}"
        )

    @allure.title("Симулятор создаёт помпу для любого pump_id")
    def test_get_status_any_pump_id_returns_200(self, api_client, invalid_pump_id):
        response = api_client.get_status(invalid_pump_id)
        assert response.status_code == 200, (
            f"Симулятор должен создавать помпу для любого ID, "
            f"получили {response.status_code}: {response.text}"
        )

    @allure.title("Негатив: пустой pump_id")
    def test_get_status_empty_pump_id(self, api_client):
        response = api_client.get_status("")
        assert response.status_code in (404, 422), (
            f"Ожидали 404 или 422 для пустого pump_id, "
            f"получили {response.status_code}: {response.text}"
        )