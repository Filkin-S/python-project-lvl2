import argparse

from gendiff.engine import generate_diff
from gendiff.formatters.stylish import make_stylish

parser = argparse.ArgumentParser(prog='gendiff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format',
                    default='stylish',
                    help='set format of output',
                    metavar='FORMAT')

args = parser.parse_args()

diff = generate_diff(args.first_file, args.second_file, make_stylish)
