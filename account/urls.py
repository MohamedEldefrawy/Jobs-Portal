from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import register, login, view_user, user

app_name = "account"
urlpatterns = [
    path('login', obtain_auth_token),
    path("register", register, name="register"),
    path("user", view_user, name="view"),
    path("users/<int:user_id>", user, name="get_user"),
]
