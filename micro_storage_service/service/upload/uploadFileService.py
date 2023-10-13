from micro_storage_service.utils.upload.decode import Decode
from micro_storage_service.DTO.upload.main import UploadAPI
from micro_storage_service.utils.upload.cdn import CDN

class UploadFileService:

    def __init__(self,dto:UploadAPI) -> None:
        self._dto=dto
    
    def _uploadToCdn(self)->dict:
        try:
            #https://res.cloudinary.com/dcf6uk047/video/upload/v1697178895/nft_assets/nftmy.mp3
            
            decoded_dict:dict=Decode.decoding(music_obj=self._dto.music_fileobj,musicCover_obj=self._dto.music_cover_fileobj)
            
            music_file_name=self._dto.music_filename.split(".")[0]
            music_cover_filename=self._dto.music_cover_filename.split(".")[0]

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