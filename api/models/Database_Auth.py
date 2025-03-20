from django.db import models


class ConnectionParameter(models.Model):
    host = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
