# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test api/districts/."""


def test_districts_root(client):
    """Start with a blank database."""

    resp = client.get("/api/v1/districts/")
    assert 200 == resp.status_code
