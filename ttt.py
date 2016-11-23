# -------------------------------------------------------------------------------
# Name:        ttt
# Purpose:     Python 2 to 3 compatibility helpers.
#
# Author:      Oluwayomi Longe
#
# Created:     Fri 18-Nov-2016 20:18
# Copyright:   (c) Olonge - AStoic Ltd 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import sys

PY2 = sys.version_info[0] == 2


if PY2:
    iteritems = lambda d: d.iteritems()
else:
    iteritems = lambda d: iter(d.items())


def main():
    pass


if __name__ == '__main__':
    main()
