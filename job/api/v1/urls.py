from django.urls import path
from . import views

app_name = 'job-rest-v1'

urlpatterns = [
    path('', views.job_list, name = 'list'),
    path('<int:job_id>', views.job_details, name = 'details'),
    path('create', views.job_create, name = 'create'),
    path('update/<int:job_id>', views.job_update, name = 'update'),
    path('delete/<int:job_id>', views.job_delete, name = 'delete'),
]