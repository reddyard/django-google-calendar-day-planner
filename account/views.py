from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from allauth.socialaccount.providers.google import provider


class AboutView(TemplateView):
    template_name = "account/index.html"


def login_view(request):
    template = 'account/login.html'
    form = LoginForm
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_authenticated:
                login(request, user)
                messages.success(request, "You have logged in!")
                return redirect('/tasks/create/')
            else:
                messages.warning(request, "Your account is disabled!")
                return redirect('/accounts/google/login/')
        else:
            messages.warning(request, "The username or password are not valid!")
            return redirect('/accounts/google/login/')
    context = {'form': form}
    return render(request, template, context)