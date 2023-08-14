from django.db import models

class File(models.Model):
    uri=models.CharField(max_length=150,primary_key=True,default="")
    music_filename=models.CharField(max_length=150,null=True,blank=True)
    music_cover_filename=models.CharField(max_length=150,null=True,blank=True)
    user_id=models.CharField(max_length=150,null=True,blank=True)
    artist_name=models.CharField(max_length=150,null=True,blank=True)
    desc=models.TextField(default="")
    http_uri=models.CharField(max_length=150,null=True,blank=True)

    def __str__(self) -> str:
        return self.user_id
