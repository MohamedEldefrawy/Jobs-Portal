from django.urls import path
from tag import views

app_name = 'tags'
urlpatterns = [
    path('', views.tags),
]
