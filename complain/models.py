from django.db import models

# Create your models here.
class storecomplain(models.Model):
    email = models.CharField(max_length=100)
    address =models.CharField(max_length=120)
    description =models.CharField(max_length=100)
