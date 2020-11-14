# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test /api/states/."""


def test_states_root(client):
    """Start with a blank database."""

    resp = client.get("/api/v1/states/")
    assert 200 == resp.status_code
