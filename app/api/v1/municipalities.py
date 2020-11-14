# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_all, get_first
from app.database import get_db
from app.models import Municipality as municipality_model


router = APIRouter()


@router.get("/", tags=["municipalities"])
def get_municipalities(db: Session = Depends(get_db)):
    return get_all(db=db, model=municipality_model)


@router.get("/{municipality_id}", tags=["municipalities"])
def get_municipality(municipality_id: int, db: Session = Depends(get_db)):
    return get_first(
        db=db, model=municipality_model, kwargs={"municipality_id": municipality_id}
    )
