import pytest

from domain.use_cases.register_vinyl_record import RegisterVinylRecord
from tests.mocks.mock_vinyl_record_repository import MockVinylRecordRepository


@pytest.mark.asyncio
async def test_should_register_a_new_vinyl_record():
    vinyl_record_repository = MockVinylRecordRepository()
    register_vinyl_record = RegisterVinylRecord(vinyl_record_repository)

    record = await register_vinyl_record.execute(
        band="Test Band",
        album="Test Album",
        year=2025,
        number_of_tracks=10,
        photo_url="http://example.com/photo.jpg",
        user_id="123",
    )

    assert record.band.value == "Test Band"
    assert record.album.value == "Test Album"
    assert len(vinyl_record_repository.records) == 1
