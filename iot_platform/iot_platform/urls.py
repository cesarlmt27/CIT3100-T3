"""
URL configuration for iot_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/admin-register/', views.AdminRegister.as_view(), name='admin-register'),

    path('api/v1/company/', views.CompanyView.as_view(), name='company-list-create'),
    path('api/v1/company/<int:pk>/', views.CompanyView.as_view(), name='company-details'),

    path('api/v1/location-create/', views.CreateLocationView.as_view(), name='location-create'),
    path('api/v1/location/', views.CompanyLocationView.as_view(), name='location-list'),
    path('api/v1/location/<int:pk>/', views.CompanyLocationView.as_view(), name='location-view-update-delete'),

    path('api/v1/sensor-create/', views.CreateSensorView.as_view(), name='sensor-create'),
    path('api/v1/sensor/', views.CompanySensorView.as_view(), name='sensor-list'),
    path('api/v1/sensor/<int:pk>/', views.CompanySensorView.as_view(), name='sensor-view-update-delete'),

    path('api/v1/sensor-data/', views.SensorDataView.as_view(), name='sensor-data-create-view'),
]
