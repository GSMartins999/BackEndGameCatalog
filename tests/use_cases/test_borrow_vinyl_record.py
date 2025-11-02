import pytest

from domain.use_cases.borrow_vinyl_record import BorrowVinylRecord
from domain.use_cases.register_user import RegisterUser
from domain.use_cases.register_vinyl_record import RegisterVinylRecord
from tests.mocks.mock_loan_repository import MockLoanRepository
from tests.mocks.mock_user_repository import MockUserRepository
from tests.mocks.mock_vinyl_record_repository import MockVinylRecordRepository


@pytest.mark.asyncio
async def test_should_borrow_a_vinyl_record():
    user_repository = MockUserRepository()
    vinyl_record_repository = MockVinylRecordRepository()
    loan_repository = MockLoanRepository()

    register_user = RegisterUser(user_repository)
    register_vinyl_record = RegisterVinylRecord(vinyl_record_repository)
    borrow_vinyl_record = BorrowVinylRecord(
        loan_repository, user_repository, vinyl_record_repository
    )

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

    assert loan.user_id == user.id
    assert loan.vinyl_record_id == record.id
    assert len(loan_repository.loans) == 1


@pytest.mark.asyncio
async def test_should_not_borrow_if_user_not_found():
    user_repository = MockUserRepository()
    vinyl_record_repository = MockVinylRecordRepository()
    loan_repository = MockLoanRepository()
    borrow_vinyl_record = BorrowVinylRecord(
        loan_repository, user_repository, vinyl_record_repository
    )

    with pytest.raises(ValueError, match="User not found"):
        await borrow_vinyl_record.execute("non-existent-user-id", "record-id")


@pytest.mark.asyncio
async def test_should_not_borrow_if_vinyl_record_not_found():
    user_repository = MockUserRepository()
    vinyl_record_repository = MockVinylRecordRepository()
    loan_repository = MockLoanRepository()
    register_user = RegisterUser(user_repository)
    borrow_vinyl_record = BorrowVinylRecord(
        loan_repository, user_repository, vinyl_record_repository
    )

    user = await register_user.execute("Test User", "test@example.com", "ValidPass1!")

    with pytest.raises(ValueError, match="Vinyl record not found"):
        await borrow_vinyl_record.execute(user.id, "non-existent-record-id")


@pytest.mark.asyncio
async def test_should_not_borrow_if_vinyl_record_is_already_on_loan():
    user_repository = MockUserRepository()
    vinyl_record_repository = MockVinylRecordRepository()
    loan_repository = MockLoanRepository()

    register_user = RegisterUser(user_repository)
    register_vinyl_record = RegisterVinylRecord(vinyl_record_repository)
    borrow_vinyl_record = BorrowVinylRecord(
        loan_repository, user_repository, vinyl_record_repository
    )

    user = await register_user.execute("Test User", "test@example.com", "ValidPass1!")
    record = await register_vinyl_record.execute(
        band="Test Band",
        album="Test Album",
        year=2025,
        number_of_tracks=10,
        photo_url="http://example.com/photo.jpg",
        user_id=user.id,
    )

    await borrow_vinyl_record.execute(user.id, record.id)

    with pytest.raises(ValueError, match="Vinyl record is already on loan"):
        await borrow_vinyl_record.execute(user.id, record.id)
