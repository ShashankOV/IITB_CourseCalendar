
from __future__ import print_function
import httplib2
import os
from os import system
from data import *
from copy import copy

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'IITB Course Calendar'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'IITB-course-calendar.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
    
def create_event(service, calendarID, sem_start_date, end_date, slot, course_code, course_name, instructor, is_tutorial, location):
    """Creates an course event in the calender given by calenderID
    
    Returns:
        The event ID.
    """
    recurring_event = []
    start_date = copy(sem_start_date)
    for individual_slot in SLOT_DATA[slot]:
        # Get start date
        days = list(individual_slot['day'])
        for i in range(len(days)):
            if (start_date.weekday() > days[i]):
                if ( i == len(days) - 1):
                    start_date += datetime.timedelta(7 + days[0] - start_date.weekday())
                    break
                continue
            else: 
                start_date += datetime.timedelta(days[i] - start_date.weekday()) 
                break
        #print(start_date)
        input('Press Enter to continue... ')
        
        # Create Event Resource
        event = {
            'anyoneCanAddSelf': True,
            'summary': course_code + ': ' + course_name,
            'description': instructor,
            'location': location,
            'visibility': 'public',
            'guestsCanSeeOtherGuests': False,
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 30},
                    {'method': 'popup', 'minutes': 10},
                ]
            },
            #attendees': [
            #    {'email': 'electrical-2k14@googlegroups.com'}   
            #],
            'start': {
                'dateTime': str(start_date) + 'T' + individual_slot['start'],
                'timeZone': 'Asia/Kolkata'
            },
            'end': {
                'dateTime': str(start_date) + 'T' + individual_slot['end'],
                'timeZone': 'Asia/Kolkata'
            },
            'recurrence': [
                individual_slot['recurrence'] + ';UNTIL=' + '{:%Y%m%d}'.format(end_date) + 'T235900Z'
            ],
            'colorId': "8" if is_tutorial else individual_slot['color'] 
        }
        recurring_event.append(service.events().insert(calendarId = calendarID, body = event, sendNotifications = False).execute())
        #page_token = None
        #while True:
            #events = service.events().instances(calendarId='primary', eventId=recurring_event[-1]['id'], pageToken=page_token).execute()
            #for event in events['items']:
                #if (event['start']['dateTime'][0:10] == '2017-01-09'):
                #   service.events().delete(calendarId='primary', eventId=event['id']).execute()
                #page_token = events.get('nextPageToken')
            #if not page_token:
                #break
        
    return recurring_event


def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    
    # Adding a secondary calendar
    
    #new_calendar = {
    #    'summary': 'Example',
    #    #'description': 'An example addition of a calendar',
    #    'timeZone': 'Asia/Kolkata'
    #}
    #created_calendar = service.calendars().insert(body = new_calendar).execute()
    #print(created_calendar['id'])
    
    # event_list = create_event(service, 'primary', datetime.date(2017, 1, 2), datetime.date(2017, 4, 14), '5', 'CS 213', 'Data Structures and Algorithms', 'G. Ramakrishnan', False, 'CC 103')
    
    # inp = input('Do you want to delete the events created? (Y/N)')
    # inp.lower()
    # if (inp == 'y'):
        # for event in event_list:
            # service.events().delete(calendarId = 'primary', eventId = event['id']).execute()
        # print('All events created, deleted succesfully!')
        
    # page_token = None
    # while True:
        # calendar_list = service.calendarList().list(pageToken=page_token).execute()
        # for calendar_list_entry in calendar_list['items']: 
            # print (calendar_list_entry['summary'])
        # page_token = calendar_list.get('nextPageToken')
        # if not page_token:
            # break
    now = '2017-02-20T00:00:00Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
       calendarId='primary', timeMin=now, maxResults=19, singleEvents=True,
       orderBy='startTime').execute()
    events = eventsResult.get('items', [])
	
    if not events:
       print('No upcoming events found.')
    for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
       print(start, event['summary'])
       service.events().delete(calendarId='primary', eventId=event['id']).execute()


if __name__ == '__main__':
    main() 
