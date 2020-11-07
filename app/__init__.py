# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find out more at

Copyright 2020 Stefan Kasberger

Licensed under the MIT License.
"""
from fastapi import FastAPI
from . import models
from .database import init_db

__author__ = "Stefan Kasberger"
__email__ = "mail@stefankasberger.at"
__copyright__ = "Copyright (c) 2020 Stefan Kasberger"
__license__ = "MIT License"
__version__ = "0.0.1"
__url__ = ""
__download_url__ = ""
__description__ = ""


def create_app(config_name="default"):
    """Create application and load settings."""
    print("* Start Offene Wahlen AT API...")

    app = FastAPI(title="owat_api")

    from app.routers import router as api_router

    app.include_router(api_router, prefix="/api")

    # init_db()
    from app.database import Base, engine

    Base.metadata.create_all(bind=engine)

    return app
