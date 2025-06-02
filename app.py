from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(100), default='No Subject')
    message = db.Column(db.Text)
with app.app_context():
    db.create_all()

@app.route("/" , methods= ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        c = Contact(
            name = request.form['name'],
            email = request.form['email'],
            subject = request.form['subject'],
            message = request.form['message']
            )
        db.session.add(c)
        db.session.commit()
        return "Thank you for your message!"

    
    
    
    return render_template("contact.html")
@app.route("/home")
def home():
    return render_template("index.html")
app.run(debug=True)