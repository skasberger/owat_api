# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter

from app.api.v1 import router as v1_router


router = APIRouter()
router.include_router(v1_router, prefix="/v1")


@router.get("/")
def get_root():
    return [
        {
            "path": "/v1",
            "name": "v1",
            "version": "1.0.0",
            "major": 1,
            "minor": 0,
            "micro": 0,
            "path": "/v1",
            "release_date": "2020-11-11",
            "status": "online",
        }
    ]
