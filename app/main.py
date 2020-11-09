# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""main"""
from dotenv import load_dotenv
from fastapi import FastAPI
import os

from app import __description__
from app.config import config, get_config_name
from app.routers import router as api_router


def create_app(config_name=None):
    """Create application and load settings."""
    print("* Start Offene Wahlen AT API...")

    if config_name is None:
        config_name = get_config_name()

    load_dotenv()

    SQLALCHEMY_DATABASE_URI = config[config_name].SQLALCHEMY_DATABASE_URI
    DEBUG = config[config_name].DEBUG
    API_PREFIX = config[config_name].API_PREFIX
    SECRET_KEY = config[config_name].SECRET_KEY
    TITLE = config[config_name].TITLE

    app = FastAPI(title=TITLE, debug=DEBUG, description=__description__)
    app.include_router(api_router, prefix=API_PREFIX)

    print(' * Settings "{0}": Loaded'.format(config_name))
    print(" * Database: " + SQLALCHEMY_DATABASE_URI)

    return app
