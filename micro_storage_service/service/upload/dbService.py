from micro_storage_service.DTO.upload.dbDto import DbDTO
from rest_framework import status
from micro_storage_service.models import File

class UploadDbService:
    def save(self, dbdto: DbDTO):
        try:
                File.objects.create(
                    uri=dbdto.uri,
                    music_filename=dbdto.mainDto.music_filename,
                    music_cover_filename=dbdto.mainDto.music_cover_filename,
                    user_id=dbdto.user_id,
                    artist_name=dbdto.mainDto.artist_name,
                    desc=dbdto.mainDto.desc,
                    music_file_uri=dbdto.music_file_uri,
                    music_cover_uri=dbdto.music_cover_uri
                )
                return dbdto.uri,status.HTTP_201_CREATED
        except Exception as e:
            raise Exception(str(e))
