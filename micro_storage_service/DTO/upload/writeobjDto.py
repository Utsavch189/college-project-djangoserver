from dataclasses import dataclass,field
from micro_storage_service.dto.upload.main import UploadAPI

@dataclass
class UploadDTO:
    music_filename:str=field(default_factory=str)
    music_obj:str=field(default_factory=str)
    music_cover_filename:str=field(default_factory=str)
    musicCover_obj:str=field(default_factory=str)
    artist_name:str=field(default_factory=str)
    desc:str=field(default_factory=str)

@dataclass
class WriteFileDTO:
    request:object=field(default_factory=object)
    uploaddto:UploadAPI=field(default_factory=UploadAPI)

    def __post_init__(self):
        try:
            self.uploaddto.music_filename=self.request.data['music_filename']
            self.uploaddto.music_obj=self.request.data['music_fileobj']
            self.uploaddto.music_cover_filename=self.request.data['music_cover_filename']
            self.uploaddto.musicCover_obj=self.request.data['music_cover_fileobj']
        except Exception as e:
            raise Exception(str(e))

