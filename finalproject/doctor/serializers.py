from doctor.models import DoctorModel
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorModel
        fields = '__all__'
        