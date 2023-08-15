from micro_storage_service.utils.upload.decode import Decode
from micro_storage_service.DTO.upload.writeobjDto import WriteFileDTO

class WriteFileService:
    def __init__(self) -> None:
        self._decode:Decode=Decode()

    def write(self,dto:WriteFileDTO)->bool:
        try:
            decoded_dict:dict=self._decode.decoding(music_obj=dto.uploaddto.music_fileobj,musicCover_obj=dto.uploaddto.music_cover_fileobj)
            with open(f'media/{dto.uploaddto.music_filename}','wb') as f:
                f.write(decoded_dict['decoded_music_obj'])
                f.close()

            with open(f'media/{dto.uploaddto.music_cover_filename}','wb') as f:
                f.write(decoded_dict['decoded_musicCover_obj'])
                f.close()
            return True
        except Exception as e:
            raise Exception(str(e))