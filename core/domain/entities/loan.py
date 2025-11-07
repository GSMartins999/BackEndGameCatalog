import dataclasses
from datetime import datetime
from typing import Optional

from .vinyl_record import VinylRecord


@dataclasses.dataclass(frozen=True)
class Loan:
    id: str
    user_id: str
    vinyl_record_id: str
    loan_date: datetime
    return_date: Optional[datetime] = None
    vinyl_record: Optional[VinylRecord] = None

    def return_loan(self) -> "Loan":
        if self.return_date:
            raise ValueError("Loan already returned")

        return dataclasses.replace(self, return_date=datetime.now())
