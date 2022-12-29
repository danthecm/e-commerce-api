from django.urls import path
from . import views

app_name = "api"


urlpatterns = [
    path('', views.CreateAdmin.as_view(), name='create_admin')
]
