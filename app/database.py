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


def init_db(config_name=None):
    engine = get_engine(config_name)
    Base.metadata.create_all(bind=engine)


def drop_db(config_name=None):
    engine = get_engine(config_name)
    Base.metadata.drop_all(bind=engine)


def import_basedata_states(config_name=None):
    pass


# def import_basedata_partiesconfig_name=None():
#     pass
#
#
# def import_basedata_nonparties(config_name=None):
#     pass
#
#
# def import_basedata_reds(config_name=None):
#     pass
#
#
# def import_basedata_districts(config_name=None):
#     pass
#
#
# def import_basedata_municipalities(config_name=None):
#     pass
#
#
# def import_result(config_name=None):
#     pass
#
#
# def import_basedata_lists(config_name=None):
#     pass
