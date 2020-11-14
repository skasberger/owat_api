# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test API."""


api_root = [
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
api_v1 = [
    {"path": "elections/", "name": "elections"},
    {"path": "parties/", "name": "parties"},
    {"path": "states/", "name": "states"},
    {"path": "regionalelectoraldistricts/", "name": "regionalelectoraldistricts"},
    {"path": "districts/", "name": "districts"},
    {"path": "municipalities/", "name": "municipalities"},
]


def test_app_root(client):
    """Start with a blank database."""

    resp = client.get("/")
    assert 404 == resp.status_code


def test_api_root(client):
    """Start with a blank database."""

    resp = client.get("/api/")
    assert 200 == resp.status_code
    assert resp.json() == api_root


def test_api_v1(client):
    """Start with a blank database."""

    resp = client.get("/api/v1/")
    assert 200 == resp.status_code
    assert resp.json() == api_v1


def test_docs_root(client):
    """Start with a blank database."""

    resp = client.get("/docs/")
    assert 200 == resp.status_code


def test_redoc_root(client):
    """Start with a blank database."""

    resp = client.get("/redoc/")
    assert 200 == resp.status_code
