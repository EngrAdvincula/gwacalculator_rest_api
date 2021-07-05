from django.db import models

# Create your models here.
class Course(models.Model):
    subject = models.CharField(max_length=70)
    units = models.CharField(max_length=70)


    def __str__(self):
        return self.subject
