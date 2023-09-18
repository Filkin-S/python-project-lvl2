from gendiff import engine
from gendiff.formatters import plain, stylish


def test_generate_diff_nested_json():
    with open('tests/fixtures/result_nested.txt') as f:
        expected = f.read()

    assert engine.generate_diff('tests/fixtures/file1_nested.json',
                                'tests/fixtures/file2_nested.json',
                                stylish.make_stylish
                                ) == expected


def test_generate_diff_nested_yml():
    with open('tests/fixtures/result_nested.txt') as f:
        expected = f.read()

    assert engine.generate_diff('tests/fixtures/file1_nested.yml',
                                'tests/fixtures/file2_nested.yml',
                                stylish.make_stylish
                                ) == expected


def test_generate_diff_nested_plain():
    with open('tests/fixtures/result_nested_plain.txt') as f:
        expected = f.read()

    assert engine.generate_diff('tests/fixtures/file1_nested.json',
                                'tests/fixtures/file2_nested.json',
                                plain.make_plain
                                ) == expected


def test_generate_diff_hexlet_json_stylish():
    with open('tests/fixtures/result_stylish') as f:
        expected = f.read()

    assert engine.generate_diff('tests/fixtures/file1.json',
                                'tests/fixtures/file2.json',
                                stylish.make_stylish
                                ) == expected


def test_generate_diff_hexlet_yaml_stylish():
    with open('tests/fixtures/result_stylish') as f:
        expected = f.read()

    assert engine.generate_diff('tests/fixtures/file1.yml',
                                'tests/fixtures/file2.yml',
                                stylish.make_stylish
                                ) == expected


def test_generate_diff_hexlet_json_plain():
    with open('tests/fixtures/result_plain') as f:
        expected = f.read()

    assert engine.generate_diff('tests/fixtures/file1.json',
                                'tests/fixtures/file2.json',
                                plain.make_plain
                                ) == expected


def test_generate_diff_hexlet_yaml_plain():
    with open('tests/fixtures/result_plain') as f:
        expected = f.read()

    assert engine.generate_diff('tests/fixtures/file1.yml',
                                'tests/fixtures/file2.yml',
                                plain.make_plain
                                ) == expected
