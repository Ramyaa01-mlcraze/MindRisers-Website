from django.urls import path
from . import views

urlpatterns=[
    path('',views.baseHome,name='baseHome'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login')
]