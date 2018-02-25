import string


def make_secret(s):
    chars = list(s)
    for idx, char in enumerate(chars):
        if char not in string.punctuation and not char.isspace():
            chars[idx] = 'x'
    return ''.join(chars)

def myprint(s):
    print('print test --------------======')

def setup(app):
    app.register_formatter('secret', make_secret)
    app.register_formatter('myprint', myprint)
