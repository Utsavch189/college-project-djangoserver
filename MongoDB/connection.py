import pymongo
from dataclasses import dataclass,field
from typing import Any

@dataclass(init=False)
class Connection:
    con = "mongodb+srv://utsav:utsav@cluster0.rqeuq69.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(con,tls=True,tlsAllowInvalidCertificates=True)

@dataclass
class ConnectCollection(Connection):
    db:object=field(default_factory=object)
    collection:object=field(default_factory=object)
    db_name:str=field(default_factory=str)
    col_name:str=field(default_factory=str)

    def __post_init__(self):
        self.db=self.client[self.db_name]
        self.collection=self.db[self.col_name]