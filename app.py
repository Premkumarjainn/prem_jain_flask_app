
import os
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to show all users
@app.route('/users')
def users():
    conn = sqlite3.connect('database.db')        # Connect to DB
    cursor = conn.cursor()                       # Create cursor
    cursor.execute("SELECT * FROM users")        # Get all users
    all_users = cursor.fetchall()                # Fetch all rows
    conn.close()                                 # Close connection
    return render_template('list.html', users=all_users)

# Route to handle form submission (inserts new user)
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Save to database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return redirect('/users')  # Redirect to user list

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
