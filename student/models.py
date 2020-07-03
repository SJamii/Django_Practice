from django.db import models

class std(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    cgpa = models.FloatField()
    std_class = models.IntegerField()
    gender = models.CharField(max_length=50)
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.name
