import json

from gendiff.formatters.stylish import sort_key


def make_json(diff):
    diff.sort(key=sort_key)
    return json.dumps(diff, sort_keys=True) + '\n'
