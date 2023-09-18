#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.get_arguments import get_arguments


def main():
    arguments = get_arguments()
    print(generate_diff(*arguments))


if __name__ == '__main__':
    main()
