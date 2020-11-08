# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test api/parties/."""


def test_parties_root(client):
    """Start with a blank database."""

    resp = client.get("/api/parties/")
    assert 200 == resp.status_code
