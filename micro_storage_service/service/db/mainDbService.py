from micro_storage_service.DTO.upload.dbDto import DbDTO
from micro_storage_service.service_interface.dbService import IDbService
from micro_storage_service.service.upload.dbService import UploadDbService
from micro_storage_service.service.fetch.dbService import FetchDbService

class DbService(IDbService):

    def __init__(self) -> None:
        self._uploaddb:UploadDbService=UploadDbService()
        self._fetchdb:FetchDbService=FetchDbService()
    
    def save(self, dbdto: DbDTO) -> str:
        return self._uploaddb.save(dbdto=dbdto)
    
    def get(self, uri: str) -> dict:
        return self._fetchdb.get(uri=uri)


    