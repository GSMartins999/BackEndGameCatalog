from ..repositories import IVinylRecordRepository


class DeleteVinylRecord:
    def __init__(self, vinyl_record_repository: IVinylRecordRepository):
        self.vinyl_record_repository = vinyl_record_repository

    async def execute(self, id: str) -> None:
        record = await self.vinyl_record_repository.find_by_id(id)

        if not record:
            raise ValueError("Vinyl record not found")

        await self.vinyl_record_repository.delete(id)
