from django.db import models

# Create your models here.
class Job(models.Model):
    #Images
    image = models.ImageField(upload_to='images/')
    #summary
    summary = models.CharField(max_length=100)
    #link to project
    link = models.CharField(max_length=100)


    def __str__(self):
        return self.summary
