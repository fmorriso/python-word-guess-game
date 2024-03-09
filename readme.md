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
#### Step 1 - Variable For Dashes

Make another string variable called ```dashes``` that holds a number of dashes equal to the length of the secret word. 
So, if your secret word is *“eggplant”*, your ```dashes``` variable should have eight dashes.

Before printing your prompt that says ```“Guess: “```, print the value of your dashes variable.

#### Step 2 - Update the Dashes

Here’s the tricky part. 
Write a function called 
```python
update_dashes
``` 
that takes three string arguments:
1. the secret word
1. the current state of dashes
1. the most recent guess

and returns the new state of dashes.

So, for example, if the word is *"eggplant"*, the current value of dashes is
```text
"e-------"
```
and the guess is *"g"*, the function should return
```text
"egg-----"
```

If the word is *"eggplant"*, the current value of dashes is
```text
"e-------"
```
and the guess is *"z"*, the function should return 
```text
"e-------" 
```
(nothing changes, since the guess was incorrect).

Here’s how you _*might*_ go about this.

In your function, start with an empty result string. 
Write a for loop from 0 up to but not including the length of your secret word. 
Say you use the variable i in your for loop. 
Compare the character in ```secret_word``` at index ```i``` to the guess. 
If they’re equal, then that means the guess matches that letter in the word,
so you should add the guess to the result. 
Otherwise, the guess does not match that letter in the word, 
so you should add whatever was at index ```i``` in dashes to your result.

Wait, why don’t I just add a dash in the second case?

If you just add a dash whenever the guess doesn’t match the character in ```secret_word```
at index ```i```, that will wipe out any correct guesses the user has already made! 
Imagine the case where the word is *“eggplant”*, the state of ```dashes``` is ```“e——-“```, 
and the guess is “g”. 
If you always add a dash when the guess doesn’t match the character in secret_word at index i,
the result would be “-gg—–”. 
Suddenly, the “e” is gone, because “g” did not match “e”! By instead using dashes at index i, you might append either a letter or a dash, depending on whether or not the user had already guessed that letter prior to the current guess.

Once your for loop is done, your result string should have letters and dashes
in all the right places, so you can just return it!

#### Step 3 - Put It All Together

Whenever the user guesses correctly, use your ```update_dashes``` function to actually
update your variable called ```dashes```.

Now, each time you print your dashes variable, 
it should reflect what the user has and has not guessed

### Part 3

At this point, you should have a program that can print a string with dashes and letters
in the correct places based on the user’s guesses.

#### End Result

When you’re finished with this exercise, you’ll have a program that more or less
correctly simulates the full game. 
The person running your program can win by guessing all the letters in the word,
and they can lose by running out of guesses!

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
### Part 4
In this exercise, you are going to add a little bit of code to allow your program to randomly select a word from a list of words.

End Result

Once you’ve finished the two steps below, your program should use a random word from your list each time you play!

#### Step 1 - Make a List

First, make a list of strings called ```words```. 
Each string should be a word that your game might use.

#### Step 2 - Pick From the List

Then, instead of assigning a particular string to ```secret_word```, 
use a function called ```choice``` contained in the ```random``` module. Here’s how to do it:

At the top of your program, write 
```python
import random
```
You can then use the function ```random.choice```. 
It takes a single argument - in this case, a list - and it returns a random element from that argument. 
Use this function when you assign to secret_word near the beginning of your program.

