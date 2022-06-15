from django.urls import path

from . import views

app_name = 'account-rest-v1'

urlpatterns = [
    path("register", views.register, name="register"),
    path('login', views.CustomAuthToken.as_view()),
    path('logout', views.logout),
    path("user/<int:user_id>", views.user, name="get_user"),
]
