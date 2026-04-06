# Python Foundation Assignments

This repository contains three Python assignments demonstrating foundational concepts ranging from basic math operations to building an interactive command-line game.

## Included Scripts

### 1. Level 1: Prime Number Checker (`level1_prime.py`)

This script determines whether a user-provided number is a prime number.

- **How it works:** It prompts the user to enter an integer. It then mathematically checks if the number is greater than 1 and divisible only by 1 and itself using a loop up to the square root of the number for optimized performance.
- **Usage:** Run the script and type a number when prompted.

### 2. Level 2: Find the Largest Number (`level2_largest.py`)

This script finds and returns the largest number from a user-provided list.

- **How it works:** It prompts the user to input a series of numbers separated by spaces. It parses the input, iterates through the numbers to find the maximum value, and prints the result.
- **Usage:** Run the script and enter multiple numbers separated by spaces (e.g., `12 45 7 89 23`).

### 3. Level 3: Tic-Tac-Toe Game (`level3_tictactoe.py`)

A complete, interactive command-line implementation of the classic Tic-Tac-Toe game.

- **How it works:** Two players take turns as "X" and "O". The game displays a 3x3 grid and prompts players to enter the row and column (0, 1, or 2) where they want to place their mark. The script automatically checks for a win condition (horizontal, vertical, or diagonal) or a draw (when the board becomes full).
- **Usage:** Run the script to start the game. Follow the interactive prompts to place your pieces on the board.

## How to Run

Make sure you have Python 3 installed. You can execute any of these scripts from the terminal using the following commands:

```bash
python level1_prime.py
python level2_largest.py
python level3_tictactoe.py
```
