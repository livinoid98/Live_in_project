from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='find'),
    path('detail/<int:hospital_id>', views.detail, name='Hospital_detail'),
]