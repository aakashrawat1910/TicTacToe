# README

## Tic-Tac-Toe Game

### Description
This is a command-line implementation of the classic Tic-Tac-Toe game. The game can be played in two modes:
1. **Single Player Mode:** You compete against the computer.
2. **Two Player Mode:** Two human players compete against each other.

The game provides a simple interface to enjoy Tic-Tac-Toe and allows for endless fun and practice.

---

### Features
- **Single Player Mode:** Play against a computer opponent with randomly chosen moves.
- **Two Player Mode:** Play against a friend locally.
- **User-Friendly Interface:** Simple grid display to understand the current state of the game.
- **Win and Tie Detection:** Automatically determines the winner or if the game ends in a tie.
- **Replay Support:** Easily restart the program to play again.

---

### Prerequisites
- **Python Installed:** Ensure Python 3.6 or higher is installed on your system.

---

### Requirements
- Operating System: Windows, macOS, or Linux
- Python Version: Python 3.6 or above
- No external libraries required (uses only standard Python libraries)

---

### Using the Program

1. **Run the Program:**
   Execute the script using the command:
   ```bash
   python tictactoe.py
   ```

2. **Select Game Mode:**
   - Enter `1` for Single Player Mode (You vs. Computer).
   - Enter `2` for Two Player Mode (Player 1 vs. Player 2).

3. **Input Moves:**
   - Each cell on the board is represented by a number from `1` to `9`:
     ```
      1 | 2 | 3
     ---+---+---
      4 | 5 | 6
     ---+---+---
      7 | 8 | 9
     ```
   - Enter the corresponding number to make your move.

4. **Game Progress:**
   - The board will update after each move.
   - A message will display the winner or if the game ends in a tie.

5. **Replay:**
   - Restart the script to play again.

---

### Sample Inputs and Outputs

#### Example 1: Single Player Mode
```
Select game mode (1 for single player, 2 for two players): 1
   |   |   
---+---+---
   |   |   
---+---+---
   |   |   
X's turn. Enter your move (1-9): 5
   |   |   
---+---+---
   | X |   
---+---+---
   |   |   
Computer wins!
```

#### Example 2: Two Player Mode
```
Select game mode (1 for single player, 2 for two players): 2
   |   |   
---+---+---
   |   |   
---+---+---
   |   |   
X's turn. Enter your move (1-9): 1
 X |   |   
---+---+---
   |   |   
---+---+---
   |   |   
O's turn. Enter your move (1-9): 2
 X | O |   
---+---+---
   |   |   
---+---+---
   |   |   
Player 1 wins!
```

---

Enjoy the classic Tic-Tac-Toe game in the terminal!
