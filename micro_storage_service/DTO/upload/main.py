from pydantic import BaseModel,constr,validator
import re

class UploadAPI(BaseModel):
    music_filename:constr(min_length=1,strip_whitespace=True)
    music_fileobj:constr(min_length=1,strip_whitespace=True)
    music_cover_filename:constr(min_length=1,strip_whitespace=True)
    music_cover_fileobj:constr(min_length=1,strip_whitespace=True)
    artist_name:constr(min_length=1,strip_whitespace=True)
    desc:constr(min_length=1,strip_whitespace=True)


