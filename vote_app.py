from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# A secret key is still needed for Flask's flash messaging system, even without user sessions.
app.secret_key = 'your_strong_secret_key_here_replace_me_with_a_real_one' 

# In-memory storage for candidates and votes
CANDIDATES = ["Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Miller", "Eve Davis"] 
VOTES = [] 

# --- Routes ---

@app.route('/')
def home():
    """
    The home page of the application. For this independent voting module,
    we simply redirect to the voting page.
    """
    return redirect(url_for('vote'))

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    """
    Handles the display and submission of the ranked-choice voting form.

    GET Request:
        Displays the voting form with all available candidates.
    
    POST Request:
        Processes the submitted vote with updated validation rules:
        1. Extracts user preferences from the form.
        2. Validates:
            - First preference is mandatory and valid.
            - All submitted preferences (optional or not) are valid candidates.
            - All submitted preferences are unique.
        3. If valid, stores the vote in the in-memory VOTES list.
        4. Renders the confirmation page, showing the user their specific preferences.
        5. If invalid, re-renders the voting form with an error message.
    """
    # Your code goes here to implement the logic for GET and POST requests.
    # On GET: return render_template('vote.html', candidates=CANDIDATES)
    # On POST (validation failed): return render_template('vote.html', candidates=CANDIDATES, error=error_message)
    # On POST (validation successful): return render_template('voted_confirmation.html', user_vote=user_preferences_dict)
    
    if request.method == 'GET':
        return render_template('vote.html', candidates=CANDIDATES)
    raw = []
    for i in range(1, 6):
        v = request.form.get(f'pref{i}')
        raw.append(v if v and v.strip() else None)
    if not raw[0]:
        error = "Please select your 1st preference."
        return render_template('vote.html',candidates=CANDIDATES, error=error)
    selected = []
    for rank, name in enumerate(raw, start=1):
        if name:
            selected.append((rank, name))
    for rank, name in selected:
        if name not in CANDIDATES:
            error = f"Invalid candidate selected for choice #{rank}."
            return render_template('vote.html',candidates=CANDIDATES, error=error)
    names = [name for _, name in selected]
    if len(names) != len(set(names)):
        error = "You may not select the same candidate more than once."
        return render_template('vote.html',candidates=CANDIDATES, error=error)
    user_vote = {
        f"{i}. Preference": raw[i-1] or ""
        for i in range(1, 6)
    } 
    VOTES.append(user_vote)
    flash("Your vote has been recorded successfully!","success")
    return render_template('voted_confirmation.html',user_vote=user_vote)

if __name__ == '__main__':
    app.run(debug=True)
