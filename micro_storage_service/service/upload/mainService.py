from micro_storage_service.service.upload.writeFileService import WriteFileService
from micro_storage_service.service.upload.dbService import DbService
from micro_storage_service.DTO.upload.writeobjDto import WriteFileDTO
from micro_storage_service.DTO.upload.dbDto import DbDTO

class MainUploadService:
    def __init__(self) -> None:
        self._writefile:WriteFileService=WriteFileService()
        self._db:DbService=DbService()
    
    def process(self,request,id):
        try:
            success=self._writefile.write(dto=WriteFileDTO(request=request))
            if success: 
                data=self._db.save(dbdto=DbDTO(request=request,user_id=id))
                return {"info":"files are uploaded!","data":data}
        except Exception  as e:
            raise Exception(str(e))