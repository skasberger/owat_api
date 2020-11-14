# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""main"""
from dotenv import load_dotenv
from fastapi import FastAPI
import os

from app import __description__
from app.config import get_config, get_config_name
from app.api import router as api_router


def create_app(config_name=None):
    """Create application and load settings."""
    print("* Start Offene Wahlen AT API...")

    if config_name is None:
        load_dotenv()
        config_name = get_config_name()

    config = get_config(config_name)
    SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
    TITLE = config.TITLE
    DEBUG = config.DEBUG

    app = FastAPI(
        title=TITLE,
        debug=DEBUG,
        description=__description__,
        flask_config=config_name,
        **config.dict(),
    )
    app.include_router(api_router, prefix="/api")

    print(' * Setting "{0}" loaded'.format(config_name))
    print(" * Database: {0}".format(SQLALCHEMY_DATABASE_URI))

    return app
