from micro_storage_service.DTO.upload.main import UploadAPI
from django.http import JsonResponse
from datetime import datetime
import json

class UploadValidationMiddleWare:

    def validates(self,request:object):
        try:
            body_unicode = request.body.decode('utf-8')
            _data:dict = json.loads(body_unicode)
            res=UploadAPI(**_data)
            if res:
                return True
        except Exception as e:
           return JsonResponse({'message': str(e),"timestamp":datetime.timestamp(datetime.now())}, status=400)
