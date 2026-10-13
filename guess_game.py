# Import the random module to generate a random number
import random  

# Control variable: the game continues while this is True
try_guessed_number = True

# Display the welcome message
print("Welcome to the Guess the Number game!")

# Ask the user to enter a valid range
while True:
    try:
        # Get the starting and ending values from the user
        start_range = int(input("Add your start range: "))
        end_range = int(input("Add your end range: "))

        # Check that the starting value is smaller than the ending value
        if start_range >= end_range:
            print("The start range must be smaller than the end range.")
        else:
            # Exit the loop if the range is valid
            break

    except ValueError:
        # Handle cases where the user enters something other than an integer
        print("Please enter valid numbers!")

# Generate a random number between the selected range (inclusive)
Guess = random.randint(start_range, end_range)

# Continue asking the user to guess until the correct number is found
while try_guessed_number:
    try:
        # Ask the user to enter their guess
        test = int(input("Enter your guess: "))

        # Check if the guess is greater than the secret number
        if test > Guess:
            print("Your guess is too high. Guess again.")

        # Check if the guess is smaller than the secret number
        elif test < Guess:
            print("Your guess is too low. Guess again.")

        # If neither condition is true, the guess is correct
        else:
            print("Congratulations! You guessed the number correctly!")

            # Stop the game by setting the control variable to False
            try_guessed_number = False

    except ValueError:
        # Handle invalid guesses, such as letters or empty input
        print("Please enter a valid number!")
