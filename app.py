import json
from flask import Flask, jsonify, render_template
app = Flask(__name__, template_folder='template')

employee = [
    {'id':1, 'name':"joshua", 'age':"24"},
    {'id':1, 'name':"adewale", 'age':"64"}
]
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/', methods=['GET'])
def hello_world(): 
    return 'Hello world!'

@app.route('/employee')
def get_employee():
    return jsonify(employee)


if __name__ == '__main___':
    app.run(port=400)
