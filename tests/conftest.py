# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""conftest"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
import os
import pytest
from sqlalchemy.orm import sessionmaker

from app.database import init_db, engine, get_db, drop_db
from app.main import create_app
from app.models import Base


TEST_DIR = os.path.dirname(os.path.realpath(__file__))


def override_get_db():
    try:
        TestingSessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=engine
        )
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    if os.getenv("TRAVIS") or False:
        app = create_app("travis")
    else:
        app = create_app("testing")

    # reset the database
    drop_db(Base)
    init_db(Base)

    # override dependencies
    app.dependency_overrides[get_db] = override_get_db

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return TestClient(app)
