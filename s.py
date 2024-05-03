import argparse

def add_numbers(x, y):
    result = x + y
    print(f"The sum of {x} and {y} is {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple script to add two numbers.') # uused ot create a parser
    parser.add_argument('x', type=int, help='First number')  # adding an argument and help indicates the first arugument in the command line argumenst
    parser.add_argument('y', type=int, help='Second number')

    args = parser.parse_args()      #this is given to save all the aruguments in a list
    add_numbers(args.x, args.y)
