# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_all, get_first
from app.database import get_db
from app.models import Election as election_model


router = APIRouter()


@router.get("/", tags=["elections"])
def get_elections(db: Session = Depends(get_db)):
    return get_all(db=db, model=election_model)


@router.get("/{election_id}", tags=["elections"])
def get_election(election_id: int, db: Session = Depends(get_db)):
    return get_first(db=db, model=election_model, kwargs={"election_id": election_id})
