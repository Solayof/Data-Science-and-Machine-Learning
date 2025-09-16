# Task 1: Rock, Paper, Scissors Game Simulation

## Overview

This task implements a simple Rock, Paper, Scissors game in Python. The game allows a user to play against the computer in an interactive command-line environment. The computer randomly selects its move, and the user is prompted to enter their choice. The game continues until the user decides to stop.

## Features

- Interactive gameplay between user and computer
- Input validation for user choices
- Randomized computer moves
- Clear display of choices and results
- Option to replay or exit

## How It Works

1. The user is prompted to enter a choice: `rock`, `paper`, or `scissors`.
2. The computer randomly selects one of the three options.
3. Both choices are displayed, and the winner is determined based on standard game rules:
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock
    - Same choices result in a tie
4. The user is asked if they want to play again. The game continues until the user chooses to exit.

## Usage

To run the game, execute the following command in your terminal:

```bash
python task-1-game-simulation.py
```

Follow the on-screen prompts to play the game.

## Example Output

```CLI
Enter a choice (rock, paper, scissors): rock

You chose: rock
The computer chose: scissors

You win!

Do you want to play again? (yes/no): no
Thanks for playing! Goodbye.
```

---
*Add more sections for other tasks below as needed.*
