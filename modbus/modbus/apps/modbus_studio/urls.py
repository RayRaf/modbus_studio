from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('generate_report/', views.generate_report, name='generate_report'),
]
