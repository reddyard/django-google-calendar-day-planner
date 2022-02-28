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

        # creds = None
        # if os.path.exists('token.json'):
        #     creds = Credentials.from_authorized_user_file('token.json', settings.GOOGLE_CALENDAR_SCOPES)
        #     #сreds = Credentials.from_authorized_user_info(settings.GOOGLE_CALENDAR_SCOPES)
        # # If there are no (valid) credentials available, let the user log in.
        # if not creds or not creds.valid:
        #     if creds and creds.expired and creds.refresh_token:
        #         creds.refresh(Request())
        #     else:
        #         flow = InstalledAppFlow.from_client_secrets_file('task\client_secret.json',
        #                                                          settings.GOOGLE_CALENDAR_SCOPES)
        #         creds = flow.run_local_server(port=0)
        #     # Save the credentials for the next run
        #     with open('token.json', 'w') as token:
        #         token.write(creds.to_json())

        social_token = SocialToken.objects.get(account__user=request.user)

        creds = Credentials(token=social_token.token,
                            refresh_token=social_token.token_secret,
                            client_id=social_token.app.client_id,
                            client_secret=social_token.app.secret)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        test_event = {
            'summary': form.cleaned_data.get('description'),
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

    form = TaskForm()

    return render(request, 'task/create_task.html', {'form': form})
