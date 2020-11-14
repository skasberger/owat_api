# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from sqlalchemy.orm import Session
from app import models


def get_all(db: Session, model: models.Election, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()


def get_first(db: Session, model: models.District, kwargs: dict):
    return db.query(model).filter_by(**kwargs).first()


def create_entity(db: Session, model: models.Election, kwargs: dict):
    db_entity = model(**kwargs)
    db_entity.save(db)
    return db_entity


def create_entities(db: Session, model: models.Election, iterable: list, kwargs: dict):
    db_entities = model.bulk_create(db, iterable, **kwargs)
    db.commit()
    return db_entities
