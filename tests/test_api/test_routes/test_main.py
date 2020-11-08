# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test API."""


def test_app_root(client):
    """Start with a blank database."""

    resp = client.get("/")
    assert 404 == resp.status_code


def test_api_root(client):
    """Start with a blank database."""

    resp = client.get("/api/")
    assert 200 == resp.status_code
    assert resp.json() == {"version": "1.0", "status": "OK", "name": "owat_api"}
