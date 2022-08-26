

from django.db import models
from django.db.models.fields import CharField, IntegerField ,EmailField

# Create your models here.


class Feedback(models.Model):
    name=models.CharField(max_length=20 , null=False )
    email=models.EmailField(null=False)
    comments=CharField(max_length=150 ,null=False)


    def __str__(self):
        return self.name

