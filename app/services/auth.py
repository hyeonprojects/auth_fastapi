import os

from fastapi import Depends
from fastapi.security import SecurityScopes
from google.auth.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SECRET_KEY = ''
ALGORITHM = ''
ACCESS_TOKEN_EXPRIRE_MINUTES = 30
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


async def get_current_user(security_scopes: SecurityScopes, token: str = Depends()):
    pass


async def google_oauth():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.vaild:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())



    try:
        service = build('people', 'v1', credentials=creds)

        print('List 10 connection names')

        results = service.people().connections().list(
            resourceName = 'people/me',
            pageSize = 10,
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])

        for person in connections:
            names = person.get('names', [])
            if names:
                name = names[0].get('displayName')
                print(name)
    except HttpError as err:
        print(err)
