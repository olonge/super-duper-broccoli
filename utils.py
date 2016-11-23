# -------------------------------------------------------------------------------
# Name:        utils
# Purpose:     Utility functions.
#
# Author:      Oluwayomi Longe
#
# Created:     Fri 18-Nov-2016 20:33
# Copyright:   (c) Olonge - AStoic Ltd 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import pprint

_pp = pprint.PrettyPrinter(indent=2)


def _print_node(node, indent, indent_symbol):
    if isinstance(node, list):
        for child in node:
            for p in _print_node(child, indent, indent_symbol):
                yield p
    elif isinstance(node, int) or isinstance(node, float) or isinstance(node, str) or node is None:
        yield ' {}'.format(node)
    elif hasattr(node, '_fields'):
        yield '\n{}{}'.format(indent_symbol * indent, type(node).__name__)
        for field in node._fields:
            yield '\n{}{}:'.format(indent_symbol * (indent + 1), field, ':')
            for p in _print_node(getattr(node, field), indent + 2, indent_symbol):
                yield p
    else:
        yield '\nError! Unable to print {}'.format(node)


def print_ast(node, indent=0, indent_symbol=' ' * 4):
    print(''.join(_print_node(node, indent, indent_symbol)))


def print_tokens(tokens):
    _pp.pprint(tokens)


def print_env(env):
    _pp.pprint(env.asdict())


def main():
    pass


if __name__ == '__main__':
    main()
