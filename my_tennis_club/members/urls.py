from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('court/', views.courts, name='courts'),
    path('court/details_courts/<int:id>', views.details_courts, name='details_courts'),
]