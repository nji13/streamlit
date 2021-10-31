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

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


def video_search(youtube, q='自動化', max_results=50):

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
    return df_video

df_video = video_search(youtube, q='python 自動化', max_results=50)

channel_ids = df_video['channel_id'].unique().tolist()  # uniqueで重複idを非表示にしている
# print(channel_ids)

subscriber_list = youtube.channels().list(
    id=','.join(channel_ids),
    part='statistics',
    fields='items(id, statistics(subscriberCount))'
).execute()

subscribers = []
for item in subscriber_list['items']:
    subscriber = {}
    subscriber['channel_id'] = item['id']
    subscriber['subscriber_count'] = int(item['statistics']['subscriberCount'])
    subscribers.append(subscriber)

df_subscribers = pd.DataFrame(subscribers)

df = pd.merge(left=df_video, right=df_subscribers, on='channel_id')

df_extracted = df[df['subscriber_count'] < 5000]

print(df_extracted)