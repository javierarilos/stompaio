#!/usr/bin/env python

import asyncore
from client import StompClient

cli = StompClient()
cli.do_con()
asyncore.loop()
