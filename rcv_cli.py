import sqlite3
from typing import List

DB_FILE = "ballots.db"

def init_db():
    # Complete the code
    con=sqlite3.connect(DB_FILE)
    cursor=con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ballots(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ranking TEXT
    )
    """)
    con.commit()
    con.close()
    


def add_ballot(ranking):
    # Complete the code
    rk=""
    l=len(ranking)
    if l>0: rk+=ranking[0]
    for i in range(1,l):
        rk+=","
        rk+=ranking[i]
    if ranking is None: return
    
    con=sqlite3.connect(DB_FILE)
    cursor=con.cursor()
    cursor.execute(
        "INSERT INTO ballots (ranking) VALUES (?)", (rk,)
    )
    con.commit()
    con.close()
    





def fetch_ballots():
    # Complete the code
    con=sqlite3.connect(DB_FILE)
    cursor=con.cursor()
    cursor.execute("SELECT ranking FROM ballots")
    rows = cursor.fetchall()
    b: List[List[str]] = []
    for (ranking_str,) in rows:
        if ranking_str:
            b.append(ranking_str.split(","))
        else:
            b.append([])

    con.commit()
    con.close()
    return b

    


def get_ballots_from_user():
    print("Welcome to the RCV Vote Counter Simulator!")
    print("Enter ranked ballots (comma-separated). Type 'done' to finish.\n")

    while True:
        entry = input("Ballot: ").strip()
        if entry.lower() == "done":
            break
        if entry:
            ranking = [name.strip() for name in entry.split(",") if name.strip()]
            if ranking:
                add_ballot(ranking)
            else:
                print("Invalid ballot. Please enter at least one candidate.")

def main():
    init_db()
    get_ballots_from_user()
    ballots = fetch_ballots()

    print(ballots)

if __name__ == "__main__":
    main()