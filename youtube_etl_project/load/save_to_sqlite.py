from sqlalchemy import create_engine

def load_to_db(df, db_name='youtube_comments.db'):
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql('comments', engine, if_exists='replace', index=False)
