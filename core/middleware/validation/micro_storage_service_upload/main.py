from micro_storage_service.DTO.upload.main import UploadAPI
import json
from pydantic import ValidationError

class UploadValidationMiddleWare:

    def validates(self,request:object):
        try:
            body_unicode = request.body.decode('utf-8')
            _data:dict = json.loads(body_unicode)
            res=UploadAPI(**_data)
            if res:
                return True
        except ValidationError as e:
           raise Exception(str(e)[:34])
