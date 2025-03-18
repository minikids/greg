from flask import Flask, render_template, request

app = Flask(__name__)

def greet_user(name):
    return f"Hello, {name}! Welcome to my website."

@app.route('/', methods=['GET', 'POST'])
def home():
    greeting_message = ""
    if request.method == 'POST':
        name = request.form.get('name')  # Get name from form
        greeting_message = greet_user(name)  # Call Python function with user input
    return render_template('index.html', greeting=greeting_message)

if __name__ == '__main__':
    app.run(debug=True)
