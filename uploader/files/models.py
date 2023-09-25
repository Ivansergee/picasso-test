from django.db import models

class File(models.Model):

    file = models.FileField(upload_to="uploads/%d%m%y/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
