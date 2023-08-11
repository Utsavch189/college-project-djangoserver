from rest_framework import serializers
from micro_storage_service.models import File

class SaveFile(serializers.ModelSerializer):
    class Meta:
        model=File
        fields='__all__'