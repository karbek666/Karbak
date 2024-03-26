from django.db import models


class Marsel(models.Model):
    name = models.TextField('Name:')
    id = models.IntegerField('1:')