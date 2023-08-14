from micro_storage_service.dto.upload.dbDto import DbDTO
from micro_storage_service.repository.upload.main import SaveRepo
from micro_storage_service.serializer.uploadSerializer import SaveFileSerializer

class SaveToDBRepo(SaveRepo):
    
    def save(self, dbdto: DbDTO):
        try:
            uploaddto=dbdto.uploaddto.__dict__
            del dbdto.__dict__['uploaddto']
            del dbdto.__dict__['request']
            dto=dbdto.__dict__
            data=uploaddto|dto
            serializer=SaveFileSerializer(data=data)
            if(serializer.is_valid()):
                serializer.save()
                return serializer.data
        except Exception as e:
            raise Exception(str(e))
        