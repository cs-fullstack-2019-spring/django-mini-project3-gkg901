from django.db import models
from django.utils import timezone


# Create your models here.


class TeacherModel(models.Model):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)
    hours = models.DecimalField(max_digits=999, decimal_places=2)
    date_of_work = models.DateField(default="")
    date_of_entry = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
