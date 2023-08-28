import json
from gendiff.parsers import parsed


def generate_diff(file1, file2):
    data1, data2 = parsed(file1), parsed(file2)
    keys1, keys2 = data1.keys(), data2.keys()
    deleted = [(-1, x, json.dumps(data1[x]).strip('"')) for x in keys1 - keys2]
    added = [(1, x, json.dumps(data2[x]).strip('"')) for x in keys2 - keys1]
    remained = []
    for key in keys1 & keys2:
        if data1[key] == data2[key]:
            remained.append((0, key, json.dumps(data2[key]).strip('"')))
        else:
            remained.append((-1, key, json.dumps(data1[key]).strip('"')))
            remained.append((1, key, json.dumps(data2[key]).strip('"')))
    result = deleted + added + remained
    result.sort(key=lambda x: x[1])
    diff = diff_to_string(result)
    print(diff)
    return diff


def diff_to_string(diff):
    signs = {-1: '-', 0: ' ', 1: '+'}
    result = ''
    for sign, key, value in diff:
        result = result + f'{signs[sign]} {key}: {value}\n'
    return result
