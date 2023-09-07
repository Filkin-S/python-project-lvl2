import json
from gendiff.parsers import parsed
from gendiff.formatters.str_format import format_to_str


def generate_diff(file1, file2, formatter=format_to_str):
    diff = make_diff(file1, file2)
    formatted_diff = formatter(diff)
    print(formatted_diff)
    return formatted_diff


def make_pair(sign, key, value):
    return (sign, key), json.dumps(value).strip('"')


def compare_equal(key, value1, value2):
    diff = {}
    if value1 == value2:
        diff = (make_pair('SAVE', key, value1), )
    else:
        diff = (make_pair('BEFORE', key, value1),
                make_pair('AFTER', key, value2))
    return diff


def make_diff(file1, file2):
    data1, data2 = parsed(file1), parsed(file2)
    keys1, keys2 = data1.keys(), data2.keys()
    diff = []
    for key in keys1 - keys2:
        diff.append(make_pair('REMOVE', key, data1[key]))
    for key in keys2 - keys1:
        diff.append(make_pair('ADD', key, data2[key]))
    for key in keys1 & keys2:
        diff.extend(compare_equal(key, data1[key], data2[key]))
    return diff
