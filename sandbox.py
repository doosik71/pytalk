# -*- coding: utf-8 -*-


class Sandbox:
    """Sandbox class."""

    def __init__(self):
        self.name = 'sandbox'

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


def hello():
    """Hello function."""
    print('Hello, PyTalk!')
