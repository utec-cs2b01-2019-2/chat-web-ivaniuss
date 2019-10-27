from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ivanxD9494xD@localhost/p1-web'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ' postgres://vojjnsvxcwetvd:62b4e0c6afd308a1fb6e23ecc7a8fe06bffea66cd9d76e68085c81503ff02e7e@ec2-54-221-244-70.compute-1.amazonaws.com:5432/d29s30e26o80r0'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#creando nuevo usuario

class newUser(db.Model):
    __tablename__ = 'newUser'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200), unique=True)
    name = db.Column(db.String(200), unique=True)
    lastName = db.Column(db.String(200), unique=True)
    
    def __init__(self, username, password, name, lastName):
        self.username = username
        self.password = password
        self.name = name
        self.lastName = lastName


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/submit', methods=['POST'])
def submit():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        lastName = request.form['lastName']
        print(username,password,name,lastName)
        if username == '' or password == '' or name == '' or lastName == '':
            return render_template('newUser.html', message='Please enter required fields')


        if db.session.query(newUser).filter(newUser.username == username).count() == 0:
            data = newUser(username, password, name, lastName) 
            db.session.add(data)
            db.session.commit()
 #           send_mail(username, password, name, lastName)
            return render_template('success.html')
        return render_template('newUser.html', message='This username already ex')


if __name__ == '__main__':
    app.run()

