from MongoDB.connection import ConnectCollection
import requests
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

class MyPlaylist:
  
    def __init__(self,request,userid):
        self.request=request
        self.userid=userid
        self.col=ConnectCollection(db_name="rythmXchange",col_name="playlist")
        
    
    @staticmethod
    def _is_exist(uri="",userid="",col=None):
        if uri!="":
            filters={"uri":uri,"userid":userid}
        else:
            filters={"userid":userid}
        if col.find_one(filters):
            return True
        else:
            return False

    def addToDB(self):
        try:
            self.http_uri=self.request.data['http_uri']
            self.data=requests.get(self.http_uri).json()   
            if not MyPlaylist._is_exist(uri=self.data['uri'],userid=self.userid,col=self.col.collection):
                self.col.collection.insert_one(self.data)
                return True,{"info":"successfully added!"}
            else:
                return False,{"info":"already added!"}
        except Exception as e:
            print(e)

    def getFromDB(self):
        try:
            filters={"userid":self.userid}
            datas=[]
            if not MyPlaylist._is_exist(userid=self.userid,col=self.col.collection):
                return False,{"info":datas}
            
            for data in self.col.collection.find(filters,{ "_id": 0}):
                datas.append(data)
            return True,{"info":datas}
        except:
            pass
    
    def deleteFromDB(self):
        try:
            self.uri=self.request.data['uri']

            if not MyPlaylist._is_exist(uri=self.uri,userid=self.userid,col=self.col.collection):
                return False,{"info":"not found!"}
            
            self.col.collection.delete_one({
                "uri":self.uri,
                "userid":self.userid
            })
            return True,{"info":"successfully deleted!"}
        except:
            pass