from abc import ABC,abstractmethod
from micro_storage_service.dto.upload.dbDto import DbDTO

class SaveRepo(ABC):

    @abstractmethod
    def save(self,dbdto:DbDTO):
        pass