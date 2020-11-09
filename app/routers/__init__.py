# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from fastapi import APIRouter

# import app.routers.districts
import app.routers.elections

# import app.routers.municipalities
import app.routers.parties

# import app.routers.states
# import app.routers.votes

router = APIRouter()
# router.include_router(districts.router, prefix="/districts", tags=["districts"])
router.include_router(elections.router, prefix="/elections", tags=["elections"])
# router.include_router(
#     municipalities.router, prefix="/municipalities", tags=["municipalities"]
# )
router.include_router(parties.router, prefix="/parties", tags=["parties"])
# router.include_router(states.router, prefix="/states", tags=["states"])
# router.include_router(votes.router, prefix="/votes", tags=["votes"])


@router.get("/")
def get_root():
    return {"version": "1.0", "status": "OK", "name": "owat_api"}
