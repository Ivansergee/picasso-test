import time
from celery import shared_task

from .models import File


@shared_task
def process_file(file_id, file_type):
    file = File.objects.get(id = file_id)
    if file_type.startswith('image'):
        print('process image')
    elif file_type == 'application/pdf':
        print('process pdf')
    elif file_type in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
        print('process excel sheet')
    else:
        print('unsupported file')
        return
    file.processed = True
    file.save()