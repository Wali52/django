from django.shortcuts import render
from staff.models import StaffModel
from staff.serializers import StaffSerializer
from patients.models import PatientModel
from patients.serializers import PatientSerializer
from nurses.models import NurseModel
from nurses.serializers import NurseSerializer
from doctor.models import DoctorModel
from doctor.serializers import DoctorSerializer
from rest_framework import generics
# Create your views here.

class StaffView(generics.ListCreateAPIView):
    queryset=StaffModel.objects.all()
    serializer_class = StaffSerializer

class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializer
    lookup_field = 'pk'

class PatientView(generics.ListCreateAPIView):
    queryset = PatientModel.objects.all()
    serializer_class = PatientSerializer

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientModel.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'pk'

class NurseView(generics.ListCreateAPIView):
    queryset = NurseModel.objects.all()
    serializer_class = NurseSerializer

class NurseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NurseModel.objects.all()
    serializer_class = NurseSerializer
    lookup_field = 'pk'

class DoctorView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = DoctorModel.objects.all()

class DoctorDetailView (generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializer
