import base64

class Decode:

    @staticmethod
    def decoding(music_obj,musicCover_obj)->dict:
        try:
            return {
                "decoded_music_obj":base64.b64decode(music_obj),
                "decoded_musicCover_obj":base64.b64decode(musicCover_obj)
            }
        except Exception as e:
            raise Exception(str(e))