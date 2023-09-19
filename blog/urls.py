from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola ),
    path('hoja1/', views.hoja1 ), 
    
    
    
]
