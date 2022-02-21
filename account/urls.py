from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('logged-in/', 'task/create_task.html', name='logged_in'),
    path('', TemplateView.as_view(template_name='account/index.html')),
    path('login/', views.login_view, name='login'),
]
