import allure
import pytest
from src.models import ActionResponse


@allure.feature("Pumps")
@allure.story("Block reset")
class TestPumpBlockReset:

    @allure.title("Сброс блокировки: допустимый ответ 200 или 403")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_reset_block_positive(self, api_client, valid_pump_id):
        response = api_client.reset_block(valid_pump_id)
        assert response.status_code in (200, 403), (
            f"Ожидали 200 или 403 (в зависимости от состояния помпы), "
            f"получили {response.status_code}: {response.text}"
        )
        data = ActionResponse(**response.json())
        assert data.status, "Поле status не должно быть пустым"
        assert data.message is not None, "Поле message обязательно"

    @allure.title("Негатив: сброс блокировки при недопустимом уровне глюкозы")
    def test_reset_block_forbidden_by_glucose(self, api_client, valid_pump_id):
        response = api_client.reset_block(valid_pump_id)
        if response.status_code == 403:
            data = ActionResponse(**response.json())
            assert data.status == "FAILED", (
                f"При 403 статус должен быть FAILED, получено {data.status}"
            )
            assert "глюкоз" in data.message.lower(), (
                f"Ожидали сообщение про глюкозу, получили: {data.message}"
            )
        else:
            pytest.skip("Помпа не заблокирована — негативный сценарий недоступен")