from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to website</p>"

@app.route("/log in")
def login():
    return(render_template("login.html"))

@app.route("/sign up")
def signup():
    return(render_template("signup.html"))

@app.route("/home")
def home():
    return(render_template("home.html"))

if __name__ == '__main__':
    app.run(debug=True)