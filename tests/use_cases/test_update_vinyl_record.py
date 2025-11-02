import pytest

from domain.use_cases.register_vinyl_record import RegisterVinylRecord
from domain.use_cases.update_vinyl_record import UpdateVinylRecord
from tests.mocks.mock_vinyl_record_repository import MockVinylRecordRepository


@pytest.mark.asyncio
async def test_should_update_a_vinyl_record():
    vinyl_record_repository = MockVinylRecordRepository()
    register_vinyl_record = RegisterVinylRecord(vinyl_record_repository)
    update_vinyl_record = UpdateVinylRecord(vinyl_record_repository)

    record = await register_vinyl_record.execute(
        band="Test Band",
        album="Test Album",
        year=2025,
        number_of_tracks=10,
        photo_url="http://example.com/photo.jpg",
        user_id="123",
    )

    updated_record = await update_vinyl_record.execute(
        id=record.id, band="Updated Band", album="Updated Album"
    )

    assert updated_record.band.value == "Updated Band"
    assert updated_record.album.value == "Updated Album"


@pytest.mark.asyncio
async def test_should_not_update_a_non_existent_vinyl_record():
    vinyl_record_repository = MockVinylRecordRepository()
    update_vinyl_record = UpdateVinylRecord(vinyl_record_repository)

    with pytest.raises(ValueError, match="Vinyl record not found"):
        await update_vinyl_record.execute("non-existent-id", band="Updated Band")
