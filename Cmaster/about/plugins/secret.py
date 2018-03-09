# -*- coding: utf-8 -*-
import string


def make_secret(s):
    chars = list(s[0])
    for idx, char in enumerate(chars):
        if char not in string.punctuation and not char.isspace():
            chars[idx] = 'x'
    return ''.join(chars)

def myprint(s):
    return 'my  print'

def setup(app):
    app.register_formatter('04secret', make_secret)
    app.register_formatter('03print', myprint)
def build(app):
    pass