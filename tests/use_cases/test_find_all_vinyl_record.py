import pytest

from core.domain.use_cases.find_all_vinyl_record import FindAllVinylRecord
from core.domain.use_cases.register_vinyl_record import RegisterVinylRecord
from core.infra.mocks.mock_vinyl_record_repository import MockVinylRecordRepository


@pytest.mark.asyncio
async def test_should_find_all_vinyl_records():
    vinyl_record_repository = MockVinylRecordRepository()
    register_vinyl_record = RegisterVinylRecord(vinyl_record_repository)
    find_all_vinyl_record = FindAllVinylRecord(vinyl_record_repository)

    await register_vinyl_record.execute(
        band="Test Band 1",
        album="Test Album 1",
        year=2025,
        number_of_tracks=10,
        photo_url="http://example.com/photo1.jpg",
        user_id="123",
    )
    await register_vinyl_record.execute(
        band="Test Band 2",
        album="Test Album 2",
        year=2026,
        number_of_tracks=12,
        photo_url="http://example.com/photo2.jpg",
        user_id="456",
    )

    records = await find_all_vinyl_record.execute()

    assert len(records) == 2
