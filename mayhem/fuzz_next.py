#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from crontab import CronTab

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    str_len = fdp.ConsumeIntInRange(0, 100)
    str_val = fdp.ConsumeUnicodeNoSurrogates(str_len)

    entry = CronTab(str_val)
    entry.next()

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()