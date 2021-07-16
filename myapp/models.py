from django.db import models
import datetime


# Create your models here.
# models.py
class Employee(models.Model):
    name = models.CharField(max_length=99)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    date = models.DateField("Date", default=datetime.date.today)

    class Meta:
        db_table = "employee"
