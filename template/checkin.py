#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
import sys

sys.path.append(".")
from lib.checkbase import CheckIn


COOKIE = os.environ.get("COOKIE_TEMPLATE")


class SampleCheckIn(CheckIn):
    def _checkin(self, get, post, info, error):
        return 0


if __name__ == "__main__":
    SampleCheckIn("SAMPLE", COOKIE).main()
