import allure
import time
from src.models import Alert


@allure.feature("Pumps")
@allure.story("Alerts")
class TestPumpAlerts:

    @allure.title("Получение списка алертов")
    def test_get_alerts_positive(self, api_client, valid_pump_id):
        response = api_client.get_alerts(valid_pump_id)
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: {response.text}"
        )
        assert isinstance(response.json(), list), (
            f"Ожидали список, получили {type(response.json()).__name__}"
        )

    @allure.title("Негатив: получение алертов для пустого pump_id")
    def test_get_alerts_empty_pump_id_returns_404(self, api_client, invalid_pump_id):
        response = api_client.get_alerts(invalid_pump_id)
        assert response.status_code == 404, (
            f"Ожидали 404, получили {response.status_code}: {response.text}"
        )

    @allure.title("Удаление всех алертов")
    def test_delete_all_alerts(self, api_client, valid_pump_id):
        response = api_client.delete_all_alerts(valid_pump_id)
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: {response.text}"
        )
        assert isinstance(response.json(), list), (
            "Ответ при удалении всех алертов должен быть списком"
        )

    @allure.title("Удаление конкретного алерта")
    def test_delete_specific_alert(self, api_client, valid_pump_id):
        # 1. Создаем алерт, вызывая тревогу через низкий уровень глюкозы
        api_client.send_glucose(valid_pump_id, 2.0)
        time.sleep(1)

        # 2. Получаем список алертов
        get_response = api_client.get_alerts(valid_pump_id)
        alerts = get_response.json()

        assert len(alerts) > 0, (
            "Сервер не создал алерт после отправки низкой глюкозы"
        )

        # 3. Удаляем первый алерт
        alert_to_delete = alerts[0]
        delete_response = api_client.delete_alert(valid_pump_id, alert_to_delete)

        assert delete_response.status_code == 200, (
            f"Ожидали 200, получили {delete_response.status_code}: {delete_response.text}"
        )