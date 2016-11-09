#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 week 12"""


import time


class CustomLogger(object):
    """A File Logger"""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Logs a message"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Removes Messages"""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Unable to open logfile.')
            raise IOError
        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError:
                self.log('unable to write logfile')
                handled.append('Error')
                break

        fhandler.close()

        for index in handled[::-1]:
            if handled[::-1] is 'Error':
                pass
            else:
                del self.msgs[index]
