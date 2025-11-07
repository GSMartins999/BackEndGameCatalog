import pytest

from core.domain.use_cases.find_vinyl_record import FindVinylRecord
from core.domain.use_cases.register_vinyl_record import RegisterVinylRecord
from core.infra.mocks.mock_vinyl_record_repository import MockVinylRecordRepository


@pytest.mark.asyncio
async def test_should_find_a_vinyl_record_by_id():
    vinyl_record_repository = MockVinylRecordRepository()
    register_vinyl_record = RegisterVinylRecord(vinyl_record_repository)
    find_vinyl_record = FindVinylRecord(vinyl_record_repository)

    record = await register_vinyl_record.execute(
        band="Test Band",
        album="Test Album",
        year=2025,
        number_of_tracks=10,
        photo_url="http://example.com/photo.jpg",
        user_id="123",
    )
    found_record = await find_vinyl_record.execute(record.id)

    assert found_record is not None
    assert found_record.id == record.id


@pytest.mark.asyncio
async def test_should_return_none_if_vinyl_record_not_found():
    vinyl_record_repository = MockVinylRecordRepository()
    find_vinyl_record = FindVinylRecord(vinyl_record_repository)

    found_record = await find_vinyl_record.execute("non-existent-id")

    assert found_record is None
