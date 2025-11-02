import uuid
from datetime import datetime

from ..entities import Loan
from ..repositories import ILoanRepository, IUserRepository, IVinylRecordRepository


class BorrowVinylRecord:
    def __init__(
        self,
        loan_repository: ILoanRepository,
        user_repository: IUserRepository,
        vinyl_record_repository: IVinylRecordRepository,
    ):
        self.loan_repository = loan_repository
        self.user_repository = user_repository
        self.vinyl_record_repository = vinyl_record_repository

    async def execute(self, user_id: str, vinyl_record_id: str) -> Loan:
        user = await self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        vinyl_record = await self.vinyl_record_repository.find_by_id(vinyl_record_id)
        if not vinyl_record:
            raise ValueError("Vinyl record not found")

        current_loan = await self.loan_repository.find_current_loan_of_record(
            vinyl_record_id
        )
        if current_loan:
            raise ValueError("Vinyl record is already on loan")

        loan = Loan(
            id=str(uuid.uuid4()),
            user_id=user_id,
            vinyl_record_id=vinyl_record_id,
            loan_date=datetime.now(),
        )

        await self.loan_repository.save(loan)
        return loan
