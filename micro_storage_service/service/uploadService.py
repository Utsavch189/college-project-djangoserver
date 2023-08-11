from micro_storage_service.models import File
from micro_storage_service.repository.uploadRepository import UploadRepo
from datetime import datetime
from micro_storage_service.serializer.uploadSerializer import SaveFile

class UploadService:

    def __init__(self, request,id):
        self.request=request
        self.id=id
        self.repo=UploadRepo(request=self.request,id=self.id)
        self.uri=str(int(datetime.timestamp(datetime.now())))+str(self.id)

    def upload(self):
        try:
            self.repo.process()
            File.objects.create(
                uri=self.uri,music_file=self.repo.music_filename,music_cover_filename=self.repo.music_cover_filename,user_id=self.id,artist_name=self.repo.artist_name,description=self.repo.desc,http_uri=self.request.META['HTTP_HOST']+'/api/v1/storage/'+f'getfile/uri={self.uri}&id={self.id}'
            )
            return {"info":"files are uploaded!","http_uri":self.request.META['HTTP_HOST']+'/api/v1/storage/'+f'getfile/uri={self.uri}&id={self.id}'}
        except Exception  as e:
            raise Exception(str(e))


