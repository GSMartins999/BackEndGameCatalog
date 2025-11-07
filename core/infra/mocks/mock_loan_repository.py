from typing import List, Optional

from core.domain.entities import Loan
from core.domain.repositories import ILoanRepository


class MockLoanRepository(ILoanRepository):
    def __init__(self):
        self.loans: List[Loan] = []

    async def save(self, loan: Loan) -> None:
        self.loans.append(loan)

    async def find_by_id(self, id: str) -> Optional[Loan]:
        return next((loan for loan in self.loans if loan.id == id), None)

    async def find_by_user_id(self, user_id: str) -> List[Loan]:
        return [loan for loan in self.loans if loan.user_id == user_id]

    async def find_current_loan_of_record(self, vinyl_record_id: str) -> Optional[Loan]:
        return next(
            (
                loan
                for loan in self.loans
                if loan.vinyl_record_id == vinyl_record_id and loan.return_date is None
            ),
            None,
        )

    async def update(self, loan: Loan) -> None:
        index = next(
            (i for i, item in enumerate(self.loans) if item.id == loan.id), None
        )
        if index is not None:
            self.loans[index] = loan
