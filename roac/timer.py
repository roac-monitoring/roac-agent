# vim: set fileencoding=utf-8 :
from __future__ import division, print_function, unicode_literals
from collections import namedtuple
import time


Callback = namedtuple('Callback', ['function', 'args', 'kwargs'])


class RepeatingTimer:
    """Calls a set of functions in regular intervals"""

    def __init__(self, interval):
        self.interval = interval
        self.callbacks = []

    def register(self, f, *args, **kwargs):
        """Adds a function to be called each interval"""
        self.callbacks.append(Callback(f, args, kwargs))

    def run(self):
        """Gets the timer running"""
        self.running = True
        while self.running:
            now = time.time()
            for callback in self.callbacks:
                callback.function(*callback.args, **callback.kwargs)
            time.sleep(self.interval - (time.time() - now))
