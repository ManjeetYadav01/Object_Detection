from django.db import models

# Create your models here.

class Detect(models.Model):
    ifile=models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.ifile
        