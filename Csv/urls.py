"""Csv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path
# from Csv.csv_app.views import home
from csv_app.views import csv_export , home , upload_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csv-export/', csv_export , name= 'csv-export' ),
    path('home/', home),
    path('upload-csv/', upload_csv, name= "upload_csv"),
]
