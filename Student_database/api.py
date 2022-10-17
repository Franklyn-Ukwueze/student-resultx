from studentdb import add_new_student, find_student, update_score
from flask import Flask, request


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Welcome to your student database."

@app.route("/register")
def register():
    return add_new_student()

@app.route("/student search")
def student_search():
    return find_student()

@app.route("/score update")
def score_update():
    return update_score()
    
app.run()