from dataclasses import dataclass,field
from datetime import datetime
from micro_storage_service.DTO.upload.main import UploadAPI
from micro_storage_service.models import File

@dataclass
class DbDTO:
    uri:str=field(default_factory=str)
    mainDto:UploadAPI=field(default_factory=object)
    user_id:str=field(default_factory=str)
    music_file_uri:str=field(default_factory=str)
    music_cover_uri:str=field(default_factory=str)

    def __post_init__(self):
        try:
            self.uri=str(int(datetime.timestamp(datetime.now())))+str(self.user_id)
            if File.objects.filter(music_file_uri=self.music_file_uri,music_cover_uri=self.music_cover_uri,uri=self.uri).exists():
                raise Exception("already files are exist with same name for this id!")
        except Exception as e:
            raise Exception(str(e))