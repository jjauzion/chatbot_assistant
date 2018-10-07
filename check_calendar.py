from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def event_exists_at(time):
    """
    Check if an event exist in the calendar at the given time
    Return True is an event exist, False if calendar is free.
    """

    # If modifying these scopes, delete the file token.json.
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    time_end = time + datetime.timedelta(hours=1)
    time = time.isoformat()
    time_end = time_end.isoformat()
    print("start: {}; end: {}".format(time, time_end))
    events_result = service.events().list(calendarId='primary', timeMin=time, timeMax=time_end,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return False
    else:
        print('event!')
        return True

"""
    date_entry = input('Enter a date in YYYY-MM-DD-hh-mm format\n')
    year, month, day, hour, minute = map(int, date_entry.split('-'))
    date_start = datetime.datetime(year, month, day, hour=hour, minute=minute).astimezone().isoformat()
    date_end = datetime.datetime(year, month, day, hour=hour + 1, minute=minute).astimezone().isoformat()
    print("start: {}; end: {}".format(date_start, date_end))
"""
