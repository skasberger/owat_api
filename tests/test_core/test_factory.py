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

        if os.getenv("TRAVIS") or False:
            assert config.TRAVIS == True
            assert app.__dict__["extra"]["TRAVIS"] == True
        else:
            assert config.TRAVIS == False
            assert app.__dict__["extra"]["TRAVIS"] == False
        assert config.SQLALCHEMY_DATABASE_URI == "postgresql://localhost/owat_dev"
        assert (
            app.__dict__["extra"]["SQLALCHEMY_DATABASE_URI"]
            == "postgresql://localhost/owat_dev"
        )
        assert config.API_PREFIX == "/api"
        assert app.__dict__["extra"]["API_PREFIX"] == "/api"
        assert config.DEBUG == True
        assert app.__dict__["extra"]["DEBUG"] == True
        assert app._debug == True
        assert config.SECRET_KEY == "my-secret-key"
        assert app.__dict__["extra"]["SECRET_KEY"] == "my-secret-key"
        assert config.ADMIN_EMAIL is None
        assert app.__dict__["extra"]["ADMIN_EMAIL"] is None
        assert config.APP_EMAIL is None
        assert app.__dict__["extra"]["APP_EMAIL"] is None
        assert config.MIN_CONNECTIONS_COUNT is None
        assert app.__dict__["extra"]["MIN_CONNECTIONS_COUNT"] is None
        assert config.MAX_CONNECTIONS_COUNT is None
        assert app.__dict__["extra"]["MAX_CONNECTIONS_COUNT"] is None
        assert config.TITLE == "owat_api"
        assert app.title == "owat_api"
        assert app.__dict__["extra"]["TITLE"] == "owat_api"
        assert app.version == "0.1.0"
        assert app.description == "RESTful API for Austrian open elections data"
        assert isinstance(app, FastAPI)


def test_config_testing():
    config_name = "testing"
    app = create_app(config_name)
    config = get_config(config_name)

    if os.getenv("TRAVIS") or False:
        assert config.TRAVIS == True
        assert app.__dict__["extra"]["TRAVIS"] == True
    else:
        assert config.TRAVIS == False
        assert app.__dict__["extra"]["TRAVIS"] == False
    assert config.SQLALCHEMY_DATABASE_URI == "postgresql://localhost/owat_test"
    assert (
        app.__dict__["extra"]["SQLALCHEMY_DATABASE_URI"]
        == "postgresql://localhost/owat_test"
    )
    assert config.API_PREFIX == "/api"
    assert app.__dict__["extra"]["API_PREFIX"] == "/api"
    assert config.DEBUG == False
    assert app.debug == False
    assert app.__dict__["extra"]["DEBUG"] == False
    assert config.SECRET_KEY == "secret-env-key"
    assert app.__dict__["extra"]["SECRET_KEY"] == "secret-env-key"
    assert config.ADMIN_EMAIL == "testing_admin@offenewahlen.at"
    assert app.__dict__["extra"]["ADMIN_EMAIL"] == "testing_admin@offenewahlen.at"
    assert config.APP_EMAIL == "testing_app@offenewahlen.at"
    assert app.__dict__["extra"]["APP_EMAIL"] == "testing_app@offenewahlen.at"
    assert config.MIN_CONNECTIONS_COUNT == 10
    assert app.__dict__["extra"]["MIN_CONNECTIONS_COUNT"] == 10
    assert config.MAX_CONNECTIONS_COUNT == 10
    assert app.__dict__["extra"]["MAX_CONNECTIONS_COUNT"] == 10
    assert config.TITLE == "owat_api"
    assert app.title == "owat_api"
    assert app.__dict__["extra"]["TITLE"] == "owat_api"
    assert app.version == "0.1.0"
    assert app.description == "RESTful API for Austrian open elections data"
    assert isinstance(app, FastAPI)


def test_config_travis():
    config_name = "travis"
    app = create_app(config_name)
    config = get_config(config_name)

    assert config.TRAVIS == True
    assert app.__dict__["extra"]["TRAVIS"] == True
    assert (
        config.SQLALCHEMY_DATABASE_URI
        == "postgresql+psycopg2://postgres@localhost:5432/travis_ci_test"
    )
    assert (
        app.__dict__["extra"]["SQLALCHEMY_DATABASE_URI"]
        == "postgresql+psycopg2://postgres@localhost:5432/travis_ci_test"
    )
    assert config.API_PREFIX == "/api"
    assert app.__dict__["extra"]["API_PREFIX"] == "/api"
    assert config.DEBUG == False
    assert app.__dict__["extra"]["DEBUG"] == False
    assert app._debug == False
    assert config.SECRET_KEY == "my-secret-key"
    assert app.__dict__["extra"]["SECRET_KEY"] == "my-secret-key"
    assert config.ADMIN_EMAIL is None
    assert app.__dict__["extra"]["ADMIN_EMAIL"] is None
    assert config.APP_EMAIL is None
    assert app.__dict__["extra"]["APP_EMAIL"] is None
    assert config.MIN_CONNECTIONS_COUNT is None
    assert app.__dict__["extra"]["MIN_CONNECTIONS_COUNT"] is None
    assert config.MAX_CONNECTIONS_COUNT is None
    assert app.__dict__["extra"]["MAX_CONNECTIONS_COUNT"] is None
    assert config.TITLE == "owat_api"
    assert app.title == "owat_api"
    assert app.__dict__["extra"]["TITLE"] == "owat_api"
    assert app.version == "0.1.0"
    assert app.description == "RESTful API for Austrian open elections data"
    assert isinstance(app, FastAPI)


def test_config_production():
    config_name = "production"
    app = create_app(config_name)
    config = get_config(config_name)

    if os.getenv("TRAVIS") or False:
        assert config.TRAVIS == True
        assert app.__dict__["extra"]["TRAVIS"] == True
    else:
        assert config.TRAVIS == False
        assert app.__dict__["extra"]["TRAVIS"] == False
    assert config.SQLALCHEMY_DATABASE_URI == "postgresql://localhost/owat"
    assert (
        app.__dict__["extra"]["SQLALCHEMY_DATABASE_URI"]
        == "postgresql://localhost/owat"
    )
    assert config.API_PREFIX == "/api"
    assert app.__dict__["extra"]["API_PREFIX"] == "/api"
    assert config.DEBUG == False
    assert app.debug == False
    assert app.__dict__["extra"]["DEBUG"] == False
    assert config.SECRET_KEY == "my-secret-key"
    assert app.__dict__["extra"]["SECRET_KEY"] == "my-secret-key"
    assert config.ADMIN_EMAIL is None
    assert app.__dict__["extra"]["ADMIN_EMAIL"] is None
    assert config.APP_EMAIL is None
    assert app.__dict__["extra"]["APP_EMAIL"] is None
    assert config.MIN_CONNECTIONS_COUNT is None
    assert app.__dict__["extra"]["MIN_CONNECTIONS_COUNT"] is None
    assert config.MAX_CONNECTIONS_COUNT is None
    assert app.__dict__["extra"]["MAX_CONNECTIONS_COUNT"] is None
    assert app.title == "owat_api"
    assert app.__dict__["extra"]["TITLE"] == "owat_api"
    assert app.version == "0.1.0"
    assert app.description == "RESTful API for Austrian open elections data"
    assert isinstance(app, FastAPI)
