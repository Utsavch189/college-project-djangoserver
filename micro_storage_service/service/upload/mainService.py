from micro_storage_service.service.upload.writeFileService import WriteFileService
from micro_storage_service.service.db.mainDbService import DbService
from micro_storage_service.DTO.upload.writeobjDto import WriteFileDTO
from micro_storage_service.DTO.upload.dbDto import DbDTO

class MainUploadService:
    def __init__(self) -> None:
        self._writefile:WriteFileService=WriteFileService()
        self._db:DbService=DbService()
    
    def process(self,request:object,id:str)->dict:
        try:
            data,status_code=self._db.save(dbdto=DbDTO(request=request,user_id=id))
            success=self._writefile.write(dto=WriteFileDTO(request=request),id=id)
            if data and success:      
                return {"info":f"files are uploaded for {data}","uri":data},status_code
        except Exception  as e:
            raise Exception(str(e))