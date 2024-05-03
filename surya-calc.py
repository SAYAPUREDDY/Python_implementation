#!/usr/bin/env python3

### File:     praveenkum.py
### Date:     2023-11-01
### Author:   Harshini Praveen Kumar, University of Potsdam
### Homework: Week 2 - Calculator

import sys
import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def add():
    num1 = random.randint(10, 100)
    num2 = random.randint(10, 100)
    print(f"What is the result of {num1} + {num2}?")
    result = num1 + num2
    answer = int(input("Enter your answer: "))
    if answer == result:
        print(GREEN,"Correct!",RESET)
    else:
        print(RED,"Wrong answer you dumb",RESET)

def multi():
    num1 = random.randint(2, 14)
    num2 = random.randint(2, 14)
    print(f"What is the result of {num1} * {num2}?")
    result = num1 * num2
    answer = int(input("Enter your answer: "))
    if answer == result:
        print(GREEN,"CORRECTTT!",RESET)
    else:
        print(RED,"WRONG ANSWER YOU DUMBBB",RESET)

def menu(n=5):
    x = 0
    while True:
        x += 1
        sel = input("Select: (a)dd, m(multi), (q)uit: ")
        if sel == "q":
            break
        elif sel == "a":
            add()
        elif sel == "m":
            multi()
        else:
            print(RED,"Wrong choice!",RESET)
            print(RED,"you didn't choose the right option",RESET)
            
        if x >= n:
            print(YELLOW,"Thats it for now, GO STUDY",RESET)
            break
        
def main(args):
    print(YELLOW, "welcome to calculatorrr ", RESET)
    print(YELLOW, "Please choose one of the options below ", RESET)
    menu()
    
if __name__ == "__main__":
        main(sys.argv)
    
    


