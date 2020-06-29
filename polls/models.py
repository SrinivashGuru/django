from django.db import models

# Create your models here.
class details (models.Model):
    name = models.CharField(max_length=35)
    age = models.IntegerField()
    sex = models.CharField(max_length=35)

    def __str__(self):
        return self.name