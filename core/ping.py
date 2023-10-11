from core.logger.logging import log
import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

logger=logging.getLogger('mylogger')

class Ping(APIView):

    @log(logger=logger)
    def get(self,request):
        return Response({"message":"ping pong"},status=status.HTTP_200_OK)