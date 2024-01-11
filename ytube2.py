# -*- coding: utf-8 -*-


import os
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from googleapiclient.discovery import build
#from google_apis import create_service

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secrets.json", scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])


flow.run_local_server(port=8080, prompt="consent",authorization_prompt_message='')

credentials = flow.credentials

print(credentials.to_json())