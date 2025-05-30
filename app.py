from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)
with app.app_context():
    db.create_all()

@app.route("/" , methods= ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        c = Contact(
            name = request.form['name'],
            email = request.form['email'],
            message = request.form['message']
            )
        db.session.add(c)
        db.session.commit()
        return "message sent!"

    
    
    
    return render_template("contact.html")

app.run(debug=True)