from pydantic import BaseModel
from datetime import datetime


class PumpStatusResponse(BaseModel):
    is_on: bool | None = None
    current_glucose_value: float | None = None
    glucose_level: str | None = None
    alert_level: str | None = None
    bolus_status: str | None = None
    basal_speed_pc: int | None = None
    manual_action_required: bool | None = None
    message: str | None = None
    action_message: str | None = None
    alerts_count: int = 0


class Alert(BaseModel):
    level: str
    level_str: str
    message: str
    action_message: str
    timestamp: datetime


class ActionResponse(BaseModel):
    status: str
    message: str