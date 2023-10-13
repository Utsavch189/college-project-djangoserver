from micro_storage_service.service.upload.uploadFileService import UploadFileService
from micro_storage_service.service.db.mainDbService import DbService
from micro_storage_service.DTO.upload.writeobjDto import WriteFileDTO
from micro_storage_service.DTO.upload.dbDto import DbDTO

class MainUploadService:
    def __init__(self) -> None:
        self._uploadFile:UploadFileService=UploadFileService
        self._db:DbService=DbService()
    
    def process(self,request:object,id:str)->dict:
        try:
            result=self._uploadFile(
                dto=WriteFileDTO(request=request),id=id
            ).process()
            print()
            data,status_code=self._db.save(dbdto=DbDTO(request=request,user_id=id,music_cover_uri=result['music_cover_cdn']['secure_url'],music_file_uri=result['music_cdn']['secure_url']))
            return {"info":f"files are uploaded for {data}","uri":data},status_code
        except Exception  as e:
            raise Exception(str(e))