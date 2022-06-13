from django.urls import path

from .views import developer_registration, company_registration

app_name = "account"
urlpatterns = [
    path("developer/register/", developer_registration, name="developer-register"),
    path("company/register/", company_registration, name="company-register"),
]
