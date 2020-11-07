# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find out more at

Copyright 2020 Stefan Kasberger

Licensed under the MIT License.
"""
from fastapi import FastAPI
from . import models
from .database import init_db
from config import config
import os

__author__ = "Stefan Kasberger"
__email__ = "mail@stefankasberger.at"
__copyright__ = "Copyright (c) 2020 Stefan Kasberger"
__license__ = "MIT License"
__version__ = "0.0.1"
__url__ = "https://github.com/skasberger/owat_api"
__download_url__ = "https://github.com/skasberger/owat_api"
__description__ = "RESTful API for Austrian open elections data"


def create_app(config_name="default"):
    """Create application and load settings."""
    print("* Start Offene Wahlen AT API...")

    FASTAPI_ENV = os.environ.get("FASTAPI_ENV")
    SQLALCHEMY_DATABASE_URI = config[FASTAPI_ENV].SQLALCHEMY_DATABASE_URI
    DEBUG = config[FASTAPI_ENV].DEBUG
    API_PREFIX = config[FASTAPI_ENV].API_PREFIX
    SECRET_KEY = config[FASTAPI_ENV].SECRET_KEY
    ADMIN_EMAIL = config[FASTAPI_ENV].ADMIN_EMAIL
    APP_EMAIL = config[FASTAPI_ENV].APP_EMAIL
    TRAVIS = config[FASTAPI_ENV].TRAVIS
    MIN_CONNECTIONS_COUNT = config[FASTAPI_ENV].MIN_CONNECTIONS_COUNT
    MAX_CONNECTIONS_COUNT = config[FASTAPI_ENV].MAX_CONNECTIONS_COUNT

    app = FastAPI(title="owat_api", debug=DEBUG)

    from app.routers import router as api_router

    app.include_router(api_router, prefix=API_PREFIX)

    # init_db()
    from app.database import Base, engine

    Base.metadata.create_all(bind=engine)

    return app
