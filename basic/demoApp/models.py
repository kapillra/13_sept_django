from django.db import models

# Create your models here.
class Master(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)

    