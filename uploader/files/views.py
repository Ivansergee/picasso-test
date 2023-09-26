import magic
from django.conf import settings
from rest_framework import generics, serializers
from rest_framework.parsers import MultiPartParser

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileCreateView(generics.CreateAPIView):
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser]
    def perform_create(self, serializer):
        file_obj = self.request.FILES['file']
        mime = magic.Magic(mime=True)
        file_type = mime.from_buffer(file_obj.read())
        if file_type in settings.ALLOWED_FILE_TYPES:
            file = serializer.save()
            process_file.delay(file.id, file_type)
        else:
            raise serializers.ValidationError('Unsupported file type')


class FileListView(generics.ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()