from django.db import models

class Api(models.Model):
    heading = models.CharField(max_length=70, blank=False, default='')
    desc=models.CharField(max_length=200, blank=False, default='')
    published=models.BooleanField(default=False)