from dataclasses import dataclass,field
from datetime import datetime

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
    uploaddto:UploadDTO=field(default_factory=UploadDTO)

    def __post_init__(self):
        try:
            self.uploaddto.music_filename=self.request.data['music_filename']
            self.uploaddto.music_obj=self.request.data['music_fileobj']
            self.uploaddto.music_cover_filename=self.request.data['music_cover_filename']
            self.uploaddto.musicCover_obj=self.request.data['music_cover_fileobj']
        except Exception as e:
            raise Exception(str(e))

@dataclass
class DbDTO:
    request:object=field(default_factory=object)
    uri:str=field(default_factory=str)
    uploaddto:UploadDTO=field(default_factory=UploadDTO)
    user_id:str=field(default_factory=str)
    http_uri:str=field(default_factory=str)

    def __post_init__(self):
        try:
            self.uploaddto.music_filename=self.request.data['music_filename']
            self.uploaddto.music_obj=self.request.data['music_fileobj']
            self.uploaddto.music_cover_filename=self.request.data['music_cover_filename']
            self.uploaddto.musicCover_obj=self.request.data['music_cover_fileobj']
            self.uploaddto.artist_name=self.request.data['artist_name']
            self.uploaddto.desc=self.request.data['desc']
        
            self.uri=str(int(datetime.timestamp(datetime.now())))+str(self.user_id)
            self.http_uri=self.request.META['HTTP_HOST']+'/api/v1/storage/'+f'getfile/uri={self.uri}&id={self.user_id}'
        except Exception as e:
            raise Exception(str(e))