from django.db import models

# Create your models here.
class testelement(models.Model):
    value=models.CharField(max_length=100)
