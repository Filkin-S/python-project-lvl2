import argparse


parser = argparse.ArgumentParser(prog='gendiff')

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format',
                    default='json',
                    help='set format of output',
                    metavar='FORMAT')

args = parser.parse_args()


def main():
    print(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
