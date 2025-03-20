from django.db import models


class BackupHistory(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
