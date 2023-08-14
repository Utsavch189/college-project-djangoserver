from micro_storage_service.repository_Impl.uploadRepo.uploadRepository import SaveToDBRepo
from micro_storage_service.dto.upload.writeobjDto import WriteFileDTO
from micro_storage_service.dto.upload.dbDto import DbDTO
from micro_storage_service.utils.uploadUtil import WriteFile

class UploadService:

    def __init__(self) -> None:
        self._repo:SaveToDBRepo=SaveToDBRepo()
        self._writefile:WriteFile=WriteFile()
 
    def upload(self,request,id):
        try:
            print(WriteFileDTO(request=request))
            success=self._writefile.write(dto=WriteFileDTO(request=request))
            if success: 
                data=self._repo.saveDB(dbdto=DbDTO(request=request,user_id=id))
                return {"info":"files are uploaded!","data":data}
        except Exception  as e:
            raise Exception(str(e))


