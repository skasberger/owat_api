# !/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_all, get_first
from app.database import get_db
from app.models import State as state_model


router = APIRouter()


@router.get("/", tags=["states"])
def get_states(db: Session = Depends(get_db)):
    return get_all(db=db, model=state_model)


@router.get("/{state_id}", tags=["states"])
def get_state(state_id: int, db: Session = Depends(get_db)):
    return get_first(db=db, model=state_model, kwargs={"state_id": state_id})
