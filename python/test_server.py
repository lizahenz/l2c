from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#@app.route("/add/<int:a>/<int:b>/")
@app.route("/add/<int:a>/<b>/")
def add_2(a,b):
      return a + b

if __name__ == "__main__":
    app.run()
