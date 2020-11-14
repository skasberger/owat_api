# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter

from app.api.v1.elections import router as elections_router
from app.api.v1.parties import router as parties_router
from app.api.v1.states import router as states_router
from app.api.v1.regionalelectoraldistricts import (
    router as regionalelectoraldistricts_router,
)
from app.api.v1.districts import router as districts_router
from app.api.v1.municipalities import router as municipalities_router


router = APIRouter()
router.include_router(elections_router, prefix="/elections", tags=["elections"])
router.include_router(parties_router, prefix="/parties", tags=["parties"])
router.include_router(districts_router, prefix="/districts", tags=["districts"])
router.include_router(
    municipalities_router, prefix="/municipalities", tags=["municipalities"]
)
router.include_router(states_router, prefix="/states", tags=["states"])
router.include_router(
    regionalelectoraldistricts_router,
    prefix="/regionalelectoraldistricts",
    tags=["regionalelectoraldistricts"],
)


@router.get("/")
def get_root():
    return [
        {"path": "elections/", "name": "elections"},
        {"path": "parties/", "name": "parties"},
        {"path": "states/", "name": "states"},
        {"path": "regionalelectoraldistricts/", "name": "regionalelectoraldistricts"},
        {"path": "districts/", "name": "districts"},
        {"path": "municipalities/", "name": "municipalities"},
    ]
