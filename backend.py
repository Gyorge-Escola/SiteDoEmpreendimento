from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def soma(a, b):
    return a + b

@app.route("/api/soma")
def rota_soma():
    resultado = soma(2, 3)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)