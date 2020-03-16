from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def getIndex():
    return render_template("index.html",hello = "Hello World")

if __name__ == "__main__":
    app.run(host='localhost', port = 5000, debug=True)