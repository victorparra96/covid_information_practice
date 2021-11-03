import logging

from fastapi import FastAPI
from core.exceptions import SettingNotFound
from core.init_app import init_middlewares, register_exceptions

from db import init_db

try:
    from settings.config import settings
except ImportError:
    raise SettingNotFound('Can not import settings. Create settings file from config.py')


app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION
)

log = logging.getLogger(__name__)
init_middlewares(app)
init_db(app)
register_exceptions(app)
#register_routers(app)