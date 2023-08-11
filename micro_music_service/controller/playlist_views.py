from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from micro_music_service.services import playlist_service

class Playlist(APIView):

    def get(self,request,userid):
        try:
            myplaylist=playlist_service.MyPlaylist(request=request,userid=userid)
            stat,message=myplaylist.getFromDB()
            if stat:
                return Response(message,status=status.HTTP_200_OK)
            else:
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

    def post(self,request,userid):
        try:
            myplaylist=playlist_service.MyPlaylist(request=request,userid=userid)
            stat,message=myplaylist.addToDB()
            if stat:
                return Response(message,status=status.HTTP_200_OK)
            else:
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

    def delete(self,request,userid):
        try:
            myplaylist=playlist_service.MyPlaylist(request=request,userid=userid)
            stat,message=myplaylist.deleteFromDB()
            if stat:
                return Response(message,status=status.HTTP_200_OK)
            else:
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
        except:
            pass