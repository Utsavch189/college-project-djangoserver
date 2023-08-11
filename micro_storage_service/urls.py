from django.urls import path
from micro_storage_service.controller.storageController import UploadFileController,FetchFileController

urlpatterns = [
    path('upload/id=<str:id>',UploadFileController.as_view()),
    path('getfile/uri=<str:uri>&id=<str:id>',FetchFileController.as_view())
]
