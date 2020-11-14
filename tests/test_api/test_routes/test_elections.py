# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test API."""


def test_api_root(client):
    """Start with a blank database."""

    resp = client.get("/api/v1/elections/")
    assert 200 == resp.status_code
