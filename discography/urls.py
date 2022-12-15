from django.urls import path
from . import views

app_name = "discography"
urlpatterns = [
    path('index/', views.index, name="index"),
    
]
