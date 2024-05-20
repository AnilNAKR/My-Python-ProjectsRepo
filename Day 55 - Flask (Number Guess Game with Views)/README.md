Flask Number Guessing Game
==========================

This project is a simple web application that allows users to guess a randomly generated number between 0 and 9. The application provides feedback on whether the guessed number is too low, too high, or correct. It is built using Flask, a lightweight web framework for Python.

Features
--------

-   Randomly generates a number between 0 and 9 at the start of the game.
-   Provides feedback to the user indicating if the guess was too low, too high, or correct.
-   Displays relevant images to enhance user experience.

### Routes

-   `/`: The home route where the user is prompted to guess a number. A new random number is generated each time this route is accessed.
-   `/<int:g_number>`: This route takes the user's guessed number as a parameter and returns feedback indicating whether the guess was too low, too high, or correct.

### Functions

-   `home()`: Generates a new random number and displays the prompt to guess a number.
-   `guess_number(g_number)`: Compares the guessed number to the random number and returns feedback with corresponding images.

<hr>

https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/46c35c09-8da9-4730-9915-458e445783d0

