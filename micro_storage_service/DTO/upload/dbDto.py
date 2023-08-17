from dataclasses import dataclass,field
from datetime import datetime
from micro_storage_service.DTO.upload.main import UploadAPI
from micro_storage_service.models import File

@dataclass
class DbDTO:
    request:object=field(default_factory=object)
    uri:str=field(default_factory=str)
    uploaddto:UploadAPI=field(default_factory=object)
    user_id:str=field(default_factory=str)
    music_file_uri:str=field(default_factory=str)
    music_cover_uri:str=field(default_factory=str)

    def __post_init__(self):
        try:
            self.uploaddto=UploadAPI(**self.request.data)
            self.uri=str(int(datetime.timestamp(datetime.now())))+str(self.user_id)
            self.music_file_uri=f'{self.user_id}'+f'{self.uploaddto.music_filename}'
            self.music_cover_uri=f'{self.user_id}'+f'{self.uploaddto.music_cover_filename}'
            if File.objects.filter(music_file_uri=self.music_file_uri,music_cover_uri=self.music_cover_uri).exists():
                raise Exception("already files are exist with same name for this id!")
        except Exception as e:
            raise Exception(str(e))