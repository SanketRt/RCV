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
7. [License](#license)  

---

## Features

- **Flask-based Login & Registration**  
  - In-memory user store  
  - Password hashing with Werkzeug  
  - Session-backed “login_required” decorator  

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
   git clone https://github.com/youruser/rcv-system.git
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

### 1. Web Application

#### Authentication & Placeholder Vote

```bash
export FLASK_APP=auth_app.py
export FLASK_ENV=development
flask run
```
Visit `http://127.0.0.1:5000`

Register a new account, log in, then land on the placeholder vote page.

#### Full RCV Voting Module

```bash
export FLASK_APP=vote_app.py
export FLASK_ENV=development
flask run
```



