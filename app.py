import os  # Add this import statement at the top of your file

from flask import Flask, render_template

app = Flask(__name__)

# Python function you want to use in HTML
def greet_user(name):
    return f"Hello, {name}! Welcome to my website."

@app.route('/')
def home():
    name = "Alice"  # You can dynamically get this from input later
    greeting_message = greet_user(name)  # Call the Python function
    return render_template('index.html', greeting=greeting_message)  # Pass result to HTML

if __name__ == '__main__':
    # Make sure Flask listens on the correct host and port
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
