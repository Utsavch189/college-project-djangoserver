from micro_storage_service.utils.upload.decode import Decode
from micro_storage_service.DTO.upload.writeobjDto import WriteFileDTO
from micro_storage_service.utils.upload.cdn import CDN

class UploadFileService:

    def __init__(self,dto:WriteFileDTO,id:str) -> None:
        self._dto=dto
        self._id=id

    def _writeToLocal(self)->bool:
        try:
            decoded_dict:dict=Decode.decoding(music_obj=self._dto.uploaddto.music_fileobj,musicCover_obj=self._dto.uploaddto.music_cover_fileobj)
            with open(f'media/nft/{self._id}'+f'{self._dto.uploaddto.music_filename}','wb') as f:
                f.write(decoded_dict['decoded_music_obj'])
                f.close()

            
            with open(f'media/nft/{self._id}'+f'{self._dto.uploaddto.music_cover_filename}','wb') as s:
                s.write(decoded_dict['decoded_musicCover_obj'])
                s.close()
            return True
        except Exception as e:
            raise Exception(str(e))
    
    def _uploadToCdn(self)->dict:
        try:
            #https://res.cloudinary.com/dcf6uk047/video/upload/v1697178895/nft_assets/nftmy.mp3
            
            decoded_dict:dict=Decode.decoding(music_obj=self._dto.uploaddto.music_fileobj,musicCover_obj=self._dto.uploaddto.music_cover_fileobj)
            
            music_file_name=self._dto.uploaddto.music_filename.split(".")[0]
            music_cover_filename=self._dto.uploaddto.music_cover_filename.split(".")[0]

            cdn=CDN()

            music_cdn_res=cdn.upload(
                decoded_dict['decoded_music_obj'],
                destination = f"nft_assets/{music_file_name}",
              
            )
            cover_cdn_res=cdn.upload(
                decoded_dict['decoded_musicCover_obj'],
                destination = f"nft_assets/{music_cover_filename}",
                
            )
            return {
                "music_cdn":music_cdn_res,
                "music_cover_cdn":cover_cdn_res
            }
        except Exception as e:
            raise Exception(str(e))
    
    def process(self):
            return self._uploadToCdn()