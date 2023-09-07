SIGNS = {'REMOVE': '-',
         'ADD': '+',
         'SAVE': ' ',
         'BEFORE': '-',
         'AFTER': '+'}


def sort_key(pair):
    (sign, key), value = pair
    return key


def format_to_str(diff):
    diff.sort(key=sort_key)
    result = ''
    for (sign, key), value in diff:
        result = result + f'{SIGNS[sign]} {key}: {value}\n'
    return result.join(['{\n', '}'])
