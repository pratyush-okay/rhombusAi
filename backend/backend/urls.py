from django.urls import path, include
from dataprocessing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_data/', include('dataprocessing.urls')),
]
