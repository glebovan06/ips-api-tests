import allure
from src.models import PumpStatusResponse


@allure.feature("Pumps")
@allure.story("GET /status")
class TestPumpStatus:

    @allure.title("Успешное получение статуса помпы")
    def test_get_status_positive(self, api_client, valid_pump_id):
        response = api_client.get_status(valid_pump_id)
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: {response.text}"
        )
        data = PumpStatusResponse(**response.json())
        assert data.alerts_count >= 0, (
            f"Количество алертов не может быть отрицательным: {data.alerts_count}"
        )

    @allure.title("Негатив: пустой pump_id")
    def test_get_status_empty_pump_id(self, api_client):
        response = api_client.get_status("")
        assert response.status_code == 404, (
            f"Ожидали 404 для пустого ID, получили {response.status_code}: {response.text}"
        )