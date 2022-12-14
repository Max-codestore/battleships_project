# (c) "Shiromi" 2020
# Python debugger

from typing import Dict
from enum import Enum
from datetime import datetime as dt


class Formatter(Enum):
    LOG = 'log',
    ERROR = 'error',
    FUNCTION = 'function',
    VARIABLE = 'variable',
    DEBUG = 'debug',
    PROGRAM = 'result'


def variable(name: str, value: any) -> None:
    print("[VARIABLE]: %s = %s" % (name, value))


def function(name: str, args: Dict[str, any]) -> None:
    _args = ''

    for name, val in args.items():
        _args += "%s: %s," % (name, val)

    _args = _args[:len(_args) - 1]

    print("[FUNCTION]: Executed '%s' with '%s' as arguments." % (name, _args if len(args) > 0 else 'nothing'))


def log(text: str) -> None:
    print("[LOG]: %s" % text)


def format(mode: Formatter, msg: str, time=False) -> str:
    _mode = mode.value if isinstance(mode.value, str) else mode.value[0]
    _now = dt.now()
    _hr = '0%s' % _now.hour if _now.hour < 10 else _now.hour
    _min = '0%s' % _now.minute if _now.minute < 10 else _now.minute
    _sec = '0%s' % _now.second if _now.second < 10 else _now.second
    _time = "%s:%s:%s" % (_hr, _min, _sec)
    _return = _time if time else ''
    _return += '%s[%s]' % (' ' if time else '', _mode.upper())

    return '%s: %s' % (_return, msg)

class Formatted:

    def variable(name: str, value: any) -> None:
        print(format(Formatter.VARIABLE, "'%s' = %s" % (name, value), True))


    def function(_name: str, args: Dict[str, any]) -> None:
        _args = ''

        for name, value in args.items():
            _args += "%s: %s" % (name, value)

        _args = _args[:len(_args) - 1]

        print(format(Formatter.FUNCTION, "Executed '%s' with '%s' as arguments." % (
        _name, _args if len(args) > 0 else 'nothing')))


    def custom(prefix: Formatter, msg: any) -> None:
        print(format(prefix, msg, True))