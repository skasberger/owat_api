# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import models, crud, schemas
import os
from .config import config

FASTAPI_CONFIG = os.getenv("FASTAPI_CONFIG") or "default"
SQLALCHEMY_DATABASE_URI = config[FASTAPI_CONFIG].SQLALCHEMY_DATABASE_URI
engine = create_engine("postgresql://localhost/owat_dev")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = get_db()
