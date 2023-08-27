from flask import Flask, request, render_template

app = Flask(__name__)

personas = []

@app.route("/")
def inicio():
    #return "Hola y tal"
    mensaje ="Bienvenido al desarrollo de aplicaciones Web"
    return render_template("bienvenido.html", mensaje=mensaje)

@app.route("/tablas")
def mostrarTabla():
    personas.clear()
    personas1=["pedro","picapiedras","@gmail.com"]
    personas2=["pedro2","picapiedras2","@gmail.com2"]
    personas.append(personas1)
    personas.append(personas2)
    return render_template("tabla.html",personas=personas)

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"hola {nombre}"

@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")

@app.route("/operaciones",methods=["POST"])
def operaciones():
    if request.method=="POST":
        d=(None,None,None)
        accion= request.form["btnAccion"]
        if (accion == "sumar"):
            n1= float(request.form["txtNum1"])
            n2 = float(request.form["txtNum2"])
            resultado = n1+n2
            d=(n1,n2,resultado)
            
        elif (accion == "restar"):
            n1= float(request.form["txtNum1"])
            n2 = float(request.form["txtNum2"])
            resultado = n1-n2
            d=(n1,n2,resultado)
           
        elif (accion == "multiplicar"):
            n1= float(request.form["txtNum1"])
            n2 = float(request.form["txtNum2"])
            resultado = n1*n2
            d=(n1,n2,resultado)
            
        elif (accion == "dividir"):
            n1= float(request.form["txtNum1"])
            n2 = float(request.form["txtNum2"])
            resultado = n1//n2
            d=(n1,n2,resultado)
        return render_template("calculadora.html",datos=d)
    

@app.route("/numero/<n>")
def parImpar(n):
    if (int(n) %2 ==0):
        return f"el numero {n} es par"
    else:
        return f"el numero {n} es Impar"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    titulo = request.args.get("titulo")
    return f"hola {titulo} {nombre}"

if __name__ == "__main__":
    app.run(port=3000, debug=True)