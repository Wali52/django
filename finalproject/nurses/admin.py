from django.contrib import admin
from nurses.models import NurseModel,DepartmentModel
# Register your models here.

admin.site.register(NurseModel)
admin.site.register(DepartmentModel)
