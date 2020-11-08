# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Database"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import get_config_name, config


SQLALCHEMY_DATABASE_URI = config[get_config_name()].SQLALCHEMY_DATABASE_URI
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db(Base):
    Base.metadata.create_all(bind=engine)


def drop_db(Base):
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
