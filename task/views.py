from django.conf import settings
from django.shortcuts import render
from .forms import TaskForm

import os.path
import datetime

'''Google Calendar API'''
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialToken


@login_required
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()

    form = TaskForm()

    return render(request, 'task/create_task.html', {'form': form})
