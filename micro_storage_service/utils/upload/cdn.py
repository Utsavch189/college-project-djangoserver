import cloudinary
import cloudinary.uploader

class CDN:
    def __init__(self) -> None:
        try:
            cloudinary.config(
                cloud_name="dcf6uk047",
                api_key="176572318442856",
                api_secret="C0hg2pOkd-7MoOdoeXLcF-RMHTk",
                secure=True,
            )
        except Exception as e:
            raise Exception(str(e))
    
    def upload(self,source:str,destination:str)->dict:
        try:
            res=cloudinary.uploader.upload(
                source,
                use_filename=True,
                unique_filename=False,
                resource_type='auto',
                public_id=destination
            )
            return res
        except Exception as e:
            raise Exception(str(e))