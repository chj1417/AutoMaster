import random
import string

from PyQt5.QtWidgets import QMessageBox

def Info(mess):
    QMessageBox.information(None, ("Infomation"), mess, QMessageBox.StandardButton(QMessageBox.Ok))

def make_random(s):
    chars = list(s)
    for idx, char in enumerate(chars):
        if char not in string.punctuation and not char.isspace():
            chars[idx] = random.choice(string.ascii_letters)
    Info('成功调起来')
    return ''.join(chars)


def setup(app):
    app.register_formatter('random', make_random)
