import random

def getting_word():
    with open('words_using_requests.txt', 'r') as file:
        words = file.read().splitlines()
    random_word = random.choice(words).upper()
    print(random_word)
    return random_word

def hangman_game():
    word = getting_word()  
    guessed = ["-" for _ in word] 
    lstguessed = []  

    while True:
        letter = input('Guess a letter: ').upper()
        print('Current word: ' + ''.join(guessed))

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single valid letter.")
            continue

        if letter in lstguessed:
            print("You already guessed that letter.")
            continue

        lstguessed.append(letter)

        if letter in word:
            for i, l in enumerate(word):
                if l == letter:
                    guessed[i] = letter
            print('Good guess!')
        else:
            print('Wrong guess!')

        if '-' not in guessed:
            print("Congratulations! You won! The word was: " + ''.join(word))
            break

if __name__ == "__main__":
    hangman_game()

