from django.db import models

# Create your models here.
from django.db import models

class Work(models.Model):
    organization = models.CharField(verbose_name='Organization', max_length=32)
    site = models.CharField(verbose_name='Web page', max_length=64, blank=True)
    image_path = models.CharField(verbose_name='Image', max_length=255)

class Study(models.Model):
    organization = models.CharField(verbose_name='Organization', max_length=32)
    site = models.CharField(verbose_name='Web page', max_length=64, blank=True)
    image_path = models.CharField(verbose_name='Image', max_length=255)


class Hobby(models.Model):
    text = models.TextField(verbose_name='Hobby description')

class Skill(models.Model):
    text = models.TextField(verbose_name='Skill description')