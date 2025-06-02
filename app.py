from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Set up the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(100), default='No Subject')
    message = db.Column(db.Text)

# Create the database file if it doesn't exist
with app.app_context():
    if not os.path.exists('contact.db'):
        db.create_all()

@app.route("/", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        c = Contact(
            name=request.form['name'],
            email=request.form['email'],
            subject=request.form['subject'],
            message=request.form['message']
        )
        db.session.add(c)
        db.session.commit()
        return "Thank you for your message!"

    return render_template("contact.html")

@app.route("/home")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
