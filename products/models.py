from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    descritpion = models.TextField()
    price       = models.TextField()
    summary     = models.TextField()
    active      = models.TextField(default='Produt Status')
