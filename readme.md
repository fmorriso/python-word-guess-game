# Word Guess Game
## Requirements
The requirements are split into three parts.
### Part 1
When you are finished with this part of the project, you’ll have a program that can print a string with dashes and letters in the correct places based on the user’s guesses, like this:
```text
--------
Guess: e
That letter is in the word!
e-------
Guess: t
That letter is not in the word.
e-------
Guess: g
That letter is in the word!
egg-----
Guess: 
```
### Part 2
### Part 3
At this point, you should have a program that can print a string with dashes and letters in the correct places based on the user’s guesses.

End Result

When you’re finished with this exercise, you’ll have a program that more or less correctly simulates the full game. The person running your program can win by guessing all the letters in the word, and they can lose by running out of guesses!

#### Step 1 - Letting the User Win

Right now, you have a while loop that lets the user enter 10 guesses. 
Change the loop so that it actually has a condition that it checks. 
That condition should be ```False``` if the user guessed every letter, and ```True``` otherwise.
(How might you write a boolean expression that does this?)

Outside the while loop, you should print something that says, ```“Congrats! You win. The word was: “```, 
followed by the secret word. 
You can do this because you know that if the while loop finished, the condition became ```False```, which means the user guessed every letter.

#### Step 2 - Letting the User Lose

Make a variable called ```guesses_left``` that stores an integer corresponding to how many incorrect guesses the user has left. Set it to 10 initially. Each time the user guesses a letter that is not in the word, subtract one from this variable.

Print the value of this variable each time you prompt the user for a guess, like this:
```text
-------
10 incorrect guesses left.
Guess: e
That letter is in the word!
e-------
10 incorrect guesses left.
Guess: t
That letter is not in the word.
e-------
9 incorrect guesses left.
Guess: g
That letter is in the word!
egg-----
9 incorrect guesses left.
Guess: r
That letter is not in the word.
egg-----
8 incorrect guesses left.
Guess: 
```