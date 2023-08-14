from typing import Any
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from micro_storage_service.service.uploadService import UploadService
from micro_storage_service.service.fetchService import FetchService
from core.logger.logging import log
import logging

logger=logging.getLogger('mylogger')

class UploadFileController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._uploadService:UploadService=UploadService()

    @log(logger=logger)
    def post(self,request,id):
        message=self._uploadService.upload(request=request,id=id)
        return Response(message,status=status.HTTP_200_OK)

class FetchFileController(APIView):

    @log(logger=logger)
    def get(self,request,uri,id):
        fetches=FetchService(request=request,uri=uri,id=id)
        message=fetches.fetch()
        return Response(message,status=status.HTTP_200_OK)
