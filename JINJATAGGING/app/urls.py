from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('register/',register,name = 'request'),
    path('login/',login,name = 'login')
]