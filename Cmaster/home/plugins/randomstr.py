# -*- coding: utf-8 -*-
import random
import string
from HCore import uibox


def make_random(s):
    chars = list(s[0])
    for idx, char in enumerate(chars):
        if char not in string.punctuation and not char.isspace():
            chars[idx] = random.choice(string.ascii_letters)
    uibox.Info('成功调起来')
    return ''.join(chars)


def setup(app):
    app.register_formatter('random', make_random)

def build(app):
    pass
