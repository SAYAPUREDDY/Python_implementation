import random
number=str(random.randint(0,9999))

def compare_number(number,user_guess):
    cowbull=[0,0]
    for i in range(len(number)):
        if number[i]==user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull
    
def playing(number):
    playing=True
    guesses=0
    while playing:
        user_guess=input("Give the guess")
        if user_guess=="exit":
            print(f"lost the game.the secret number is {number}")
            break
        cowbullcount=compare_number(number,user_guess)
        guesses+1
        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing=False
            print("u have won the game")
            break
        else:
            print("try again")
if __name__=="__main__":
    print("welcome to game")
    playing(number)
