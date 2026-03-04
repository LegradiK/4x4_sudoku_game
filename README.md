# 4x4 Sudoku Game- Pygame

## Overview

This project is a 4x4 Sudoku game built using Python and Pygame.
It loads puzzles from a CSV file, allows user interaction through keyboard input, and validates entries against a predefined solution.

The application demonstrates grid rendering, event handling, state management, and structured game logic using Pygame.

---
## Features

- Interactive 4x4 Sudoku grid
- Keyboard navigation using arrow keys
- Number input (1–4)
- Erasing user-entered values
- Automatic marking of incorrect cells
- Validation against a solution file
- Warning if the board is incomplete
- Success message when puzzle is solved
- Restart and New Game functionality
- Random puzzle selection from CSV

---
## Requirements

Python 3.8 or newer

Pygame

Install Pygame using:
```
pip install pygame
```
---
## Project Structure
```bash
sudoku/
│
├── main.py              # Main game loop and event handling
├── ui.py                # Rendering and UI functions
├── button.py            # Button component
├── csv_reader.py        # Puzzle loading logic
├── 4x4-Sudoku-Dataset-master          # Stored puzzles and solutions
│     ├── 4x4_sudoku_unique_puzzles.csv  # over 1 million puizzes - some quiz overlap
│     └── 4x4_sudoku_unique_solution.csv   # 288 sudoku puzzles
└── README.md
```

---
## How to Run

From the project directory:
```
python3 main.py
```
---
## Controls

<b>Move selection</b>:	Arrow keys or mouse click

<b>Enter number</b>:	1–4 (top row or numpad)

<b>Erase cells</b>:	Backspace / Delete / E / D

<b>Validate puzzle</b>:	Enter

<b>Restarting puzzle</b>:	Restart button

<b>Loading new puzzle</b>:	New Game button

---
## Game Logic

- A puzzle and its solution are loaded from a CSV file.
- Users may only modify cells that were originally empty.
- Input is validated directly against the solution.
- Incorrect entries are marked visually.
- The puzzle is considered solved only when:
        - All cells are filled
        - No incorrect values remain

---
## Learning Objectives

This project demonstrates:
- Event-driven programming with Pygame
- Grid-based rendering
- State-driven UI updates
- Input validation against external data
- Separation of game logic and presentation
- Structured code organisation

---
## Puzzle Dataset
The Sudoku puzzles and solutions used in this project are sourced from the following repository:

<a href="https://github.com/Black-Phoenix/4x4-Sudoku-Dataset.git">Sudoku 4x4 dataset</a>
