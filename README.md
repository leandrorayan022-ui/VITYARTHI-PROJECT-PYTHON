Advanced Number Guessing Game

Overview of the Project:

The Advanced Number Guessing Game is an interactive, console-based game developed in Python. It challenges the player to guess a randomly generated secret number within a selected range and a limited number of attempts. The game provides three difficulty levels—Easy, Medium, and Hard—with different number ranges and attempt limits. It also maintains a cumulative score throughout the session and provides feedback after every guess.

The application is designed to demonstrate fundamental Python programming concepts including random number generation, functions, loops, conditional statements, user input, exception handling, formatted output, and score calculation.

Features:

Multi-Level Difficulty: Supports 3 distinct difficulty levels:

Easy: Number range from 1–50 with 10 attempts
Medium: Number range from 1–100 with 7 attempts
Hard: Number range from 1–200 with 5 attempts
Random Secret Number Generation: A secret number is randomly generated within the selected difficulty range using Python's random.randint() function.

Limited Attempts: Each difficulty level provides a fixed number of attempts. The player must identify the secret number before running out of attempts.

Dynamic Feedback: After every valid guess, the game informs the player whether the guessed number is:

Too low
Too high
Correct
Dynamic Hint System: After the third unsuccessful valid attempt, the game provides a hint indicating whether the secret number is even or odd.

Score System: Players receive points based on how quickly they correctly guess the number. The score is calculated according to the number of attempts used:

Score = (Maximum Attempts - Attempts Used + 1) × 10
This means fewer attempts result in a higher score.

Cumulative Score: The score continues to accumulate across multiple rounds during the same game session.

Input Validation & Error Handling: The program handles invalid difficulty selections and non-numeric guesses without terminating the game. try-except is used to catch ValueError when the player enters something that cannot be converted into an integer.

Exit Option: The player can select option 4 at any time from the difficulty menu to exit the game and view the final score.

Technical Specifications:

Language: Python 3

Primary Function: number_guessing_game()

Python Modules Used:

random — used for generating the secret number
Core Concepts:

Functions
Variables
while loops
if-elif-else conditional statements
try-except exception handling
User input using input()
Integer conversion using int()
Random number generation using random.randint()
Formatted strings using f-strings
Boolean variables
Arithmetic expressions
Modulo operator %
Program entry-point condition using if __name__ == "__main__":
How It Works:

Game Initialization: The program starts by calling the number_guessing_game() function. A welcome message is displayed and the player's score is initialized to zero.

Difficulty Selection: The player is presented with four options:

1. Easy
2. Medium
3. Hard
4. Exit Game
Based on the selected option, the program assigns an upper limit and maximum number of attempts:

Easy   → upper limit = 50,  attempts = 10
Medium → upper limit = 100, attempts = 7
Hard   → upper limit = 200, attempts = 5
Secret Number Generation: After selecting a difficulty, the program generates a random integer between 1 and the selected upper limit:

secret_number = random.randint(1, upper_limit)
The attempt counter is then initialized to zero and the won variable is set to False.

Guess Processing: The player enters a guess using the input() function. The input is converted into an integer using int().

If the input is not a valid integer, the ValueError exception is caught and an error message is displayed. The player is then allowed to enter the guess again.

Comparison Logic: After a valid guess, the program compares it with the secret number:

If guess == secret number
    Player wins

If guess < secret number
    Display "Too low"

If guess > secret number
    Display "Too high"
The attempt counter is increased after each valid guess.

Hint Generation: If the player has made exactly three unsuccessful valid attempts, the program checks the secret number using the modulo operator:

secret_number % 2
If the remainder is 0, the number is even; otherwise, it is odd. The corresponding hint is displayed to the player.

Winning Condition: When the player correctly guesses the secret number, the program displays the number of attempts used and calculates the score. The current round then ends.

Losing Condition: If the player uses all available attempts without guessing correctly, the program displays the correct secret number and ends the current round.

Continuous Gameplay: After every completed round, the current total score is displayed and the player is returned to the difficulty-selection menu. This allows multiple rounds to be played without restarting the program.

Execution Guide:

Run the Program

Save the Python source code as:

Rayan.py
Run it using:

python Rayan.py
or, depending on the Python installation:

python3 Rayan.py
Interactive Game Mode

The program starts directly in interactive mode and displays:

========================================
      WELCOME TO ADVANCED GUESS
========================================

Select Difficulty:
1. Easy (1 - 50, 10 attempts)
2. Medium (1 - 100, 7 attempts)
3. Hard (1 - 200, 5 attempts)
4. Exit Game
The player can select a difficulty and begin guessing.

Example:

Enter your choice (1-4): 2

I have picked a number between 1 and 100.
You have 7 attempts.

Attempt 1/7 - Enter your guess: 40
📈 Too high!

Attempt 2/7 - Enter your guess: 20
📉 Too low!

Attempt 3/7 - Enter your guess: 30
📉 Too low!

💡 Hint: The secret number is an even number.
If the correct number is eventually guessed, the game displays the number of attempts used and updates the total score.

Program Structure:

The main game functionality is contained inside the:

number_guessing_game()
function.

The function manages:

Game initialization
Difficulty selection
Random number generation
Attempt tracking
User input
Guess comparison
Hint generation
Score calculation
Win/loss handling
Continuous gameplay
The program starts execution through:

if __name__ == "__main__":
    number_guessing_game()
This ensures that the game function is executed when the Python file is run directly.

Conclusion:

The Advanced Number Guessing Game is a simple but interactive Python project that demonstrates the practical use of fundamental programming concepts. It combines random number generation, conditional logic, loops, functions, exception handling, user input validation, and arithmetic calculations to create an engaging command-line game.

The project also introduces game-development concepts such as difficulty levels, limited attempts, dynamic hints, scoring, win/loss conditions, and persistent session scores. Implementing the game provides practical experience with Python control flow and user interaction while keeping the program lightweight and easy to execute from the command line.

Moving forward, potential enhancements could include high-score storage, multiple players, additional hint types, difficulty customization, a graphical user interface (GUI), sound effects, and leaderboard functionality.
