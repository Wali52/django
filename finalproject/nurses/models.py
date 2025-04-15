from django.db import models


class DepartmentModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

# Create your models here.
class NurseModel (models.Model):
        
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)


    qualification = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

    depart_choices = [
        ('ICU','ICU'),
        ('Pediatrics','Pediatrics'),
        ('Emergency','Emergency'),
        ('OPD','OPD')
    ]
    # department = models.CharField(max_length=100,choices=depart_choices)  # e.g., ICU, Pediatrics, Emergency
    departments = models.ForeignKey(DepartmentModel, on_delete=models.SET_NULL, null=True, blank=True)


    shift = models.CharField(max_length=20, choices=[
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ])

    assigned_room = models.CharField(max_length=10, blank=True, null=True)
    assigned_doctor = models.CharField(max_length=100, blank=True, null=True)  # OR use ForeignKey if Doctor model is present

    joined_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.id})"
    

