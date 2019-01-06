from django.db import models


class Landmark(models.Model) :
    landmark = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    description = models.TextField()


class Image(models.Model):
    url = models.TextField()
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE)
