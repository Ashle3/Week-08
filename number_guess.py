import random

#generate a random number between 1 and 100
ranNum = random.randint(1,101)

#function removes a turn
def subtract_turn(turn):
    newTurn = turn-1
    return newTurn

print()
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print()

# Number of attempts allowed
attemptsLeft = 10
# Number of attempts completed
attempts = 0
# Array holds the user's previous guesses
guesses = []

while attemptsLeft > 0:
    # Print out the number of tries left
    print(f"Attempts left: {attemptsLeft}")
    # If there are guesses in the array, then print the array
    if len(guesses) > 0:
        print(f"Previous Guesses: {guesses}")
    #user enters guess here
    userGuess = int(input("Enter a number: "))
    #Add the user guess to the guesses array
    guesses.append(userGuess)

    # Guess too low
    if userGuess < ranNum:
        print()
        print("Higher")
        print()
        # Subtract a turn from attemptsLeft
        attemptsLeft = subtract_turn(attemptsLeft)
        # Add 1 to the number of attempts
        attempts += 1
    # Guess too high
    elif userGuess > ranNum:
        print()
        print("Lower")
        print()
        # Subtract a turn from attemptsLeft
        attemptsLeft = subtract_turn(attemptsLeft)
        # Add 1 to the number of attempts
        attempts += 1
    else:
        print()
        # Prints the correct answer
        print(f"You Got It! The number is {ranNum}.")
        print()
        # Turns attemptsLeft into a negative number so that it exits the while loop on line 23
        attemptsLeft = -1

# If the player runs out of turns
if attemptsLeft == 0:
    print("GAME OVER. You've run out of turns.")
    print(f"The number was {ranNum}")
    print()
    print("GAME SUMMARY: ")
    print(f"Total number of attempts: {attempts}")
    print(f"Guesses: {guesses}")
    print()
# If the player wins
elif attemptsLeft == -1:
    print("Thank you for playing! ")
    print()
    print("GAME SUMMARY: ")
    print(f"Total number of attempts: {attempts}")
    print(f"Guesses: {guesses}")
    print()







# # Generate a random number between 1 and 100
# secret_number = random.randint(1, 100)

# # Initialize a valid variable.
# valid = False

# # Start the loop. End when valid is true. 
# while not valid:
#     try:
#         # Ask the player to guess the number
#         guess = int(input("Your guess: "))
#         attempts += 1

#         if guess < secret_number:
#             print("Too low! Try again.")
#         elif guess > secret_number:
#             print("Too high! Try again.")
#         else:
#             valid = True
#             print(f"Congratulations! You've guessed the number in {attempts} attempts.")

#     except ValueError:
#         print("Please enter a valid number.")

