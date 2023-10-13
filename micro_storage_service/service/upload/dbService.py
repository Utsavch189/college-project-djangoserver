from micro_storage_service.DTO.upload.dbDto import DbDTO
from micro_storage_service.serializer.uploadSerializer import SaveFileSerializer
from rest_framework import status


class UploadDbService:
    def save(self, dbdto: DbDTO):
        try:
            uploaddto=dbdto.uploaddto.__dict__
            del dbdto.__dict__['uploaddto']
            del dbdto.__dict__['request']
            del uploaddto['music_fileobj']
            del uploaddto['music_cover_fileobj']
            dto=dbdto.__dict__
            data=uploaddto|dto
            serializer=SaveFileSerializer(data=data)
            if(serializer.is_valid()):
                serializer.save()
                return serializer.data['uri'],status.HTTP_201_CREATED
        except Exception as e:
            raise Exception(str(e))
