import random
numGuesses = 0
print('Hi! What is your name?')
userName = input()
theNumber = random.randint(1, 75)
print(userName + ', I am thinking of a number between 1 and 75.')
while numGuesses < 6:
    print('Take a guess.')
    theirGuess = input()
    theirGuess = int(theirGuess)
    numGuesses = numGuesses + 1
    if theirGuess < theNumber:
        print('Your guess is too low.')
    if theirGuess > theNumber:
        print('Your guess is too high.')
    if theirGuess == theNumber:
        break
if theirGuess == theNumber:
    print('Good job! You guessed my number in ' + str(numGuesses) + ' guesses!')
if theirGuess != theNumber:
    print('Sorry, nice try. The number I was thinking of was ' + str(theNumber))
