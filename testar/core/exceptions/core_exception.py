# -*- coding: utf-8 -*-
"""Main Exceptions for testar library"""


from testar.core.loggers.logger_manager import LoggerManager


class CoreException(Exception):
    """Base Exception class for inherit new exceptions on library"""

    log = None
    message = None

    def __init__(self,
                 err=None,
                 message='Exception without message',
                 log=None):
        """Raise an exception from any part of testar package"""
        super(CoreException, self).__init__(err, message)
        self.message = "FAILED {}: message={}".format(
            type(self),
            message)
        if log is None:
            self.log = LoggerManager().logger
        else:
            self.log = log
        if err is not None and isinstance(err, Exception):
            self.log.warning(err.args)
        self.log.error(self.message)
