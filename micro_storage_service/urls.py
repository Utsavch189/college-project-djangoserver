from django.urls import path
from micro_storage_service.controller.controller import UploadFileController,FetchFileController

urlpatterns = [
    path('upload/id=<str:id>',UploadFileController.as_view()),
    path('getfile/uri=<str:uri>',FetchFileController.as_view())
]
