import os

class Settings:
    VERSION = '0.0.1'
    APP_TITLE = 'Covid information'
    PROJECT_NAME = 'Covid information for usa'
    APP_DESCRIPTION = 'Show results for covid information'

    DB_URL = 'postgres://{}:{}@web-db:5432/{}'.format(
        os.environ['POSTGRES_USER'],
        os.environ['POSTGRES_PASSWORD'],
        os.environ['POSTGRES_DB']
    )

    CORS_ORIGINS = [
        "http://localhost",
        "http://localhost:8000",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]

settings = Settings()