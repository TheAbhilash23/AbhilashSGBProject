from . import views
from django.urls import path

urlpatterns = [
    path('custid/<int:pk>',views.custid,name='apihome'),
    path('custid/all',views.showall,name='showall'),
    path('editdb/',views.editdb,name='editdb'),
    path('analyzerapi/',views.analyzerapi, name='analyzerapi'),
]
