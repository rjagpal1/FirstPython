import random
number = random.randint(1, 10)

player_name = input("Hello, What is your name? ")
number_of_guesses = 0
print('Okay! '+ player_name+ " let's play a Guessing number Game.")
print("I am Guessing a number between 1 and 10, can you guess it?")

while number_of_guesses < 5:
    print() #Print a blank line each time
    guess = int(input("Take a guess: "))
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
print() #Print a blank line 
if guess == number:
    print('You guessed it Right in ' + str(number_of_guesses) + ' tries!')
else:
    print('You LOST, the number was ' + str(number))