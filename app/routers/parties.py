# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud
from ..schemas import Party
from ..database import get_db

router = APIRouter()


@router.get("/", tags=["parties"])
def get_parties(db: Session = Depends(get_db)):
    return crud.get_parties(db=db)


@router.get("/{party_id}", tags=["parties"])
def get_party(party_id: int, db: Session = Depends(get_db)):
    return crud.get_party(db=db, party_id=party_id)


@router.post("/", response_model=Party, tags=["parties"])
def create_party(party: Party, db: Session = Depends(get_db)):
    db_party = crud.get_party_by_name(db, name=party.name)
    if db_party:
        raise HTTPException(status_code=400, detail="Party already registered")
    return crud.create_party(db=db, party=party)
