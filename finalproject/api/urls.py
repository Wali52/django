# from django.urls import path,include,re_path
# from . import views
# from .views import StaffView,StaffDetailView, PatientView,PatientDetailView,NurseView,NurseDetailView,DoctorView,DoctorDetailView
# from .views import RegisterView,LoginView,DashboardView
# from rest_framework.routers import DefaultRouter
# from tokenapp.serializers import RegisterSerializer
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# # router = DefaultRouter()
# # router.register('staff',viewset=StaffView,basename='staff')

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Hospital Managment System APIs",
#       default_version='v1',
#       description="API documentation for your Django project",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="your@email.com"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )



# urlpatterns = [
#     # API Endpoints

#     path('staff/', StaffView.as_view(), name='staff-list'),
#     path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),

#     path('patient/',PatientView.as_view()),
#     path('patient/<int:pk>/',PatientDetailView.as_view()),

#     path('nurse/',NurseView.as_view()),
#     path('nurse/<int:pk>/',NurseDetailView.as_view()),

#     path('doctor/',DoctorView.as_view()),
#     path('doctor/<int:pk>/',DoctorDetailView.as_view()),

#     # Authentication

#     path('auth/register/',RegisterView.as_view(),name='auth register'),
#     path('auth/login/',LoginView.as_view(),name='auth login'),
#     path('dashboard/',DashboardView.as_view(),name='dasboard'),


#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # Swagger Docs

#     # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     # re_path(r'^api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json')
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # ✅ clean path for Postman
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


from django.urls import path
from .views import (
    StaffView, StaffDetailView,
    PatientView, PatientDetailView,
    NurseView, NurseDetailView,
    DoctorView, DoctorDetailView,
    RegisterView, LoginView, DashboardView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hospital Management System APIs",
        default_version='v1',
        description="API documentation for your Django project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Staff
    path('staff/', StaffView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),

    # Patient
    path('patient/', PatientView.as_view(), name='patient-list'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # Nurse
    path('nurse/', NurseView.as_view(), name='nurse-list'),
    path('nurse/<int:pk>/', NurseDetailView.as_view(), name='nurse-detail'),

    # Doctor
    path('doctor/', DoctorView.as_view(), name='doctor-list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Authentication
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # JWT Tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger / OpenAPI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # ✅ for Postman
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

