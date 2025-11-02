import pytest

from domain.use_cases.delete_vinyl_record import DeleteVinylRecord
from domain.use_cases.register_vinyl_record import RegisterVinylRecord
from tests.mocks.mock_vinyl_record_repository import MockVinylRecordRepository


@pytest.mark.asyncio
async def test_should_delete_a_vinyl_record():
    vinyl_record_repository = MockVinylRecordRepository()
    register_vinyl_record = RegisterVinylRecord(vinyl_record_repository)
    delete_vinyl_record = DeleteVinylRecord(vinyl_record_repository)

    record = await register_vinyl_record.execute(
        band="Test Band",
        album="Test Album",
        year=2025,
        number_of_tracks=10,
        photo_url="http://example.com/photo.jpg",
        user_id="123",
    )

    await delete_vinyl_record.execute(record.id)

    assert len(vinyl_record_repository.records) == 0


@pytest.mark.asyncio
async def test_should_not_delete_a_non_existent_vinyl_record():
    vinyl_record_repository = MockVinylRecordRepository()
    delete_vinyl_record = DeleteVinylRecord(vinyl_record_repository)

    with pytest.raises(ValueError, match="Vinyl record not found"):
        await delete_vinyl_record.execute("non-existent-id")
