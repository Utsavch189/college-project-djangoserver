from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from micro_storage_service.service.uploadService import UploadService
from micro_storage_service.service.fetchService import FetchService

from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

class UploadFileController(APIView):

    @log(logger=logger)
    def post(self,request,id):
        uploads=UploadService(request=request,id=id)
        message=uploads.upload()
        return Response(message,status=status.HTTP_200_OK)

class FetchFileController(APIView):

    @log(logger=logger)
    def get(self,request,uri,id):
        fetches=FetchService(request=request,uri=uri,id=id)
        message=fetches.fetch()
        return Response(message,status=status.HTTP_200_OK)
