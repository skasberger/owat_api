# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Election(Base):
    __tablename__ = "elections"

    id = Column(Integer, primary_key=True, index=True)
    acronym = Column(String, unique=False, index=True)
