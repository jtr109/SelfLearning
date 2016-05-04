# !/usr/bin/env python
# -*- coding: utf-8 -*-


def safe_raw_input(text):
    try:
        return raw_input(text)
    except (EOFError, KeyboardInterrupt):
        return None

