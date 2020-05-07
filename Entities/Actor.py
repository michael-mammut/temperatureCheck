#!/usr/bin/env python3
from datetime import datetime


class Actor:
    def __init__(self, gpio, on: datetime, off: datetime):
        self.gpio = gpio
        self.on = on
        self.off = off
