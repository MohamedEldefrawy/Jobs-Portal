from django.urls import path

from .views import register, login, view_user, user

app_name = "account"
urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("user/", view_user, name="view"),
    path("users/<int:pk>", user, name="get_user"),
]
