from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=1000, verbose_name='link')
    status = models.BooleanField(verbose_name='state link', default=True)
    short_link = models.CharField(max_length=1000, verbose_name='short_link', unique=True)
