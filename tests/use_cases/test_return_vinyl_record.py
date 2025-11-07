import pytest

from core.domain.use_cases.borrow_vinyl_record import BorrowVinylRecord
from core.domain.use_cases.register_user import RegisterUser
from core.domain.use_cases.register_vinyl_record import RegisterVinylRecord
from core.domain.use_cases.return_vinyl_record import ReturnVinylRecord
from core.infra.mocks.mock_loan_repository import MockLoanRepository
from core.infra.mocks.mock_user_repository import MockUserRepository
from core.infra.mocks.mock_vinyl_record_repository import MockVinylRecordRepository


@pytest.mark.asyncio
async def test_should_return_a_vinyl_record():
    user_repository = MockUserRepository()
    vinyl_record_repository = MockVinylRecordRepository()
    loan_repository = MockLoanRepository()

    register_user = RegisterUser(user_repository)
    register_vinyl_record = RegisterVinylRecord(vinyl_record_repository)
    borrow_vinyl_record = BorrowVinylRecord(
        loan_repository, user_repository, vinyl_record_repository
    )
    return_vinyl_record = ReturnVinylRecord(loan_repository)

    user = await register_user.execute("Test User", "test@example.com", "ValidPass1!")
    record = await register_vinyl_record.execute(
        band="Test Band",
        album="Test Album",
        year=2025,
        number_of_tracks=10,
        photo_url="http://example.com/photo.jpg",
        user_id=user.id,
    )
    loan = await borrow_vinyl_record.execute(user.id, record.id)

    returned_loan = await return_vinyl_record.execute(loan.id)

    assert returned_loan.return_date is not None


@pytest.mark.asyncio
async def test_should_not_return_a_non_existent_loan():
    loan_repository = MockLoanRepository()
    return_vinyl_record = ReturnVinylRecord(loan_repository)

    with pytest.raises(ValueError, match="Loan not found"):
        await return_vinyl_record.execute("non-existent-loan-id")
