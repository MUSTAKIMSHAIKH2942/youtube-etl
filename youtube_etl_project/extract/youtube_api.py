from googleapiclient.discovery import build
import json
import os

def extract_comments(api_key, video_id, max_results=100):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=max_results,
        textFormat='plainText'
    )
    response = request.execute()

    comments = []
    for item in response.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append({
            'author': comment['authorDisplayName'],
            'text': comment['textDisplay'],
            'published_at': comment['publishedAt']
        })

    os.makedirs("data/raw", exist_ok=True)
    with open(f'data/raw/comments_{video_id}.json', 'w') as f:
        json.dump(comments, f, indent=4)
    
    return comments
