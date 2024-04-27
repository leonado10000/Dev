from django.db import models

# Create your models here.
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    textfield = models.CharField(max_length=2000)
    time = models.DateTimeField()
    sender = models.CharField(max_length=10,null=True)