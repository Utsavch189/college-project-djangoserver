from micro_storage_service.utils.upload.decode import Decode
from micro_storage_service.DTO.upload.writeobjDto import WriteFileDTO

class WriteFileService:

    def write(self,dto:WriteFileDTO,id:str)->bool:
        try:
            decoded_dict:dict=Decode.decoding(music_obj=dto.uploaddto.music_fileobj,musicCover_obj=dto.uploaddto.music_cover_fileobj)
            with open(f'media/nft/{id}'+f'{dto.uploaddto.music_filename}','wb') as f:
                f.write(decoded_dict['decoded_music_obj'])
                f.close()

            
            with open(f'media/nft/{id}'+f'{dto.uploaddto.music_cover_filename}','wb') as s:
                s.write(decoded_dict['decoded_musicCover_obj'])
                s.close()
            return True
        except Exception as e:
            raise Exception(str(e))