from django.db import models


class Settings(models.Model):
    lazy = models.BooleanField()
    active = models.BooleanField()