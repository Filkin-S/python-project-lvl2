import itertools
import json

SIGNS = {'REMOVE': '-',
         'ADD': '+',
         'SAVE': ' ',
         'BEFORE': '-',
         'AFTER': '+',
         'CHILD': ' '}


def sort_key(pair):
    (sign, key), value = pair
    return key


def make_line(indent, sign, key, value):
    return f'{indent}{sign} {key}: {value}'


def make_stylish(diff, replacer=' ', count=2):

    def iter_(current_value, depth):
        if not isinstance(current_value, list):
            return json.dumps(current_value).strip('"')

        deep_indent_size = depth + count
        deep_indent = replacer * (deep_indent_size + depth)
        current_indent = replacer * depth * count
        lines = []
        current_value.sort(key=sort_key)
        for element in current_value:
            (status, key), value = element
            sign = SIGNS[status]
            lines.append(make_line(deep_indent,
                                   sign,
                                   key,
                                   iter_(value, deep_indent_size)))
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(diff, 0)
