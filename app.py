from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '624545123'
app.config['MYSQL_DB'] = 'ordering'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer")
    records = cur.fetchall()

    return render_template('index.html',records=records)

    #return str(records)

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    contact = request.form['contact']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO customer (name,email,address,phone) VALUES (%s,%s,%s,%s)",(name,email,address,contact))
    mysql.connection.commit()
    cur.close()

    return "INSERTED SUCCESSFULLY"

app.run(debug=True)