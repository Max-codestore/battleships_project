# (c) "Shiromi", max 2020
# Python debugger

from enum import Enum
from datetime import datetime as dt


class Mode(Enum):
    LOG = 0x0
    ERROR = 0x82


def _format_(mode: Mode, msg: str, time=False) -> str:
    _mode = mode.value if isinstance(mode.value, int) else 0x0
    _now = dt.now()
    _hr = '0%s' % _now.hour if _now.hour < 10 else str(_now.hour)
    _min = '0%s' % _now.minute if _now.minute < 10 else str(_now.minute)
    _sec = '0%s' % _now.second if _now.second < 10 else str(_now.second)
    _time = '%s:%s:%s' % (_hr, _min, _sec)
    _return = _time if time else ''
    _return += '%s[%s]' % (' ' if time else '', __parse__(_mode))

    return '%s: %s' % (_return, msg)


def __parse__(mode: int) -> str:
    _res = ''

    if mode == 0x0:
        _res = 'LOG'
    elif mode == 0x82:
        _res = 'ERROR'

    else:
        _res = 'NONE'

    return _res

# -------------------------------------------------------------


print(_format_(Mode.LOG, 'testing', True))
