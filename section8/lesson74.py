from apiclient.discovery import build
# from apiclient.errors import HttpError
# from oauth2client.tools import argparser
import json

with open('secret.json') as f:
    secret = json.load(f)

DEVELOPER_KEY = secret['KEY']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# def youtube_search(options):
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

q = 'Python'
max_results = 50

response = youtube.search().list(
    q=q,
    part="id,snippet",
    maxResults=max_results
).execute()

print(response)