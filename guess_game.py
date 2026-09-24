print(""" /////////////////////////////////////////////////////
              Welcome to guess the number game
/////////////////////////////////////////////////////
""")
import random
secret_number = random.randint(1,100)
print("I have selected a number between 1 and 100. Try to guess it!")
while True:
    guess = int(input("Enter ur guess:")) 
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue
    if guess == secret_number:
        print("You guessed it correctly!")
        break
    elif guess > secret_number:
        print("Guess lower")
    elif guess < secret_number:
        print("Guess higher")
    else:
        print("Invalid input. Please enter a valid number.")