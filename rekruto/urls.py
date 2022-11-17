from django.urls import path
from . import views

urlpatterns = [
    path('rekruto/templates/rekruto/',views.home),
    path('rekruto/templates/rekruto/rekruto',views.rekruto)
]