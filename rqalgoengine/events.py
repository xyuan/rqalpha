# -*- coding: utf-8 -*-

import datetime

import pytz
from enum import Enum

from .const import EVENT_TYPE


class SimulatorAStockTradingEventSource(object):
    def __init__(self, trading_env):
        self.trading_env = trading_env
        self.timezone = trading_env.timezone
        self.generator = self.create_generator()

    def create_generator(self):
        for date in self.trading_env.trading_calendar:
            yield date.replace(hour=9, minute=0, tzinfo=self.timezone), EVENT_TYPE.DAY_START
            yield date.replace(hour=15, minute=0, tzinfo=self.timezone), EVENT_TYPE.HANDLE_BAR
            yield date.replace(hour=16, minute=0, tzinfo=self.timezone), EVENT_TYPE.DAY_END

    def __iter__(self):
        return self

    def __next__(self):
        for date, event in self.generator:
            return date, event

        raise StopIteration

    next = __next__  # Python 2
