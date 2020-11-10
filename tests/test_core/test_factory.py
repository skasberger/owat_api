# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test factory."""
from fastapi import FastAPI
import os
import pytest

from app.config import get_config
from app.database import get_engine, get_SessionLocal
from app.main import create_app


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def test_config_development():
    for config_name in ["default", "development"]:
        app = create_app(config_name)
        config = get_config(config_name)

        assert config.SQLALCHEMY_DATABASE_URI == "postgresql://localhost/owat_dev"
        assert config.API_PREFIX == "/api"
        assert config.DEBUG == True
        assert config.SECRET_KEY == "my-secret-key"
        assert config.ADMIN_EMAIL is None
        assert config.APP_EMAIL is None
        assert config.TRAVIS == False
        assert config.MIN_CONNECTIONS_COUNT is None
        assert config.MAX_CONNECTIONS_COUNT is None
        assert config.TITLE == "owat_api"
        assert isinstance(app, FastAPI)


def test_config_testing():
    config_name = "testing"
    app = create_app(config_name)
    config = get_config(config_name)

    if os.getenv("TRAVIS") or False:
        assert config.TRAVIS == True
    else:
        assert config.TRAVIS == False
    assert config.SQLALCHEMY_DATABASE_URI == "postgresql://localhost/owat_test"
    assert config.API_PREFIX == "/api"
    assert config.DEBUG == False
    assert config.SECRET_KEY == "secret-env-key"
    assert config.ADMIN_EMAIL == "testing_admin@offenewahlen.at"
    assert config.APP_EMAIL == "testing_app@offenewahlen.at"
    assert config.MIN_CONNECTIONS_COUNT == 10
    assert config.MAX_CONNECTIONS_COUNT == 10
    assert config.TITLE == "owat_api"
    assert isinstance(app, FastAPI)


def test_config_travis():
    config_name = "travis"
    app = create_app(config_name)
    config = get_config(config_name)

    assert config.TRAVIS == True
    assert (
        config.SQLALCHEMY_DATABASE_URI
        == "postgresql+psycopg2://postgres@localhost:5432/travis_ci_test"
    )
    assert config.API_PREFIX == "/api"
    assert config.DEBUG == False
    assert config.SECRET_KEY == "my-secret-key"
    assert config.ADMIN_EMAIL is None
    assert config.APP_EMAIL is None
    assert config.MIN_CONNECTIONS_COUNT is None
    assert config.MAX_CONNECTIONS_COUNT is None
    assert config.TITLE == "owat_api"
    assert isinstance(app, FastAPI)


def test_config_production():
    config_name = "production"
    app = create_app(config_name)
    config = get_config(config_name)

    if os.getenv("TRAVIS") or False:
        assert config.TRAVIS == True
    else:
        assert config.TRAVIS == False
    assert config.SQLALCHEMY_DATABASE_URI == "postgresql://localhost/owat"
    assert config.API_PREFIX == "/api"
    assert config.DEBUG == False
    assert config.SECRET_KEY == "my-secret-key"
    assert config.ADMIN_EMAIL is None
    assert config.APP_EMAIL is None
    assert config.MIN_CONNECTIONS_COUNT is None
    assert config.MAX_CONNECTIONS_COUNT is None
    assert config.TITLE == "owat_api"
    assert isinstance(app, FastAPI)
