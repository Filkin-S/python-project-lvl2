
from gendiff.parsers import parsed
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


def generate_diff(file1, file2, format='stylish'):
    formatter = turn_format(format)
    data1, data2 = parsed(file1), parsed(file2)
    diff = make_diff(data1, data2)
    formatted_diff = formatter(diff).rstrip()
    return formatted_diff


def turn_format(argument):
    if argument == 'plain':
        return make_plain
    elif argument == 'json':
        return make_json
    else:
        return make_stylish


def is_child(value1, value2):
    return isinstance(value1, dict) & isinstance(value2, dict)


def make_pair(sign, key, value):
    return (sign, key), value


def compare_equal(key, value1, value2):
    diff = {}
    if value1 == value2:
        diff = (make_pair('SAVE', key, value1), )
    elif is_child(value1, value2):
        diff = (make_pair('CHILD', key, make_diff(value1, value2)), )
    else:
        diff = (make_pair('BEFORE', key, flatten(value1)),
                make_pair('AFTER', key, flatten(value2)))
    return diff


def make_diff(data1, data2):
    keys1, keys2 = data1.keys(), data2.keys()
    diff = list()
    for key in keys1 & keys2:
        diff.extend(compare_equal(key, data1[key], data2[key]))
    for key in keys1 - keys2:
        diff.append(make_pair('REMOVE', key, flatten(data1[key])))
    for key in keys2 - keys1:
        diff.append(make_pair('ADD', key, flatten(data2[key])))
    return diff


def flatten(value):
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            v = flatten(v)
            lines.append(make_pair('SAVE', k, v))
        return lines
    return value
