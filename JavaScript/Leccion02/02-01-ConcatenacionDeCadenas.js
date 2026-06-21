/*var nombre = "Jose"
var apellido = "Montes"
var nombreCompleto = nombre+ " " +apellido
console.log(nombreCompleto)
var nombreCompleto2 = "Brian"+" "+"Astaburuaga"
console.log(nombreCompleto2)
var juntos = nombre + 219 //Lee de izq a der siguiendo la cadena lee el numero como tipo String
console.log(juntos)
juntos = nombre + (78 + 17) //Aqui se puede diferenciar a traves de los parentecis
console.log(juntos)
juntos = 78 + 17 + nombre
console.log(juntos)

nombre += apellido //Tercera Concatenacion usando el operador simplificado
console.log(nombre)*/

//Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro"
console.log(nombre2)

const apellido2 = "Lepes"
//apellido = "perez"; una constante no se puede modificar
console.log(apellido2)

//Ampliando el uso de var, let y const
/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobreescriba
*/

var nombre = "Brian"
nombre = "Astaburuaga"
console.log(nombre)

function saludar(){
    var nombre = "Natalia"
    console.log(nombre3)
}
//console.log(nombre3) //aqui no lee el dato en la funcion

if(true){
    var edad = 34
    console.log(edad)
}
console.log(edad) //en la funcion funciono correctamente, en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar2(){
    let nombre2 = "Brian"
    console.log(nombre2)
}
console.log(nombre2)
if(true){
    let edad2 = 26
    console.log(edad2)
}
console.log(edad)

/*
const se utiliza para valores constantes que no pueden ser reasignadas
*/
const fechaNacimiento = 2006
console.log(fechaNacimiento)
//fechaNacimiento = 2003
//console.log(fechaNacimiento) //solo se ejecuta el console anterior
