# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_all, get_first
from app.database import get_db
from app.models import District as district_model


router = APIRouter()


@router.get("/", tags=["districts"])
def get_districts(db: Session = Depends(get_db)):
    return get_all(db=db, model=district_model)


@router.get("/{district_id}", tags=["districts"])
def get_district(district_id: int, db: Session = Depends(get_db)):
    return get_first(db=db, model=district_model, kwargs={"district_id": district_id})
