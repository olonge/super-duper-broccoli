# -------------------------------------------------------------------------------
# Name:        errors
# Purpose:     Exceptions and exception helpers.
#
# Author:      Oluwayomi Longe
#
# Created:     Fri 18-Nov-2016 20:20
# Copyright:   (c) Olonge - AStoic Ltd 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------


class InterpSyntaxError(Exception):

    def __init__(self, message, line, column):
        super(InterpSyntaxError, self).__init__(message)
        self.message = message
        self.line = line
        self.column = column


def report_syntax_error(lexer, error):
    line = error.line
    column = error.column
    source_line = lexer.source_lines[line - 1]
    print('Syntax error: {} at line {}, column {}'.format(error.message, line, column))
    print('{}\n{}^'.format(source_line, ' ' * (column - 1)))


def main():
    pass


if __name__ == '__main__':
    main()
