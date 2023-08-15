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

    def __post_init__(self):
        try:
            self.uploaddto=UploadAPI(**self.request.data)
            self.uri=str(int(datetime.timestamp(datetime.now())))+str(self.user_id)
            self.http_uri=self.request.META['HTTP_HOST']+'/api/v1/storage/'+f'getfile/uri={self.uri}&id={self.user_id}'
        except Exception as e:
            raise Exception(str(e))