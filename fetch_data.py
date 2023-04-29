import csv
import googleapiclient.discovery as api

# Set up the API client
youtube = api.build('youtube', 'v3', developerKey='Your_API_Key')

# Get the channel ID for Dhruv Rathee's channel
channel_response = youtube.channels().list(
    part='snippet,contentDetails,statistics',
    forUsername='DhruvRathee',
).execute()
channel_id = channel_response['items'][0]['id']

# Use the channel ID to get the IDs of all videos on the channel
video_ids = []
next_page_token = None
while True:
    videos_response = youtube.search().list(
        part='id',
        channelId=channel_id,
        maxResults=50,
        order='date',
        pageToken=next_page_token,
        type='video',
    ).execute()
    for item in videos_response['items']:
        video_ids.append(item['id']['videoId'])
    next_page_token = videos_response.get('nextPageToken')
    if not next_page_token:
        break

# Use the video IDs to get the details for each video and save to csv file
with open('dhruv_rathee_videos.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Title', 'Description', 'Views', 'Likes']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for video_id in video_ids:
        video_response = youtube.videos().list(
            part='snippet,statistics',
            id=video_id,
        ).execute()
        video = video_response['items'][0]
        title = video['snippet']['title']
        description = video['snippet']['description']
        views = video['statistics']['viewCount']
        likes = video['statistics']['likeCount']
        writer.writerow({'Title': title, 'Description': description, 'Views': views, 'Likes': likes})
