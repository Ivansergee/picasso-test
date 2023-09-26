from django.urls import path

from .views import FileCreateView, FileListView


urlpatterns = [
    path('upload/', FileCreateView.as_view(), name='upload-file'),
    path('files/', FileListView.as_view(), name='list-files'),
]