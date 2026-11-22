from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PumpStatusResponse(BaseModel):
    is_on: Optional[bool] = None
    current_glucose_value: Optional[float] = None
    glucose_level: Optional[str] = None
    alert_level: Optional[str] = None
    bolus_status: Optional[str] = None
    basal_speed_pc: Optional[int] = None
    manual_action_required: Optional[bool] = None
    message: Optional[str] = None
    action_message: Optional[str] = None
    alerts_count: int = 0


class Alert(BaseModel):
    level: str
    level_str: str = ""
    message: str = ""
    action_message: str = ""
    timestamp: datetime


class ActionResponse(BaseModel):
    status: str
    message: str