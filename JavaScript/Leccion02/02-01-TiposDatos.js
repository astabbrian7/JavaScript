// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica
*/

var nombre = "Brian"; // tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero = 3000; // Tipo Numérico
console.log(numero);

var objeto = {    // Tipo Object
    nombre : "Brian",
    apellido : "Astaburuaga",
    telefono : "2604232323"

}

console.log(objeto);

// Tipo de dato Boolean
var bandera = true;
console.log(bandera);

// Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("mi simbolo")
console.log(simbolo)

// Tipo de dato clase
class Persona{
	constructor(nombre,apellido){
		this.nombre = nombre;
		this.apellido = apellido;
	}
}

console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ["Citroen","Audi","BMW","Ford"];
console.log(typeof autos); //preguntamos que tipo de dato es:

var z = "";
console.log(z); //Esto se refiere a que es una cadena vacia:
console.log(typeof z); String

