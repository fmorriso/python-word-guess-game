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


def update_dashes(word: str, dashes: str, guess: str) -> str:
    dash_parts = list(dashes)

    for i in range(len(word)):
        if word[i] == guess:
            dash_parts[i] = guess

    dashes = "".join(dash_parts)
    return dashes


def guess_word(secret: str) -> None:
    dashes = '-' * len(secret)
    guesses_left = 10
    while guesses_left > 0 and dashes != secret:
        print(dashes)
        print(f'{guesses_left} incorrect guesses left.')
        letter = get_guess()
        idx = secret.find(letter)
        if idx == -1:
            print('That letter is not in the word.')
            guesses_left -= 1
        else:
            print('That letter is in the word!')
            dashes = update_dashes(secret, dashes, letter)

        print(f'{guesses_left} incorrect guesses remaining')

    if dashes == secret:
        print(f'Congrats! You win. The word was: {secret}')
    else:
        print(f'Sorry, you lose. The word was: {secret}')


if __name__ == '__main__':
    print(f'Word Guess Game using python: {get_python_version()}')
    words = ['rabbit', 'banana', 'egg', 'turtle']
    secret_word = random.choice(words)
    guess_word(secret_word)
