from django.db import models

# Create your models here.

class StaffModel(models.Model):
    role_choices = [
        ('Receptionist','Receptionist'),
        ('Admin','Admin'),
        ('Emergency','Emergency'),
        ('ICU','ICU'),
        ('Cleaner','Cleaner'),
        ('Technician','Technician'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20,choices=role_choices)
    contact_info = models.CharField(max_length=15)

    def __self__(self):
        return self.name
