import random
import sys


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_guess() -> str:
    while True:
        guess = input('Guess: ')
        if guess is None or len(guess) > 1 or not guess.islower():
            print('Your guess must have exactly one letter')
        else:
            return guess


def update_dashes(secret_word: str, dashes: str, guess: str) -> str:
    dash_parts = list(dashes)

    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            dash_parts[i] = guess

    retval = "".join(dash_parts)
    return retval


def guess_word(secret_word: str):
    dashes = '-' * len(secret_word)
    guesses_left = 10
    while guesses_left > 0 and dashes != secret_word:
        print(dashes)
        print(f'{guesses_left} incorrect guesses left.')
        letter = get_guess()
        idx = secret_word.find(letter)
        if idx == -1:
            print('That letter is not in the word.')
            guesses_left -= 1
        else:
            print('That letter is in the word!')
            dashes = update_dashes(secret_word, dashes, letter)

        print(f'{guesses_left} incorrect guesses remaining')

    if dashes == secret_word:
        print(f'Congrats! You win. The word was: {secret_word}')
    else:
        print(f'Sorry, you lose. The word was: {secret_word}')


if __name__ == '__main__':
    print(f'Word Guess Game using python: {get_python_version()}')
    words = ['rabbit', 'banana', 'egg', 'turtle']
    secret_word = random.choice(words)
    guess_word(secret_word)
