from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LoanCreate(BaseModel):
    user_id: str
    vinyl_record_id: str


class LoanResponse(BaseModel):
    id: str
    user_id: str
    vinyl_record_id: str
    loan_date: datetime
    return_date: datetime | None

    model_config = ConfigDict(from_attributes=True)
