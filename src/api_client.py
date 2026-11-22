import requests

BASE_URL = "https://ips.alexgallax-edu.ru/api/v1"


class PumpApiClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get_status(self, pump_id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/pumps/{pump_id}/status")

    def get_alerts(self, pump_id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/pumps/{pump_id}/alerts")

    def delete_alert(self, pump_id: str, alert_data: dict) -> requests.Response:
        return self.session.delete(
            f"{self.base_url}/pumps/{pump_id}/alerts",
            json=alert_data,
        )

    def delete_all_alerts(self, pump_id: str) -> requests.Response:
        return self.session.delete(f"{self.base_url}/pumps/{pump_id}/alerts/all")

    def reset_block(self, pump_id: str) -> requests.Response:
        return self.session.post(f"{self.base_url}/pumps/{pump_id}/block/reset")