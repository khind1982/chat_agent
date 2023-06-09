from django.db import models


class Settings(models.Model):
    lazy = models.BooleanField()
    active = models.BooleanField()
    cold = models.BooleanField()
    mild = models.BooleanField()
    hot = models.BooleanField()
    city = models.BooleanField()
    mountain = models.BooleanField()
    sea = models.BooleanField()