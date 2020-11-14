# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_all, get_first
from app.database import get_db
from app.models import RegionalElectoralDistrict as regionalelectoraldistricts_model


router = APIRouter()


@router.get("/", tags=["regionalelectoraldistricts"])
def get_regionalelectoraldistricts(db: Session = Depends(get_db)):
    return get_all(db=db, model=regionalelectoraldistricts_model)


@router.get("/{regionalelectoraldistricts_id}", tags=["regionalelectoraldistricts"])
def get_regionalelectoraldistricts(
    regionalelectoraldistricts_id: int, db: Session = Depends(get_db)
):
    return get_first(
        db=db,
        model=regionalelectoraldistricts_model,
        kwargs={"regionalelectoraldistricts_id": regionalelectoraldistricts_id},
    )
