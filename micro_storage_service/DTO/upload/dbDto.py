from dataclasses import dataclass,field
from datetime import datetime
from micro_storage_service.DTO.upload.main import UploadAPI

@dataclass
class DbDTO:
    request:object=field(default_factory=object)
    uri:str=field(default_factory=str)
    uploaddto:UploadAPI=field(default_factory=object)
    user_id:str=field(default_factory=str)
    http_uri:str=field(default_factory=str)
    music_file_url:str=field(default_factory=str)
    music_cover_url:str=field(default_factory=str)

    def __post_init__(self):
        try:
            self.uploaddto=UploadAPI(**self.request.data)
            self.uri=str(int(datetime.timestamp(datetime.now())))+str(self.user_id)
            self.music_file_url=self.request.META['HTTP_HOST']+'/media/nft/'+f'{self.uploaddto.music_filename}'+f'{self.user_id}'
            self.music_cover_url=self.request.META['HTTP_HOST']+'/media/nft/'+f'{self.uploaddto.music_cover_filename}'+f'{self.user_id}'
        except Exception as e:
            raise Exception(str(e))