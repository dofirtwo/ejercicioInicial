function validarDatos(){
    let num1 = document.getElementById("txtNum1");
    let num2 = document.getElementById("txtNum2");
    if(num1.value=="" || num2.value==""){
        return false; 
    }else{
        return true;
    }
}
/**
 * realiza una peticion al servidor para sumar
 * 
 */
function sumar(){
    if (validarDatos()){
        const data = new FormData(document.getElementById("frmCalculadora"));
        const url="/sumar";
        fetch(url, {
            method:"POST",
            body:data
        })
        .then(respuesta=>respuesta.json())
        .then(resultado=>{
            console.log(resultado);
            document.getElementById("txtResultado").value=resultado.Resultado;
        })
        .catch(error => console.log(error))
    }else{
        Swal.fire("problemas","faltan datos","warning")
    }
}
function restar(){
    if (validarDatos()){
        const data = new FormData(document.getElementById("frmCalculadora"));
        const url="/restar";
        fetch(url, {
            method:"POST",
            body:data
        })
        .then(respuesta=>respuesta.json())
        .then(resultado=>{
            console.log(resultado);
            document.getElementById("txtResultado").value=resultado.Resultado;
        })
        .catch(error => console.log(error))
    }else{
        Swal.fire("problemas","faltan datos","warning")
    }
}
function multiplicar(){
    if (validarDatos()){
        const data = new FormData(document.getElementById("frmCalculadora"));
        const url="/multiplicar";
        fetch(url, {
            method:"POST",
            body:data
        })
        .then(respuesta=>respuesta.json())
        .then(resultado=>{
            console.log(resultado);
            document.getElementById("txtResultado").value=resultado.Resultado;
        })
        .catch(error => console.log(error))
    }else{
        Swal.fire("problemas","faltan datos","warning")
    }
}
function dividir(){
    if (validarDatos()){
        const data = new FormData(document.getElementById("frmCalculadora"));
        const url="/dividir";
        fetch(url, {
            method:"POST",
            body:data
        })
        .then(respuesta=>respuesta.json())
        .then(resultado=>{
            n2=resultado.Numero2;
            if (n2==0.0){
                Swal.fire("Error","No se puede dividir por cero","warning")
            }else{
                console.log(resultado);
                document.getElementById("txtResultado").value=resultado.Resultado;
            }
            
        })
        .catch(error => console.log(error))
    }else{
        Swal.fire("problemas","faltan datos","warning")
    }
}