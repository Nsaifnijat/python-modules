# -*- coding: utf-8 -*-

from googleapiclient.discovery import build




api_key = 'AIzaSyAjm6Tt5GZrrnFDCu0rGtkdzTX6YkdIAzY'


youtube = build('youtube','v3', developerKey=api_key)
'''
request = youtube.channels().list(
    part='contentDetails',
    forUsername='MrBeast6000'
    
    )

response = request.execute()

print(response)

'''
request = youtube.playlistItems().list(
    part='snippet',playlistId='UUX6OQ3DkcsbYNE6H8uQQuVA')

response = request.execute()
for i in response['items']:
    print(i['snippet']['title'])
    print(i['snippet']['resourceId']['videoId'])
    print('888888888888888888888888888888888')
    break
#print(response['items'])
'''
latest video:
100,000,000 Subscriber Special
dZklZVaU4AI

100 Girls Vs 100 Boys For $500,000
tVWWp1PqDus




request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id="Ks-_Mh1QhMc"
    )
response = request.execute()

print(response)
'''
