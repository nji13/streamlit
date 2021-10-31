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

items_id = []
items = response['items']
for item in items:
    item_id = {}
    item_id['video_id'] = item['id']['videoId']
    item_id['channel_id'] = item['snippet']['channelId']
    items_id.append(item_id)

df_video = pd.DataFrame(items_id)

print(df_video)