import pandas as pd

def transform_comments(json_data):
    df = pd.DataFrame(json_data)
    df['text'] = df['text'].str.replace(r'[^A-Za-z0-9 ]+', '', regex=True)
    df['text'] = df['text'].str.strip().str.lower()
    df['published_at'] = pd.to_datetime(df['published_at'])
    return df
