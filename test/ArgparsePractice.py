import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type = str, help='What is your name', required=True)
    parser.add_argument('--a', type = int, help='What is your age',required=True )
    parser.add_argument('--x', type=int, help='What is the first number?',required=True)
    parser.add_argument('--y', type=int,help='What is the second number?',required=True)
    parser.add_argument('--operation', type=str, default='add',help='What operation? Choose add, sub, mul, or div',required=True)
    args = parser.parse_args()
    print("Hello my name is "+ args.n)
    print(calc(args))
    
def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()


