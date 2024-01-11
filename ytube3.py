import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]



api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secrets.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

{
  "snippet": {
    "videoId": "eMhF2X8TXDo",
    "textDisplay": "very nice"
  }
}

request = youtube.comments().insert(
    body={
        "snippet": {
    "videoId": "eMhF2X8TXDo",
    "textDisplay": "very nice"
  }
    }
)
response = request.execute()

print(response)