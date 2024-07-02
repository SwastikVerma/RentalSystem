from django.urls import path
from .views import *

urlpatterns = [
    path('register', register_user, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('car/create', create_car,name = 'create_car'),
    path('car/rent', rent_car,name = 'rent_car'),
    
]