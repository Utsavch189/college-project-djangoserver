from micro_storage_service.service.db.mainDbService import DbService

class MainFetchService:

    def __init__(self) -> None:
        self._db:DbService=DbService()
        
    def fetch(self,uri:str)->dict:
        try:
            data,status_code=self._db.get(uri=uri)
            return {"data":data},status_code
        except Exception  as e:
            print(e)
