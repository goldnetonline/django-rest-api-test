'''
File: logging.py
Project: token-credit-backend
File Created: Tuesday, 27th October 2020 11:40:05 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Thursday, 29th October 2020 1:13:01 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from logging import getLogger
from .helper import config
from typing import (
    Any
)

idenfifier = config('APP_IDENTIFIER', 'token_credit')


class Logger:

    name = None

    def __init__(self) -> None:
        self.name = idenfifier

    def emit_logger(self, msg: Any, name: str = None, * args, **kwargs) -> None:

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
    logger
]
