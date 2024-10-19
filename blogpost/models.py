from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class sample(models.Model):
    head=models.CharField(max_length=100)
    information=RichTextField()