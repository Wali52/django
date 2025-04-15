from django.db import models
from doctor.models import DoctorModel
from django.contrib.auth.models import User

# Create your models here.
# class DoctorSelectionModel(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name


class PatientModel(models.Model):
    gender_choices = [
        ('Male',"Male"),
        ('Female','Female'),
        ('Other','Other'),
    ]

    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=10,choices=gender_choices)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=12)
    email =  models.EmailField(blank=True,null=True)

    medical_history = models.TextField(blank=True,null=True)
    current_condition = models.TextField(blank=True,null=True)
    admission_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField(blank=True, null=True)

    attending_doctor = models.ForeignKey(DoctorModel,on_delete=models.SET_NULL, null=True, blank=True)
    room_number = models.CharField(max_length=10, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mr.{self.name} (ID: {self.id})"
    




