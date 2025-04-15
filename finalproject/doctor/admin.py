from django.contrib import admin
from doctor.models import DoctorModel,DepartmentModel
# Register your models here.

admin.site.register(DoctorModel)
admin.site.register(DepartmentModel)