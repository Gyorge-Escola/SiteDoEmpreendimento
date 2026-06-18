from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/multiplicar", methods=["POST"])
def multiplicar():
    data = request.json
    resultado = data["a"] * data["b"]
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)