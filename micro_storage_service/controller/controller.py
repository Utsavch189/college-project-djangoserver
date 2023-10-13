from typing import Any
from rest_framework.response import Response
from rest_framework.views import APIView
from micro_storage_service.service.upload.mainService import MainUploadService
from micro_storage_service.service.fetch.mainService import MainFetchService
from core.logger.logging import log
import logging
from micro_storage_service.DTO.upload.main import UploadAPI

logger=logging.getLogger('mylogger')

class UploadFileController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._uploadService:MainUploadService=MainUploadService

    @log(logger=logger)
    def post(self,request,id):
        message,status_code=self._uploadService().process(dto=UploadAPI(**request.data),id=id)
        return Response(message,status=status_code)

class FetchFileController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._fetchService:MainFetchService=MainFetchService()

    @log(logger=logger)
    def get(self,request,uri):
        message,status_code=self._fetchService.fetch(uri=uri)
        return Response(message,status=status_code)
