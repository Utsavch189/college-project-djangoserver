from micro_storage_service.models import File
from micro_storage_service.serializer.fetchSerializer import GetFileSerializer

class FetchDbService:

    def get(self,uri:str):
        try:
            file=File.objects.get(uri=uri)
            serializer=GetFileSerializer(file)
            
            return serializer.data
        except Exception as e:
            raise Exception(str(e))