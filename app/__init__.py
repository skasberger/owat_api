# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find out more at

Copyright 2020 Stefan Kasberger

Licensed under the MIT License.
"""
from fastapi import FastAPI
from . import models
from .database import init_db
from .config import config
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

    # init_db()
    from app.database import Base, engine

    Base.metadata.create_all(bind=engine)

    return app
