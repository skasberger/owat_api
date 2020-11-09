# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test factory."""
from fastapi import FastAPI
import os
import pytest
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session, sessionmaker

from app.main import create_app
from app.config import config
from app.database import get_engine, get_SessionLocal


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def test_config_development():
    for config_name in ["default", "development"]:
        app = create_app(config_name)
        engine = get_engine()
        SessionLocal = get_SessionLocal()

        assert (
            config[config_name].SQLALCHEMY_DATABASE_URI
            == "postgresql://localhost/owat_dev"
        )
        assert config[config_name].API_PREFIX == "/api"
        assert config[config_name].DEBUG == True
        assert config[config_name].SECRET_KEY == "my-secret-key"
        assert config[config_name].ADMIN_EMAIL is None
        assert config[config_name].APP_EMAIL is None
        assert config[config_name].TRAVIS == False
        assert config[config_name].MIN_CONNECTIONS_COUNT is None
        assert config[config_name].MAX_CONNECTIONS_COUNT is None
        assert config[config_name].TITLE == "owat_api"
        assert isinstance(app, FastAPI)
        assert isinstance(engine, Engine)
        assert isinstance(SessionLocal, sessionmaker)


def test_config_testing():
    config_name = "testing"
    app = create_app(config_name)
    engine = get_engine()
    SessionLocal = get_SessionLocal()

    assert (
        config[config_name].SQLALCHEMY_DATABASE_URI
        == "postgresql://localhost/owat_test"
    )
    assert config[config_name].API_PREFIX == "/api"
    assert config[config_name].DEBUG == False
    assert config[config_name].SECRET_KEY == "my-secret-key"
    assert config[config_name].ADMIN_EMAIL == "testing@offenewahlen.at"
    assert config[config_name].APP_EMAIL == "testing@offenewahlen.at"
    assert config[config_name].TRAVIS == False
    assert config[config_name].MIN_CONNECTIONS_COUNT is None
    assert config[config_name].MAX_CONNECTIONS_COUNT is None
    assert config[config_name].TITLE == "owat_api"
    assert isinstance(app, FastAPI)
    assert isinstance(engine, Engine)
    assert isinstance(SessionLocal, sessionmaker)


def test_config_testing_travis():
    config_name = "travis"
    app = create_app(config_name)
    engine = get_engine()
    SessionLocal = get_SessionLocal()

    assert (
        config[config_name].SQLALCHEMY_DATABASE_URI
        == "postgresql+psycopg2://postgres@localhost:5432/travis_ci_test"
    )
    assert config[config_name].API_PREFIX == "/api"
    assert config[config_name].DEBUG == False
    assert config[config_name].SECRET_KEY == "my-secret-key"
    assert config[config_name].ADMIN_EMAIL == "testing@offenewahlen.at"
    assert config[config_name].APP_EMAIL == "testing@offenewahlen.at"
    assert config[config_name].TRAVIS == True
    assert config[config_name].MIN_CONNECTIONS_COUNT is None
    assert config[config_name].MAX_CONNECTIONS_COUNT is None
    assert config[config_name].TITLE == "owat_api"
    assert isinstance(app, FastAPI)
    assert isinstance(engine, Engine)
    assert isinstance(SessionLocal, sessionmaker)


def test_config_production():
    config_name = "production"
    app = create_app(config_name)
    engine = get_engine()
    SessionLocal = get_SessionLocal()

    assert config[config_name].API_PREFIX == "/api"
    assert config[config_name].DEBUG == False
    assert config[config_name].SECRET_KEY == "my-secret-key"
    assert config[config_name].ADMIN_EMAIL is None
    assert config[config_name].APP_EMAIL is None
    assert config[config_name].TRAVIS == False
    assert config[config_name].MIN_CONNECTIONS_COUNT is None
    assert config[config_name].MAX_CONNECTIONS_COUNT is None
    assert config[config_name].TITLE == "owat_api"
    assert isinstance(app, FastAPI)
    assert config[config_name].SQLALCHEMY_DATABASE_URI == "postgresql://localhost/owat"
    assert isinstance(engine, Engine)
    assert isinstance(SessionLocal, sessionmaker)
