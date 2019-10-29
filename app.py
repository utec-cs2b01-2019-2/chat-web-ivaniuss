from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
import psycopg2


app = Flask(__name__)
ENV = 'dev'



'''
ENV = 'prod'
'''
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ivanxD9494xD@localhost/p1-web'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rexpoeydjvqqpt:9dbf8236bddda6b5e704fef6f0b1ce6c0d45df60dd4d03511dc5c8751a123ed2@ec2-174-129-252-226.compute-1.amazonaws.com:5432/d20v915npeo4ga'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#creando nuevo usuario

class User(db.Model):
    __tablename__ = 'users'
    
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


class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(200))
    nombre = db.Column(db.String(200),unique=True)
    estado = db.Column(db.Integer)
    mail = db.Column(db.String(200),unique=True)
    descripcion = db.Column(db.Text())
    
    def __init__(self, tipo, nombre, estado, mail,descripcion):
        self.tipo = tipo
        self.nombre = nombre
        self.estado = estado
        self.mail = mail
        self.descripcion = descripcion


@app.route('/editUser',methods=['POST'])
def editUser():
    print(userId)
    connection = psycopg2.connect (user="postgres",
                                       password="ivanxD9494xD",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="p1-web")
    cursor = connection.cursor ()
    postgreSQL_select_Query = "select * from users"

    cursor.execute (postgreSQL_select_Query)
    print ("Selecting rows from users table using cursor.fetchall")
    users = cursor.fetchall ()

    print ("Print each row and it's columns values")
    print(uuser,ppass)


    for fila in range (len (users)):
        if users[fila][1] == uuser and users[fila][2] == ppass:
            user = (users[fila][1])
            password = (users[fila][2])
            name = (users[fila][3])
            lastname = (users[fila][4])




    return render_template('editUser.html', username=user,password=password,name=name,lastname=lastname)




'''
    finally:
        # closing database connection.
        if (connection):
            cursor.close ()
            connection.close ()
            print ("PostgreSQL connection is closed")
'''

'''
def insertTable():
   
    connection = psycopg2.connect (user="postgres",
                                       password="ivanxD9494xD",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="p1-web")

    cursor = connection.cursor ()
    username=request.form()
    postgres_insert_query = """ INSERT INTO users (id, username, password, name, lastname) VALUES (%s,%s,%s,%s,%s)"""
    record_to_insert = (9, 'One Plus 6', "950","r","f")
    cursor.execute (postgres_insert_query, record_to_insert)

    connection.commit ()
    count = cursor.rowcount
    print (count, "Record inserted successfully into usuario table")

    

    finally:
        # closing database connection.
        if (connection):
            cursor.close ()
            connection.close ()
            print ("PostgreSQL connection is closed")
'''
@app.route('/update',methods=['POST'])
def updateTable():


    connection = psycopg2.connect (user="postgres",
                                       password="ivanxD9494xD",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="p1-web")

    cursor = connection.cursor ()

    if request.method == 'POST':

        password = request.form['password']

    sql_select_query = """select * from users where id = %s"""
    cursor.execute (sql_select_query, (userId,))
    record = cursor.fetchone ()
    print (record)

    # Update single record now
    sql_update_query = """Update users set password = %s where id = %s"""
    cursor.execute (sql_update_query, (password,userId))
    connection.commit ()
    count = cursor.rowcount
    print (count, "Record Updated successfully ")
    return "updated"


@app.route('/delete',methods=['POST'])
def delete():


    connection = psycopg2.connect (user="postgres",
                                       password="ivanxD9494xD",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="p1-web")

    cursor = connection.cursor()

    # Update single record now
    sql_delete_query = """Delete from users where id = %s"""
    cursor.execute(sql_delete_query, (userId,))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")
    return "succeed"




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

        if username == '' or password == '' or name == '' or lastName == '':
            return render_template('newUser.html', message='Please enter required fields')


        if db.session.query(User).filter(User.username == username).count() == 0:
            data = User(username, password, name, lastName) 
            db.session.add(data)
            db.session.commit()
            
            return render_template('success.html')
        return render_template('newUser.html', message='This username already exists')




@app.route ('/login', methods=['POST'])
def login():
    global uuser
    global ppass
    global userId

    connection = psycopg2.connect (user="postgres",
                                   password="ivanxD9494xD",
                                   host="127.0.0.1",
                                   port="5432",
                                   database="p1-web")
    cursor = connection.cursor ()
    postgreSQL_select_Query = "select * from users"

    cursor.execute (postgreSQL_select_Query)
    print ("Selecting rows from users table using cursor.fetchall")
    users = cursor.fetchall ()

    print ("Print each row and it's columns values")

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == '' or password == '':
            return render_template ('login.html', message='Please enter required fields')

        else:
            for columna in range(len(users)):
                if users[columna][1] == username and users[columna][2] == password:

                    userId = users[columna][0]

                    uuser = username
                    ppass = password

                    return render_template('book.html')

            return render_template('login.html',message='Enter a valid user or password')

@app.route ('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        tipo = request.form['tipo']
        nombre = request.form['namebook']
        estado = request.form['estado']
        descripcion = request.form['descripcion']
        mail = request.form['mail']
        
        if nombre == '' or descripcion == '' or tipo == '' or mail == '':
            return render_template ('book.html', message='Please enter required fields')

        if db.session.query (Book).filter (Book.nombre == nombre).count () == 0:
            data = Book (tipo, nombre, estado, descripcion, mail)
            db.session.add (data)
            db.session.commit()
            send_mail(tipo, nombre, estado, mail, descripcion)
            return "solicitud creada, le contactaremos a traves de su correo"
        return render_template ('book.html', message='This name already exists')


if __name__ == '__main__':
    app.run()

