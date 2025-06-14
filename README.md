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
