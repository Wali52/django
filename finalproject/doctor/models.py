from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class DoctorModel(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    qualification = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()

    department = models.ForeignKey(DepartmentModel, on_delete=models.SET_NULL, null=True, blank=True)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)

    is_available = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)

    address = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"