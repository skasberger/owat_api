# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from app import create_app
from typing import Optional
import os

app = create_app(os.getenv("FASTAPI_CONFIG") or "default")
