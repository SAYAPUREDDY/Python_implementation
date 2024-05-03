import random

RED="\033[31m"
GREEN = "\033[32m"
RESET="\033[0m"

# displayed men options will be the following
def menu():
    print("Welcome to the Console Calculator!")
    print("Choose an operation:")
    print("m - Multiplication")
    print("a - Addition")
    print("q - Quit")

# Now i have added the Add function first as it is in the requirement
def add():
    num1 = random.randint(10, 100)
    num2 = random.randint(10, 100)
    print(f"What is the result of {num1} + {num2}?")
    return num1 + num2

# Now i have added the Multiple function second as it is in the requirement
def multi():
    num1 = random.randint(2, 14) # using only numbers from 2-14
    num2 = random.randint(2, 14)
    print(f"What is the result of {num1} * {num2}?")
    return num1 * num2

# Now coming to the main function where ill be giving remaining requirements
def main():
    correct_answers = 0
    total_questions = 5 # total number of questions are only 5

    while True:
        menu()
        choice = input("Enter m/a/q: ")

        if choice == 'm':
            result = multi()
            answer = int(input("Enter your answer: "))
            if answer == result:
                print(GREEN,"Correct!",RESET)
                correct_answers += 1
            else:
                print(RED,"Wrong Answer u dumbb",RESET)

        elif choice == 'a':
            result = add()
            answer = int(input("Enter your answer: "))
            if answer == result:
                print(GREEN,"Correct!",RESET)
                correct_answers += 1
            else:
                print(RED,"Wrong Answer u dumbb",RESET)

        elif choice == 'q':
            break

        else:
            print("Invalid choice. Please enter m, a, or q.")

        total_questions -= 1
        if total_questions == 0:
            break

    print("\n*** Summary ***")
    print(f"Total correct answers: {correct_answers} out of 5")

if __name__ == "__main__":
    main()
