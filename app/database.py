# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Database"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_config_name, config
from app.models import Base


def get_engine(config_name=None):
    if config_name is None:
        config_name = get_config_name()
    SQLALCHEMY_DATABASE_URI = config[config_name].SQLALCHEMY_DATABASE_URI
    return create_engine(SQLALCHEMY_DATABASE_URI)


def get_SessionLocal():
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal


def get_db():
    SessionLocal = get_SessionLocal()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)


def drop_db():
    engine = get_engine()
    Base.metadata.drop_all(bind=engine)


def import_basedata_states():
    pass


# def import_basedata_parties():
#     pass
#
#
# def import_basedata_nonparties():
#     pass
#
#
# def import_basedata_reds():
#     pass
#
#
# def import_basedata_districts():
#     pass
#
#
# def import_basedata_municipalities():
#     pass
#
#
# def import_result():
#     pass
#
#
# def import_basedata_lists():
#     pass
