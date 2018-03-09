# -*- coding: utf-8 -*-
def make_uppercase(s):
    return s[0].upper()


def setup(app):
    app.register_formatter('01uppercase', make_uppercase)
def build(app):
    pass