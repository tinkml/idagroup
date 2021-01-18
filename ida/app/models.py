from django.db import models


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    file_format = models.CharField(max_length=5, null=True)
    url = models.URLField(null=True)


class ResizedImage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    original_image = models.ForeignKey('Image', related_name='resized_image', on_delete=models.CASCADE)
