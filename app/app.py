from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:9192/postgres'
db = SQLAlchemy(app)

class People(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(25), nullable=False) 
   age = db.Column(db.Integer, nullable=False)
   
   def to_json(self):
       return {
           "name": self.name,
           "age": int(self.age)
       }
        
validate_data = ["name", "age"]

db.create_all()

@app.route('/get_users')
def index():
    people = People.query.all()
    return jsonify({"users": [x.to_json() for x in people]})

@app.route('/post_people', methods=['POST'])
def post_people():
    content = json.loads(request.data)
    if content:
        verify_data = [data for data in validate_data if data in content.keys()]
        if validate_data == verify_data:
            people = People(name=content['name'], age=content['age'])
            db.session.add(people)
            db.session.commit()
        else:
            data = {'Error': 'it was not possible to register the person'}
            return jsonify(data), 500