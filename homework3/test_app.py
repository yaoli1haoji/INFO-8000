from flask import Flask,escape, request,jsonify 
import sqlite3


app = Flask(__name__)

DATABASE = './assignment3.db'


def connect_db():
    db =sqlite3.connect('assignment3.db')
    return db
    

    
@app.route('/',methods=['GET','POST'])

def fun():
    name = request.args.get("name","World")
    response = {"name":name}
    return jsonify(response)

@app.route('/create_default_experiment')

def create_experiment(
):
    conn = connect_db()
    conn.execute("""
    DROP TABLE IF EXISTS experiment
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS experiment (crop TEXT,experiment_ID INT,treatment TEXT,PRIMARY KEY('experiment_ID'));
    """)
    conn.execute("INSERT INTO experiment VALUES ('maize',1,'living_mulch')")
    conn.execute("INSERT INTO experiment VALUES ('maize',2,'CrimsonClover')")
    conn.execute("INSERT INTO experiment VALUES ('maize',3,'CerealRye')")
    conn.execute("INSERT INTO experiment VALUES ('maize',4,'Nocover')")
    cur = conn.execute("""SELECT * from experiment""")
    experiment_list = [dict(crop=row[0],experiment_ID=row[1],treatment=row[2]) for row in cur]
    data = jsonify(experiment_list)
    return data 

@app.route('/add_experiment/')

def add_experiment(
):
    crop = request.args.get("crop","submit a crop name")
    experiment_id = request.args.get("experiment_id","submit a experiment_id")
    treatment = request.args.get("treatment","submit a treatment")
    conn = connect_db()
    conn.execute("INSERT INTO experiment VALUES ('crop','experiment_id','treatment')")
    cur = conn.execute("""SELECT * from experiment""")
    experiment_list = [dict(crop=row[0],experiment_ID=row[1],treatment=row[2]) for row in cur]
    data = jsonify(experiment_list)
    return data 