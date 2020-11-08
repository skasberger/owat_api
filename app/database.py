# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from . import models, crud, schemas
from .config import get_config_name, config

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


def init_db():
    try:
        # Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        parties = [
            {"id": 1, "name": "SPÖ"},
            {"id": 2, "name": "FPÖ"},
            {"id": 3, "name": "ÖVP"},
            {"id": 4, "name": "Grüne"},
            {"id": 5, "name": "NEOS"},
            {"id": 6, "name": "Links"},
        ]
        for p in parties:
            party = schemas.Party(**p)
            db_party = crud.create_party(db=db, party=party)

        elections = [
            {"id": 1, "acronym": "NRW2019"},
            {"id": 2, "acronym": "NRW2017"},
            {"id": 3, "acronym": "NRW2013"},
            {"id": 4, "acronym": "EUW2019"},
            {"id": 5, "acronym": "EUW2014"},
            {"id": 6, "acronym": "BPW2016"},
            {"id": 7, "acronym": "BPW2010"},
        ]
        for e in elections:
            election = schemas.Election(**e)
            db_election = crud.create_election(db=db, election=election)
    finally:
        db.close()


def drop_db():
    Base.metadata.drop_all(bind=engine)
