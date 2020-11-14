# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test api/municipalities/."""


def test_municipalities_root(client):
    """Start with a blank database."""

    resp = client.get("/api/v1/municipalities/")
    assert 200 == resp.status_code
