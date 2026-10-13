# Guess the Number Game

## Objective

The objective of this exercise is to create a game where the player guesses a randomly generated number.

## Description

Guess the Number is a single-player game where the player tries to guess a secret number generated randomly by the computer. The game provides feedback after each guess, indicating whether the guess is too high or too low, until the player guesses the correct number.

In this version, the player can choose the starting and ending values of the number range.

## Instructions

1. Use `input()` to ask the player to enter the starting and ending values of the range.
2. Use `int()` to convert the player's input into integers.
3. Import the `random` module to generate a random number.
4. Use `random.randint()` to generate a secret number within the selected range.
5. Use `if`, `elif`, and `else` statements to check the player's guess.
6. Use `print()` to display feedback to the player.
7. Use a `while` loop to continue the game until the correct number is guessed.
8. Use `try` and `except` to handle invalid inputs.

## Example

```text
Welcome to the Guess the Number game!
Add your start range: 1
Add your end range: 100

Enter your guess: 50
Your guess is too high. Guess again.

Enter your guess: 25
Your guess is too low. Guess again.

Enter your guess: 31
Congratulations! You guessed the number correctly!
```

## Expected Learning Outcomes

By completing this exercise, you will practice:

- Variables and data types
- User input and type conversion
- Random number generation
- Conditional statements
- `while` loops
- Exception handling using `try` and `except`

## Customization

The game can be extended by allowing the player to choose a predefined range, such as 1 to 100, or customize the range. You can also add a limited number of guesses to make the game more challenging.

## How to Run

1. Make sure Python is installed on your computer.
2. Save the code in a file named `guess_game.py`.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python guess_game.py
py guess_game
```

Enjoy playing Guess the Number!
