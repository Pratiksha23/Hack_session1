from flask import Flask
from flask import render_template,jsonify
app = Flask(__name__)
name = "dat"

@app.route("/")
def hello():
    return "Hi I am Mangesh"

#pori is variable
@app.route("/user=<pori>")
def user(pori):
    return render_template("profile.html", name=pori) # 'pori' is passed to 'name'(next process will be in templetes/profile.html)
    return"Hello  This is second page dear "+pori



@app.route("/lotofdata")
def age():
    my_bap = {'neha': 60,
              'pratiksha' : 85,
               'kaka': 5 }
    return jsonify(my_bap)
app.run(debug = True , host='0.0.0.0', port=5000)
