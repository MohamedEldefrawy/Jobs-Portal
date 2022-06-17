from django.urls import path

from . import views

app_name = 'notification-rest-v1'

urlpatterns = [
    path("<int:user_id>", views.get, name="get_notifications"),
]
