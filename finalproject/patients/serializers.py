from rest_framework import serializers
from .models import PatientModel

class PatientSerializer (serializers.ModelSerializer):
    class Meta :
        model = PatientModel
        fields = '__all__'

# class DoctorSelectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DoctorSelectionModel
#         fields = '__all__'

