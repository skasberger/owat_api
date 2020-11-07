# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from pydantic import BaseModel


class District(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Election(BaseModel):
    id: int
    acronym: str

    class Config:
        orm_mode = True


class Municipality(BaseModel):
    id: int
    name: str
    gemeindekennzahl: str
    district: int

    class Config:
        orm_mode = True


class NonPartyVote(BaseModel):
    id: int
    count: int
    municipality: int
    type: str
    election: int

    class Config:
        orm_mode = True


class Party(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class PartyVote(BaseModel):
    id: int
    count: int
    municipality: int
    party: int
    election: int

    class Config:
        orm_mode = True


class State(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
