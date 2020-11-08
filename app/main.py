# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""main"""
from fastapi import FastAPI
import os
from .config import config, get_config_name
from . import __description__


def create_app(config_name="default"):
    """Create application and load settings."""
    print("* Start Offene Wahlen AT API...")

    SQLALCHEMY_DATABASE_URI = config[config_name].SQLALCHEMY_DATABASE_URI
    DEBUG = config[config_name].DEBUG
    API_PREFIX = config[config_name].API_PREFIX
    SECRET_KEY = config[config_name].SECRET_KEY
    TITLE = config[config_name].TITLE

    app = FastAPI(title=TITLE, debug=DEBUG, description=__description__)

    print(' * Settings "{0}": Loaded'.format(config_name))
    print(" * Database: " + SQLALCHEMY_DATABASE_URI)

    from app.routers import router as api_router

    app.include_router(api_router, prefix=API_PREFIX)

    return app
