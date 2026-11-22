import allure
import pytest
from src.models import Alert


@allure.feature("Pumps")
@allure.story("Alerts")
class TestPumpAlerts:

    @allure.title("Получение списка алертов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_alerts_positive(self, api_client, valid_pump_id):
        response = api_client.get_alerts(valid_pump_id)
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: {response.text}"
        )
        alerts_data = response.json()
        assert isinstance(alerts_data, list), (
            f"Ожидали список, получили {type(alerts_data).__name__}"
        )
        for item in alerts_data:
            Alert(**item)

    @allure.title("Симулятор возвращает пустой список для несуществующего pump_id")
    def test_get_alerts_any_pump_id_returns_empty(self, api_client, invalid_pump_id):
        response = api_client.get_alerts(invalid_pump_id)
        assert response.status_code == 200, (
            f"Симулятор должен возвращать 200, получили {response.status_code}: {response.text}"
        )
        assert response.json() == [], (
            f"Ожидали пустой список для нового pump_id, получили {response.json()}"
        )

    @allure.title("Удаление всех алертов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_all_alerts(self, api_client, valid_pump_id):
        response = api_client.delete_all_alerts(valid_pump_id)
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: {response.text}"
        )
        assert isinstance(response.json(), list), (
            "Ответ при удалении всех алертов должен быть списком"
        )

    @allure.title("Удаление конкретного алерта (пропускается, если алертов нет)")
    def test_delete_specific_alert(self, api_client, valid_pump_id):
        get_response = api_client.get_alerts(valid_pump_id)
        alerts = get_response.json()
        if not alerts:
            pytest.skip("Нет алертов для удаления — пропускаем")
        alert_to_delete = alerts[0]
        response = api_client.delete_alert(valid_pump_id, alert_to_delete)
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: {response.text}"
        )