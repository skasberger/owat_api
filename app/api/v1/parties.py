# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_all, get_first
from app.database import get_db
from app.models import Party as party_model


router = APIRouter()


@router.get("/", tags=["parties"])
def get_parties(db: Session = Depends(get_db)):
    return get_all(db=db, model=party_model)


@router.get("/{party_id}", tags=["parties"])
def get_party(party_id: int, db: Session = Depends(get_db)):
    return get_first(db=db, model=party_model, kwargs={"party_id": party_id})
