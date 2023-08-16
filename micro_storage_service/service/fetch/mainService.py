from micro_storage_service.service.fetch.dbService import FetchDbService

class MainFetchService:

    def __init__(self) -> None:
        self._fetchdb:FetchDbService=FetchDbService()
    #def checks(self):
#
    #    if (not File.objects.filter(uri=self.uri).exists()) and File.objects.get(uri=self.uri).user_id!=self.id:
    #        return False,{"info":"no records!"}
    #    
    #    else:
    #        return True,{}
        
    def fetch(self,uri:str)->dict:
        try:
            data=self._fetchdb.get(uri=uri)
            return {"data":data}
        except Exception  as e:
            print(e)
