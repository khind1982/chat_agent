from django.urls import path
from . import views

urlpatterns = [
    path('retrieve_and_return_data/', views.retrieve_data, name='retrieve_data')
]
