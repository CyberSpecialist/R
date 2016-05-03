import random
num_to_guess = random.randrange(1, 10)
number = input("Pick a number between 1 and 10 ")
answer = int (number)

if answer == num_to_guess:
    print ("Congrats You Guessed Right!")
    
else:
    print("Too bad. You guessed wrong.")

print ("The number was ", num_to_guess)
