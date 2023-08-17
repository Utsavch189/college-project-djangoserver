from abc import ABC,abstractmethod
from micro_storage_service.DTO.upload.dbDto import DbDTO


class IDbService(ABC):

    @abstractmethod
    def save(self,dbdto: DbDTO)->str:
        pass

    @abstractmethod
    def get(self,uri:str)->dict:
        pass