import json
from extract.youtube_api import extract_comments
from transform.clean_comments import transform_comments
from load.save_to_sqlite import load_to_db

API_KEY = 'YOUR_YOUTUBE_API_KEY'
VIDEO_ID = 'VIDEO_ID_HERE'

def main():
    print("[INFO] Starting ETL Pipeline...")
    raw_comments = extract_comments(API_KEY, VIDEO_ID)
    
    print("[INFO] Transforming comments...")
    df = transform_comments(raw_comments)
    
    print("[INFO] Loading to database...")
    load_to_db(df)
    print("[SUCCESS] ETL completed!")

if __name__ == '__main__':
    main()
