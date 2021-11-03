from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise

from settings.config import settings


TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.DB_URL,
        modules={"models": ["models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


Tortoise.init_models(["models"], 'models')