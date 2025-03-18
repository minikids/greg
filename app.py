import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Python function you want to use in HTML
def greet_user(name):
    return f"Hello, {name}! Welcome to my website."

@app.route('/', methods=['GET', 'POST'])  # Allow both GET and POST requests
def home():
    greeting_message = ""
    if request.method == 'POST':
        name = request.form.get('name')  # Get user input from the form
        greeting_message = greet_user(name)  # Call Python function with user input
    
    return render_template('index.html', greeting=greeting_message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
