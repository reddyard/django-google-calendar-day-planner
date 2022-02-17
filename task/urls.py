from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_task, name='create_task'),
]
