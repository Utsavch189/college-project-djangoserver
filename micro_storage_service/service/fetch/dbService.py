from micro_storage_service.models import File
from micro_storage_service.serializer.fetchSerializer import GetFileSerializer
from rest_framework import status


class FetchDbService:

    def get(self,uri:str):
        try:
            if File.objects.filter(uri=uri).exists():
                file=File.objects.get(uri=uri)
                serializer=GetFileSerializer(file)
                return serializer.data,status.HTTP_200_OK
            return "no data",status.HTTP_204_NO_CONTENT
        except Exception as e:
            raise Exception(str(e))