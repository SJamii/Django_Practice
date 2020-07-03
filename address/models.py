from django.db import models

class district(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    population = models.IntegerField()
    literacy = models.CharField(max_length=100)
    subdivision = models.CharField(max_length=200)

    def __str__(self):
        return self.name

