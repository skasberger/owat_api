# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from sqlalchemy.orm import Session
from app import schemas, models


def get_elections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Election).offset(skip).limit(limit).all()


def get_election(db: Session, election_id: int):
    return db.query(models.Election).filter(models.Election.id == election_id).first()


def get_election_by_acronym(db: Session, acronym: str):
    return db.query(models.Election).filter(models.Election.acronym == acronym).first()


def create_election(db: Session, election: schemas.Election):
    db_election = models.Election(**election.dict())
    db.add(db_election)
    db.commit()
    db.refresh(db_election)
    return db_election


def get_parties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Party).offset(skip).limit(limit).all()


def get_party(db: Session, party_id: int):
    return db.query(models.Party).filter(models.Party.id == party_id).first()


def get_party_by_name(db: Session, name: str):
    return db.query(models.Party).filter(models.Party.name == name).first()


def create_party(db: Session, party: schemas.Party):
    db_party = models.Party(**party.dict())
    db.add(db_party)
    db.commit()
    db.refresh(db_party)
    return db_party
