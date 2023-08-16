from django.http import JsonResponse
from datetime import datetime
from micro_storage_service.models import File
from rest_framework.response import Response

class FetchValidationMiddleWare:

    def validates(self,request:object):
        try:
            arr=request.path.split("/")
            uri=arr[len(arr)-1].split('=')[1]
            if File.objects.filter(uri=uri).exists():
                return True
            else:
                raise Exception("no data found")   
        except Exception as e:
           raise Exception(str(e))