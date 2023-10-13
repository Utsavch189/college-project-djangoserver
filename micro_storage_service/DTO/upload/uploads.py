from dataclasses import dataclass,field
from micro_storage_service.DTO.upload.main import UploadAPI

@dataclass
class UploadFileDTO:
    request:object=field(default_factory=object)
    uploaddto:UploadAPI=field(default_factory=object)

    def __post_init__(self):
        try:
            self.uploaddto=UploadAPI(**self.request.data)
        except Exception as e:
            raise Exception(str(e))

