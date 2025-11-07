from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.loan import Loan


class ILoanRepository(ABC):
    @abstractmethod
    async def save(self, loan: Loan) -> None:
        pass

    @abstractmethod
    async def find_by_id(self, id: str) -> Optional[Loan]:
        pass

    @abstractmethod
    async def find_by_user_id(self, user_id: str) -> List[Loan]:
        pass

    @abstractmethod
    async def find_current_loan_of_record(self, vinyl_record_id: str) -> Optional[Loan]:
        pass

    @abstractmethod
    async def update(self, loan: Loan) -> None:
        pass
