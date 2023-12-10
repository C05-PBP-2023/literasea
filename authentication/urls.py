from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("login-mobile/", login_mobile, name="login_mobile"),
    path("logout-mobile/", logout_mobile, name="logout_mobile"),
    path("register-mobile/", register_mobile, name="register_mobile")
]
