from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html") #render_template is used to redirect the linke to the html file instead of just typing words in "".

@app.route("/<name>")
def say_hello_to(name):
    return f"Hello {name}"

app.run(debug=True)