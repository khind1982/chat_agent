from django.urls import path
from . import views

urlpatterns = [
    path('retrieve_and_return_data/', views.RetrieveData.as_view(), name='home')
]
