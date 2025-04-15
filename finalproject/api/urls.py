from django.urls import path,include
from . import views
from .views import StaffView,StaffDetailView, PatientView,PatientDetailView,NurseView,NurseDetailView,DoctorView,DoctorDetailView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('staff',viewset=StaffView,basename='staff')

urlpatterns = [
    path('staff/', StaffView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),

    path('patient/',PatientView.as_view()),
    path('patient/<int:pk>/',PatientDetailView.as_view()),

    path('nurse/',NurseView.as_view()),
    path('nurse/<int:pk>/',NurseDetailView.as_view()),

    path('doctor/',DoctorView.as_view()),
    path('doctor/<int:pk>/',DoctorDetailView.as_view(),)
]
