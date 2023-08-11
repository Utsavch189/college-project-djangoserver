from micro_storage_service.models import File

class FetchService:

    def __init__(self,request,uri,id):
        self.request=request
        self.uri=uri
        self.id=id
        self.file=File.objects.get(uri=uri)
        self.stat,self.message=self.checks()
    def checks(self):

        if (not File.objects.filter(uri=self.uri).exists()) and File.objects.get(uri=self.uri).user_id!=self.id:
            return False,{"info":"no records!"}
        
        else:
            return True,{}
        
    def fetch(self):
        try:
            if self.stat:
                return {
                    "uri":self.file.uri,
                    "userid":self.file.user_id,
                    "music_file":self.request.META['HTTP_HOST']+'/media/'+self.file.music_file,
                    "music_name":self.file.music_file.replace('.mp3',''),
                    "image_file":self.request.META['HTTP_HOST']+'/media/'+self.file.image_file,
                    "artist_name":self.file.artist_name,
                    "description":self.file.description,
                    "http_uri":self.file.http_uri
                }
            else:
                return self.message
        except Exception  as e:
            print(e)
