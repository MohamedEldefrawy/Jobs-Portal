from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'account-rest-v1'

urlpatterns = [
    path("register", views.register, name="register"),
    path('login', views.CustomAuthToken.as_view()),
    path('logout', views.logout),
    path("user", views.view_user, name="view"),
    path("user/<int:user_id>", views.user, name="get_user"),
]
