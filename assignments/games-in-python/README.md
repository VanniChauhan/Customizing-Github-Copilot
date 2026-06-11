
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Python Hangman game that uses strings, loops, and conditionals to let players guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the game structure and randomly choose a hidden word from a predefined list.

#### Requirements
Completed program should:

- Define a list of secret words.
- Randomly select one word at the start of the game.
- Keep the selected word hidden from the player.

### 🛠️ Player Guesses and Progress Display

#### Description
Allow the player to guess letters and display the current progress with blanks for unknown letters.

#### Requirements
Completed program should:

- Prompt the player for a letter guess.
- Reveal correctly guessed letters while keeping other letters hidden.
- Show the current progress in a `_ _ _` style format.

### 🛠️ Guess Tracking and Win/Lose Logic

#### Description
Track incorrect guesses and end the game when the player wins or uses all attempts.

#### Requirements
Completed program should:

- Count incorrect letter guesses.
- Limit the number of wrong attempts.
- Display a winning message when the word is fully guessed.
- Display a losing message when attempts run out.
