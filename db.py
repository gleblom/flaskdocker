from flask import Flask, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
import requests
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1488@localhost:5432/postgres'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Machine(db.Model):
    __tablename__ = 'Machine'
    MachineID = db.Column(db.Integer, primary_key = True)
    Machine = db.Column(db.Text)

class Material(db.Model):
    __tablename__ = 'Material'
    MaterialID = db.Column(db.Integer, primary_key = True)
    Material = db.Column(db.Text)


class MachineMaterial(db.Model):
    __tablename__ = 'MachineMaterial'
    ID = db.Column(db.Integer, primary_key = True)
    MachineID = db.Column(db.Integer, db.ForeignKey('Machine.MachineID'))
    MaterialID = db.Column(db.Integer, db.ForeignKey('Material.MaterialID'))

@app.route('/')
@app.route('/Machine', methods = ['GET', 'POST'])
def Add_Machine():
    req1 = request.json.get("MachineID")
    req2 = request.json.get("Machine")
    if request.json.get('MachineID') is None or request.json.get('Machine') is None:
        print(req1, req2, 111111111111111)
    else:
        mch = Machine(MachineID = req1, Machine = req2)
        db.session.add(mch)
        db.session.commit()
        print(Machine.query.all())
    return make_response('ok', 200)
    
if __name__ == '__main__':
    app.run(host='192.168.1.64')

    
    
    
