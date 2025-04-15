from rest_framework import serializers
from nurses.models import NurseModel

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseModel
        fields = '__all__'