import json

from gendiff import generate_diff
from gendiff.formatters.stylish import sort_key


def make_plain(diff):
    str_diff = ''
    diff.sort(key=sort_key)
    for element in diff:
        (status, key), value = element
        if status == 'CHILD':
            str_diff += make_plain(deepen(key, value))
        else:
            str_diff += select(element)
    return str_diff


def deepen(key, value):
    new_diff = []
    for element in value:
        (status_v, key_v), value_v = element
        new_key = '.'.join([key, key_v])
        new_diff.append(generate_diff.make_pair(status_v, new_key, value_v))
    return new_diff


def select(element):
    (status, key), value = element
    if (status != 'REMOVE' or status != 'SAVE') and isinstance(value, list):
        element = generate_diff.make_pair(status, key, '[complex value]')
        return make_line(element)
    elif status == 'SAVE':
        return ''
    element = generate_diff.make_pair(status,
                                      key,
                                      json.dumps(value).replace('"', "'"))
    return make_line(element)


def make_line(element):
    appendix = ''
    (status, key), value = element
    if status == 'REMOVE':
        appendix = 'removed\n'
    elif status == 'BEFORE':
        appendix = f'updated. From {value} to '
    elif status == 'AFTER':
        return f'{value}\n'
    elif status == 'ADD':
        appendix = f'added with value: {value}\n'
    return f"Property '{key}' was {appendix}"
