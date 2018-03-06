# -*- coding: utf-8 -*-
def make_lowercase(s):
    return s[0].lower()


def setup(app):
    app.register_formatter('00lowercase', make_lowercase)
