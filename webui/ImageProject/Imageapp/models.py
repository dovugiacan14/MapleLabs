from django.db import models

# Create your models here.
class Search(models.Model):
    prompt = models.CharField(max_length= 500)
