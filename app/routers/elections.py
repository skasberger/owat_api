# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter
from app import crud
from app.schemas import Election
from app.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", tags=["elections"])
async def get_elections(db: Session = Depends(get_db)):
    return crud.get_elections(db=db)


@router.get("/{election_id}", tags=["elections"])
async def get_election(election_id: int, db: Session = Depends(get_db)):
    return crud.get_election(db=db, election_id=election_id)


@router.post("/", response_model=Election, tags=["elections"])
async def create_election(election: Election, db: Session = Depends(get_db)):
    db_election = crud.get_election_by_acronym(db, acronym=election.acronym)
    if db_election:
        raise HTTPException(status_code=400, detail="Election already registered")
    return crud.create_election(db=db, election=election)
