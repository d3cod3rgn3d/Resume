from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set the secret key for your Flask application
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Process form data (e.g., save to database, send email, etc.)
        # For demonstration purposes, let's just print the data
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # Redirect user to the submit_form.html template
        return redirect(url_for('submit_form'))

@app.route('/submit_form')
def submit_form_page():
    return render_template('submit_form.html')


if __name__ == '__main__':
    app.run()
