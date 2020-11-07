# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from app import create_app
from app.config import get_config_name
from typing import Optional
import os

app = create_app(get_config_name())
