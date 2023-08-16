from micro_storage_service.models import File
from rest_framework import serializers

class GetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields=['uri','music_filename','music_cover_filename','user_id','artist_name','desc','music_file_uri','music_cover_uri']