import os
STIMULI_UPLOAD_PATH = 'static/artworks/'
DB_TYPE = 'postgresql+psycopg2'
POSTGRES_DB = os.getenv('POSTGRES_DB','livegaze')
POSTGRES_HOST = os.getenv('POSTGRES_HOST','localhost')
POSTGRES_USER = os.getenv('POSTGRES_USER','testuser')
POSTGRES_PORT = os.getenv('POSTGRES_PORT',5432)
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD','testPassword')
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL",DB_TYPE+"://"+POSTGRES_USER+":"+POSTGRES_PASSWORD+"@"+POSTGRES_HOST+":"+str(POSTGRES_PORT)+"/"+POSTGRES_DB)
SECRET_KEY=os.getenv("SECRET_KEY","powerful secretkey")
WTF_CSRF_SECRET_KEY=os.getenv("WTF_CSRF_SECRET_KEY","a csrf secret key")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY","EXAMPLE_YOUTUBE_KEY")