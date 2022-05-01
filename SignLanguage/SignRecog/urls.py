from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recognize-sign', views.read_sign, name='sign'),
]