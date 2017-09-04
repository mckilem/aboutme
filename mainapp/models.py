from django.db import models


# Create your models here.

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=32)
    image_path = models.CharField(verbose_name='Image', max_length=255)
    site = models.CharField(verbose_name='Сайт', max_length=255, blank=True)


class Work(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, verbose_name='Организация')
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')

class Study(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Organization', max_length=32)
    site = models.CharField(verbose_name='Web page', max_length=255, blank=True)
    image_path = models.CharField(verbose_name='Image', max_length=255)

class Hobby(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name='Hobby description')

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name='Skill description')

