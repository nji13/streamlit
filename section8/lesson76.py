from apiclient.discovery import build
# from apiclient.errors import HttpError
# from oauth2client.tools import argparser
import json
import pandas as pd

with open('secret.json') as f:
    secret = json.load(f)

DEVELOPER_KEY = secret['KEY']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# def youtube_search(options):
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

q = 'Python 自動化'
max_results = 30

response = youtube.search().list(
    q=q,
    part="id,snippet",
    order="viewCount",
    type='video',
    maxResults=max_results
).execute()

items = response['items']
item = items[0]

print(item)