from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import AboutView

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('logged-in/', 'task/create_task.html', name='logged_in'),
    path('', AboutView.as_view()),
    path('login/', views.login_view, name='login'),
]
