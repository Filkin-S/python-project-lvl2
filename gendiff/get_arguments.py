import argparse


def get_arguments():
    parser = argparse.ArgumentParser(prog='gendiff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output',
                        metavar='FORMAT')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
