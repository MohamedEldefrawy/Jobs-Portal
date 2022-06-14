from django.urls import path

from .views import developer_registration, company_registration, login, view_user

app_name = "account"
urlpatterns = [
    path("developer/register/", developer_registration, name="developer-register"),
    path("company/register/", company_registration, name="company-register"),
    path("login/", login, name="login"),
    path("user/", view_user, name="view"),
]
