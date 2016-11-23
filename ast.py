# -------------------------------------------------------------------------------
# Name:        ast.py
# Purpose:     Abstract syntax tree nodes.
#
# Author:      Oluwayomi Longe
#
# Created:     Fri 18-Nov-2016 20:16
# Copyright:   (c) Olonge - AStoic Ltd 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from collections import namedtuple

Number = namedtuple('Number', ['value'])
String = namedtuple('String', ['value'])
Identifier = namedtuple('Identifier', ['value'])
Assignment = namedtuple('Assignment', ['left', 'right'])
BinaryOperator = namedtuple('BinaryOperator', ['operator', 'left', 'right'])
UnaryOperator = namedtuple('UnaryOperator', ['operator', 'right'])
Call = namedtuple('Call', ['left', 'arguments'])
Function = namedtuple('Function', ['name', 'params', 'body'])
Condition = namedtuple('Condition', ['test', 'if_body', 'elifs', 'else_body'])
ConditionElif = namedtuple('ConditionElif', ['test', 'body'])
Match = namedtuple('Match', ['test', 'patterns', 'else_body'])
MatchPattern = namedtuple('MatchPattern', ['pattern', 'body'])
WhileLoop = namedtuple('WhileLoop', ['test', 'body'])
ForLoop = namedtuple('ForLoop', ['var_name', 'collection', 'body'])
Break = namedtuple('Break', [])
Continue = namedtuple('Continue', [])
Return = namedtuple('Return', ['value'])
Array = namedtuple('Array', ['items'])
Dictionary = namedtuple('Dictionary', ['items'])
SubscriptOperator = namedtuple('SubscriptOperator', ['left', 'key'])
Program = namedtuple('Program', ['body'])


def main():
    pass


if __name__ == '__main__':
    main()
