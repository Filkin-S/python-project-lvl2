from gendiff.engine import generate_diff
from gendiff.formatters import plain, stylish


def test_generate_diff_nested_json():
    with open('tests/fixtures/result_nested.txt') as f:
        expected = f.read()

    assert generate_diff('tests/fixtures/file1_nested.json',
                         'tests/fixtures/file2_nested.json',
                         stylish.make_stylish
                         ) == expected


def test_generate_diff_nested_yml():
    with open('tests/fixtures/result_nested.txt') as f:
        expected = f.read()

    assert generate_diff('tests/fixtures/file1_nested.yml',
                         'tests/fixtures/file2_nested.yml',
                         stylish.make_stylish
                         ) == expected


generate_diff('tests/fixtures/file1_nested.json',
              'tests/fixtures/file2_nested.json',
              stylish.make_stylish
              )
