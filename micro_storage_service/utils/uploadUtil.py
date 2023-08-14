import base64
from micro_storage_service.dto.upload.writeobjDto import WriteFileDTO

class Decode:

    def decoding(self,music_obj,musicCover_obj)->dict:
        try:
            return {
                "decoded_music_obj":base64.b64decode(music_obj),
                "decoded_musicCover_obj":base64.b64decode(musicCover_obj)
            }
        except Exception as e:
            raise Exception(str(e))

class WriteFile:

    def __init__(self) -> None:
        self._decode:Decode=Decode()

    def write(self,dto:WriteFileDTO)->bool:
        try:
            decoded_dict:dict=self._decode.decoding(music_obj=dto.uploaddto.music_obj,musicCover_obj=dto.uploaddto.musicCover_obj)
            with open(f'media/{dto.uploaddto.music_filename}','wb') as f:
                f.write(decoded_dict['decoded_music_obj'])
                f.close()

            with open(f'media/{dto.uploaddto.music_cover_filename}','wb') as f:
                f.write(decoded_dict['decoded_musicCover_obj'])
                f.close()
            return True
        except Exception as e:
            raise Exception(str(e))
