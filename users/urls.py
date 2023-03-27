from django.urls import path
from .views import user_registration, login_user, logout_user

app_name='users'

urlpatterns = [
    path("register/", user_registration, name='user_register'),
    path('login/', login_user, name='user_login'),
    path('logout/', logout_user, name='logout_user')
]
