from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
from functools import wraps


app = Flask(__name__)
# IMPORTANT: For production, use a strong, fixed secret key from an environment variable.
# For this contest, os.urandom(24) is fine for session management during development.
app.secret_key = os.urandom(24) 

# --- Server-Side "Local Storage" (In-Memory Data) ---
# This dictionary will store our user accounts in memory.
# Format: {'username': {'password_hash': '...', 'voted': False}}
USERS = {}

# --- Helper Functions (Provided for convenience) ---

def login_required(f):
    """
    Decorator to ensure a user is logged in before accessing certain routes.
    If not logged in, it flashes a message and redirects to the login page.
    """
    @wraps(f)
    def decorator(*args,**kwargs):
        if 'username' not in session:
            flash('You must be logged in.','warning')
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return decorator
    

# --- Routes (Your main task is to complete these!) ---

@app.route('/')
def index():
    """
    Default route: Should redirect to the login page.
    """
    # TODO: Implement redirect to login page
    if 'username' in session:
        return redirect(url_for('vote'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login route:
    - On GET request: Display the login form.
    - On POST request:
        - Get username and password from the form.
        - Check if username exists in USERS.
        - If yes, verify password using check_password_hash.
        - If credentials are valid:
            - Store username in session.
            - Flash a success message.
            - Redirect to a placeholder logged-in page (e.g., '/').
        - If credentials are invalid:
            - Flash an error message.
            - Re-render the login form.
    - If user is already logged in (username in session), redirect them to the logged-in page.
    """
    # TODO: Implement login logic
    if 'username' in session:
        flash(f"You're already logged in as {session['username']}.",'info')
        return redirect(url_for('vote'))
    if request.method=='POST':
        username=request.form.get('username','').strip()
        password=request.form.get('password','')
        user=USERS.get(username)
        if user and check_password_hash(user['password_hash'],password):
            session['username']=username
            flash(f"Welcome back, {username}!", 'success')
            return redirect(url_for('vote'))
        else:
            flash('Invalid username or password.', 'danger')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register route:
    - On GET request: Display the registration form.
    - On POST request:
        - Get username and password from the form.
        - Validate input (e.g., not empty).
        - Check if username already exists in USERS.
        - If username is new and valid:
            - Hash the password using generate_password_hash.
            - Store the new user in USERS (username, hashed password, and 'voted': False).
            - Flash a success message.
            - Redirect to the login page.
        - If validation fails or username exists:
            - Flash an appropriate error message.
            - Re-render the registration form.
    - If user is already logged in (username in session), redirect them to the logged-in page.
    """
    # TODO: Implement registration logic
    if 'username' in session:
        flash(f"You are already registered and logged in as {session['username']}.",'info')
        return redirect(url_for('vote'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            flash('Username and password cannot be empty.','warning')
            return render_template('register.html')

        if username in USERS:
            flash('That username is already taken. Please choose another.','warning')
            return render_template('register.html')

        pw_hash = generate_password_hash(password)
        USERS[username] = {'password_hash': pw_hash,'voted': False}
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
@login_required # This decorator ensures only logged-in users can access this.
def logout():
    """
    Logout route:
    - Remove 'username' from session.
    - Flash an info message.
    - Redirect to the login page.
    """
    # TODO: Implement logout logic
    user = session.pop('username', None)
    flash(f'Goodbye, {user}! You have been logged out.','info')
    return redirect(url_for('login'))


# --- Placeholder for a route that a logged-in user would see ---
# This 'vote' route is here just to provide a valid redirect target for login.
@app.route('/vote')
@login_required
def vote():
    """
    Placeholder route for logged-in users.
    In Part 2, this will become the actual voting interface.
    """
    return render_template('base.html', content="<p>Welcome to the voting page! (Content for Part 2)</p>")


if __name__ == '__main__':
    app.run(debug=True) # debug=True makes the server reload on code changes