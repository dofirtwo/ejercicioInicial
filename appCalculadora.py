from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def calculadora():
    return render_template("calculadoraJS.html")

@app.route("/sumar",methods=["POST"])
def sumar():
    n1= float(request.form["txtNum1"])
    n2 = float(request.form["txtNum2"])
    resultado = n1+n2
    return jsonify({"Resultado":resultado,"Estado":True})
@app.route("/restar",methods=["POST"])
def restar():
    n1= float(request.form["txtNum1"])
    n2 = float(request.form["txtNum2"])
    resultado = n1-n2
    return jsonify({"Resultado":resultado,"Estado":True})
@app.route("/multiplicar",methods=["POST"])
def multiplicar():
    n1= float(request.form["txtNum1"])
    n2 = float(request.form["txtNum2"])
    resultado = n1*n2
    return jsonify({"Resultado":resultado,"Estado":True})
@app.route("/dividir",methods=["POST"])
def dividir():
    n1= float(request.form["txtNum1"])
    n2 = float(request.form["txtNum2"])
    resultado = n1/n2
    return jsonify({"Resultado":resultado,"Numero2":n2,"Estado":True})



if __name__ == "__main__":
    app.run(port=3000, debug=True)