import mysql.connector
from flask import Flask


mydb=mysql.connector.connect(
host='localhost',
user='root',
password='root',
database='faculdade'
)

app = Flask(__name__)




@app.route('/curso', methods= ['GET'])
def get_universidade():
    my_cursor=mydb.cursor()
    my_cursor.execute('select * from cursos')
    universidade=my_cursor.fetchall()
    return universidade

app.run()