from gendiff.engine import generate_diff


def test_generate_diff_json():
    with open('tests/fixtures/result1.txt') as f:
        expected = f.read()

    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json'
                         ) == expected


def test_generate_diff_yml():
    with open('tests/fixtures/result1.txt') as f:
        expected = f.read()

    assert generate_diff('tests/fixtures/file1.yml',
                         'tests/fixtures/file2.yml'
                         ) == expected
