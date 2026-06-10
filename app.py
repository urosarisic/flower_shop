from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/buketi")
def buketi():
    return render_template("buketi.html")

@app.route("/test")
def test():
    return "OVO JE TEST"

if __name__ == "__main__":
    app.run(debug=False)