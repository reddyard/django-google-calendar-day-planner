from django.shortcuts import render
from .forms import TaskForm

'''Google Calendar API'''
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']


def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('D:\django-google-calendar-day-planner\\task\\'
                                                             'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    test_event = {
        'summary': form.cleaned_data.get('title'),
        'start': {
            'dateTime': now,
            'timeZone': 'Asia/Tomsk',
        },
        'end': {
            'dateTime': now,
            'timeZone': 'Asia/Tomsk',
        },
    }

    test_event = service.events().insert(calendarId='primary', body=test_event).execute()

    return render(request, 'task/create_task.html', {'form': form})
