from rest_framework import generics
from rest_framework.parsers import MultiPartParser

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileCreateView(generics.CreateAPIView):
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer):
        file = serializer.save()
        process_file.delay(file.id)


class FileListView(generics.ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()