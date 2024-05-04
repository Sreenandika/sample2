from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=150)
    place=models.CharField(max_length=200, null=True, blank=True)
    age=models.IntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
