from typing import Any
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from micro_storage_service.service.upload.mainService import MainUploadService
from micro_storage_service.service.fetch.mainService import MainFetchService
from core.logger.logging import log
import logging

logger=logging.getLogger('mylogger')

class UploadFileController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._uploadService:MainUploadService=MainUploadService()

    @log(logger=logger)
    def post(self,request,id):
        message=self._uploadService.process(request=request,id=id)
        return Response(message,status=status.HTTP_200_OK)

class FetchFileController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._fetchService:MainFetchService=MainFetchService()

    @log(logger=logger)
    def get(self,request,uri):
        message=self._fetchService.fetch(uri=uri)
        return Response(message,status=status.HTTP_200_OK)
