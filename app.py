from flask import Flask


app = Flask(__name__)



@app.route("/")
def lw():
    return "Hello There I am Pushpendra"


app.run(host='0.0.0.0')



