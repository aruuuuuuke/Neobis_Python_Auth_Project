from django.urls import path
from .views import signup, home, user_login

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),

]
