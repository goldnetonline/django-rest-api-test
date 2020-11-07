'''
File: logging.py
Project: token-credit-backend
File Created: Tuesday, 27th October 2020 11:40:05 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 2nd November 2020 1:54:39 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from typing import (
    Any
)
from logging import getLogger
from .helper import config

IDENTIFIER = config('APP_IDENTIFIER', 'token_credit')


class Logger:
    """
    System Logging factory
    """

    name = None

    def __init__(self) -> None:
        self.name = IDENTIFIER

    def emit_logger(self, msg: Any, name: str = None, *args, **kwargs) -> None:

        level = self.name if not name else f"{self.name}.{name}"
        getattr(getLogger(level), name if name else 'info')(
            msg, *args, **kwargs)

    def error(self, msg: Any, *args, **kwargs) -> None:
        return self.emit_logger(msg, 'error', *args, **kwargs)

    def debug(self, msg: Any, *args, **kwargs) -> None:
        return self.emit_logger(msg, 'debug', *args, **kwargs)

    def warning(self, msg: Any, *args, **kwargs) -> None:
        return self.emit_logger(msg, 'warning', *args, **kwargs)

    def critical(self, msg: Any, *args, **kwargs) -> None:
        return self.emit_logger(msg, 'critical', *args, **kwargs)

    def info(self, msg: Any, *args, **kwargs) -> None:
        return self.emit_logger(msg, 'info', *args, **kwargs)

    def exception(self, msg: Any, *args, **kwargs) -> None:
        return self.error(msg, *args, **kwargs)


logger = Logger()

__all__ = [
    "logger"
]
