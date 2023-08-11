
import base64

class UploadRepo:
    def __init__(self, request,id):
        self.request=request
        self.id=id
        
    
    def _parse_req(self):
        self.music_filename=self.request.data['music_filename']
        self.music_fileobj=self.request.data['music_fileobj'].split(',')[1]
        self.music_cover_filename=self.request.data['music_cover_filename']
        self.music_cover_fileobj=self.request.data['music_cover_fileobj'].split(',')[1]
        self.artist_name=self.request.data['artist_name']
        self.desc=self.request.data['desc']


    def _decoding(self):
        self.decode_music=base64.b64decode(self.music_fileobj)
        self.decode_music_cover=base64.b64decode(self.music_cover_fileobj)

    def _write_objs(self):
        try:
            with open(f'media/{self.music_filename}','wb') as f:
                f.write(self.decode_music)
                f.close()

            with open(f'media/{self.music_cover_filename}','wb') as f:
                f.write(self.decode_music_cover)
                f.close()
        except Exception  as e:
            raise Exception(str(e))
    
    def process(self):
        self._parse_req()
        self._decoding()
        self._write_objs()