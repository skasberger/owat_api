# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter
from app import crud
from app.schemas import PartyVote, NonPartyVote
from app.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter()
