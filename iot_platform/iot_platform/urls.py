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
    path('admin-register/', views.AdminRegister.as_view(), name='admin-register'),
    path('company/', views.CompanyView.as_view(), name='company-list-create'),
    path('company/<int:pk>/', views.CompanyView.as_view(), name='company-detail'),
    path('admin-locations/', views.AdminLocationView.as_view(), name='admin-locations'),
    path('admin-locations/<int:pk>/', views.AdminLocationView.as_view(), name='admin-location-detail'),
    path('company/locations/', views.CompanyLocationView.as_view(), name='company-location-list'),
    path('company/locations/<int:pk>/', views.CompanyLocationView.as_view(), name='company-location-detail'),
]
