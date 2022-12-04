from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('contact/', contact, name='contact'),
    path('enroll/', enroll, name='enroll'),
    path('profile/', profile, name='profile'),
    path('attendance/', attendance, name='attendance'),
]