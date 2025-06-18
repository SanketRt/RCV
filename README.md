# Ranked-Choice Voting System

A small suite of Python tools demonstrating:

1. **User Authentication & Session Management** (Flask)  
2. **Ranked-Choice Voting Web Interface** (Flask)  
3. **Command-Line RCV Vote Counter Simulator** (SQLite + CLI)  
4. **RCV Tallying Algorithms** (Pure Python)

---

## Table of Contents

1. [Features](#features)  
2. [Tech Stack & Requirements](#tech-stack--requirements)  
3. [Project Layout](#project-layout)  
4. [Installation](#installation)  
5. [Usage](#usage)  
   - [Web App: Authentication + Voting](#web-app-authentication--voting)  
   - [CLI RCV Simulator](#cli-rcv-simulator)  
   - [RCV Algorithms (Library)](#rcv-algorithms-library)  
6. [Examples](#examples)  


---

## Features

- **Flask-based Login & Registration**  
  - In-memory user store  
  - Password hashing with Werkzeug  
  - Session-backed "login_required" decorator  

- **Flask-based Ranked-Choice Voting Form**  
  - 1st preference required, 2nd–5th optional  
  - Validation: mandatory first choice, unique entries, valid candidates  
  - Confirmation page with flash messages  

- **CLI Vote Counter Simulator**  
  - SQLite backend for storing ballots  
  - Interactive prompt to enter comma-separated ranked ballots  
  - Fetch & display all stored ballots  

- **RCV & Plurality Tally Functions**  
  - `calculate_rcv_winner(ballots)`: elimination-style RCV winner  
  - `count_first_choices(ballots)`: simple plurality count  

---

## Tech Stack & Requirements

- **Language**: Python 3.8+  
- **Web Framework**: Flask  
- **Database**: SQLite (for CLI simulator)  
- **Templating**: Jinja2 (bundled with Flask)  

Install dependencies with:

```bash
pip install Flask
```

## Project Layout

```text
.
├── auth_app.py              # Flask app: login/register/logout + placeholder vote
├── vote_app.py              # Flask app: full ranked-choice voting module
├── run_app.py               # Entry point that wires together auth_app.py and vote_app.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── vote.html
│   └── voted_confirmation.html
├── static/
│   └── style.css
├── rcv_cli.py               # CLI RCV simulator (init_db, add_ballot, fetch_ballots)
├── ballots.db               # SQLite database for CLI simulator (auto-generated)
├── rcv_winner.py            # RCV elimination-style tally function
└── first_choice_count.py    # Simple plurality (first-choice) tally function
```

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/SanketRt/RCV.git
   cd rcv-system
   ```

2. **Create a virtual environment & install dependencies**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install Flask
   ```

---

## Usage

### Web App: Authentication + Voting

#### Authentication & Placeholder Vote

```bash
export FLASK_APP=auth_app.py
export FLASK_ENV=development
flask run
```

- Visit `http://127.0.0.1:5000`
- Register a new account, log in, then land on the placeholder vote page

#### Full RCV Voting Module

```bash
export FLASK_APP=vote_app.py
export FLASK_ENV=development
flask run
```

- Visit `http://127.0.0.1:5000/vote`
- Fill out 1st–5th preferences (1st required, others optional)
- Submit to see confirmation and success banner

#### Combined Application

```bash
export FLASK_APP=run_app.py
export FLASK_ENV=development
flask run
```

- Access both authentication and voting features in one unified application
- Complete user flow from registration → login → voting → confirmation

### CLI RCV Simulator

```bash
python rcv_cli.py
```

- Enter ballots one at a time (comma-separated), e.g.:

```
Ballot: Alice Smith, Bob Johnson, Charlie Brown
Ballot: Diana Miller
Ballot: done
```

- The script will print back the stored ballots list
- All ballots are stored in `ballots.db` SQLite database

### RCV Algorithms (Library)

Use the RCV and plurality counting functions in any Python script or REPL:

```python
from rcv_winner import calculate_rcv_winner
from first_choice_count import count_first_choices

# Sample ballots data
ballots = [
    ["Alice Smith", "Charlie Brown"],
    ["Bob Johnson", "Eve Davis"],
    ["Alice Smith"],
    ["Charlie Brown", "Alice Smith", "Bob Johnson"]
]

# Get plurality (first-choice) count
plurality_results = count_first_choices(ballots)
print("Plurality Results:", plurality_results)
# Output: {'Alice Smith': 2, 'Bob Johnson': 1, 'Charlie Brown': 1}

# Calculate RCV winner using elimination rounds
rcv_winner = calculate_rcv_winner(ballots)
print("RCV Winner:", rcv_winner)
# Output: Alice Smith (after elimination rounds)
```

---

## Examples

### Web Interface Examples

- **Full Web Vote**: All five preferences selected → confirmation shows all five + success banner
- **Partial Web Vote**: Only 1st & 3rd selected → confirmation shows those two + success banner
- **Authentication Flow**: Register → Login → Vote → Logout

### CLI Examples

**Interactive Ballot Entry:**
```bash
$ python rcv_cli.py
Enter ballots (comma-separated candidates, 'done' to finish):
Ballot: Alice Smith, Bob Johnson, Charlie Brown
Ballot: Diana Miller, Alice Smith
Ballot: Bob Johnson
Ballot: done

Stored ballots:
1. ['Alice Smith', 'Bob Johnson', 'Charlie Brown']
2. ['Diana Miller', 'Alice Smith']
3. ['Bob Johnson']
```

### Algorithm Examples

**RCV Elimination Process:**
```python
ballots = [
    ["A", "B", "C"],
    ["B", "C", "A"],
    ["C", "A", "B"],
    ["A", "C", "B"]
]

# Round 1: A=2, B=1, C=1 → B eliminated
# Round 2: A=2, C=2 → Continue with remaining votes
# Winner determined through elimination process
```

---

## Project Structure Details

### Core Components

- **`auth_app.py`**: Handles user registration, login, logout, and session management
- **`vote_app.py`**: Manages the ranked-choice voting interface and ballot submission
- **`run_app.py`**: Combines both applications for a complete user experience
- **`rcv_cli.py`**: Command-line interface for ballot collection and storage
- **`rcv_winner.py`**: Implements the RCV elimination algorithm
- **`first_choice_count.py`**: Provides simple plurality vote counting

### Templates & Static Files

- **Templates**: Jinja2 templates for all web pages (login, register, vote, confirmation)
- **Static**: CSS styling for consistent web interface appearance

### Database

- **`ballots.db`**: SQLite database automatically created for CLI ballot storage

---

## Development Notes

### Running in Development Mode

Set `FLASK_ENV=development` to enable:
- Auto-reloading on code changes
- Enhanced error messages
- Debug mode features

### Security Considerations

- Uses Werkzeug for password hashing
- Session-based authentication
- CSRF protection through Flask's built-in features
- Input validation for ballot submissions

### Extending the System

The modular design allows for easy extension:
- Add new voting algorithms to the library components
- Extend the web interface with additional features
- Integrate with external databases or authentication systems
- Add API endpoints for programmatic access

---
