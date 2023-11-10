from django.db import models
import uuid
# Create your models here.

class Car(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),blank=False,null=False,primary_key=True,editable=False)
    make = models.CharField(max_length=50,null=True,blank=True)
    model = models.CharField(max_length=50,null=True,blank=True)
    descriptions = models.TextField(null=True,blank=True) 
    