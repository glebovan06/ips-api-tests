import requests
import allure
from datetime import datetime, timezone

BASE_URL = "https://ips.alexgallax-edu.ru/api/v1"


class PumpApiClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    @allure.step("GET /pumps/{pump_id}/status")
    def get_status(self, pump_id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/pumps/{pump_id}/status")

    @allure.step("GET /pumps/{pump_id}/alerts")
    def get_alerts(self, pump_id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/pumps/{pump_id}/alerts")

    @allure.step("DELETE /pumps/{pump_id}/alerts")
    def delete_alert(self, pump_id: str, alert_data: dict) -> requests.Response:
        return self.session.delete(
            f"{self.base_url}/pumps/{pump_id}/alerts",
            json=alert_data,
        )

    @allure.step("DELETE /pumps/{pump_id}/alerts/all")
    def delete_all_alerts(self, pump_id: str) -> requests.Response:
        return self.session.delete(f"{self.base_url}/pumps/{pump_id}/alerts/all")

    @allure.step("POST /pumps/{pump_id}/block/reset")
    def reset_block(self, pump_id: str) -> requests.Response:
        return self.session.post(f"{self.base_url}/pumps/{pump_id}/block/reset")

    @allure.step("POST /pumps/{pump_id}/telemetry")
    def send_glucose(self, pump_id: str, glucose_value: float) -> requests.Response:
        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        payload = {
            "glucose_value": glucose_value,
            "glucose_unit": "mmol/L",
            "timestamp": timestamp
        }
        return self.session.post(f"{self.base_url}/pumps/{pump_id}/telemetry", json=payload)