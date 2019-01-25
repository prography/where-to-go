from django.db import models


class Landmark(models.Model):
    landmark = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.landmark


class Image(models.Model):
    url = models.TextField(unique=True)
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE)
    cluster1 = models.IntegerField()
    cluster2 = models.IntegerField()
    cluster3 = models.IntegerField()

    def __str__(self):
        return self.url
