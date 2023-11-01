import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Number of attempts allowed
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Initialize a valid variable.
valid = False

# Start the loop. End when valid is true. 
while not valid:
    try:
        # Ask the player to guess the number
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            valid = True
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

    except ValueError:
        print("Please enter a valid number.")

