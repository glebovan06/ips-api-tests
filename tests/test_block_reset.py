import allure
from src.models import ActionResponse


@allure.feature("Pumps")
@allure.story("Block reset")
class TestPumpBlockReset:

    @allure.title("Сброс блокировки: ответ содержит корректные поля")
    def test_reset_block_response_structure(self, api_client, valid_pump_id):
        response = api_client.reset_block(valid_pump_id)
        # Сервер может вернуть 200 или 403 в зависимости от состояния помпы
        assert response.status_code in (200, 403), (
            f"Неожиданный статус-код: {response.status_code}"
        )
        data = ActionResponse(**response.json())
        assert data.status in ("FAILED", "SUCCESS"), (
            f"Неожиданный статус в ответе: {data.status}"
        )

    @allure.title("Негатив: сброс блокировки при недопустимом уровне глюкозы")
    def test_reset_block_forbidden_by_glucose(self, api_client, valid_pump_id):
        response = api_client.reset_block(valid_pump_id)
        assert response.status_code == 403, (
            f"Ожидали 403 (блокировка из-за глюкозы), получили {response.status_code}: {response.text}"
        )
        data = ActionResponse(**response.json())
        assert data.status == "FAILED", (
            f"При 403 статус должен быть FAILED, получено {data.status}"
        )
        assert "глюкоз" in data.message.lower(), (
            f"Ожидали сообщение про глюкозу, получили: {data.message}"
        )