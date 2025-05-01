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
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from tokenapp.serializers  import LoginSerializer,UserSerializer,RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
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



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=401)
        
class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({
            'message':'welcome to dashboard',
            'user':user_serializer.data
        },200)