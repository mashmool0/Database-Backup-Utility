from django.db import models


class ConnectionParameter(models.Model):
    host = models.CharField(max_length=100, blank=True, null=True)
    port = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
