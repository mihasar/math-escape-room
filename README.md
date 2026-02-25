```markdown
# Math Escape Room (OOP Final Project)

A small "escape room" game built for the OOP course, using an MVC-style structure with a local SQLite database for saving scores.

## Features
- CLI Game Mode: Play directly in the terminal.
- Pygame Game Mode: Play using a graphical user interface (GUI).
- Scoreboard: Player scores and mistakes are saved locally to a SQLite database (`database/escape_room.db`).
- MVC Architecture:
  - `models/` – Puzzles and core game logic.
  - `views/` – CLI and Pygame user interfaces.
  - `controllers/` – Game flow orchestration and REPL menu.
  - `database/` – DBManager for SQLite operations.

## Requirements
- Python 3.x
- Pygame (required only for GUI mode)

### Installation
To install the required dependencies for the GUI mode, run:
```bash
pip install pygame

```

## How to Run

From the project root directory, execute the main script:

```bash
python main.py

```

## Menu Options

1. Play (CLI)
2. Play (Pygame)
3. Show Scores
4. Change Player Name
5. Reset Scores
6. Exit

## Notes

* The SQLite database file is automatically created and used at: `database/escape_room.db`.
* If you plan to run the GUI mode (Option 2), make sure the `pygame` library is installed.
