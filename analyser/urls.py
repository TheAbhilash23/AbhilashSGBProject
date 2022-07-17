from . import views
from django.urls import path


urlpatterns = [
    path('mlmodel/',views.mlmodel),
    path('correlation/',views.correlation),
    
    
    
]


