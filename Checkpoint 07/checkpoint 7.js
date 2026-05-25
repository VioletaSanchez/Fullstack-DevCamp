/*
Cree una función JS que acepte 4 argumentos. Suma los dos primeros argumentos, luego los dos segundos y multiplícalos.
Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". Si es más pequeño, la consola registra "¡El número es menor que 50!"
 */

function comparar_nums(num_uno, num_dos, num_tres, num_cuatro) {
    var primera_suma = num_uno + num_dos;
    console.log("La suma de los primeros dos números (" + num_uno + " y " + num_dos + ") es: " + primera_suma);
    var segunda_suma = num_tres + num_cuatro;
    console.log("La suma de los últimos dos números (" + num_tres + " y " + num_cuatro + ") es: " + segunda_suma);
    var total = primera_suma * segunda_suma;
    console.log("La multiplicación de los dos resultado es: " + total);
    if (total > 50) {
        console.log("¡El número es mayor que 50!");
    } else {
        console.log("¡El número es menor que 50!");
    }
    return total;
}

// Hacemos una comparación que resulta menor que 50.
var primera_comparación = comparar_nums(1, 2, 3, 4);

// Hacemos una comparación mayor que 50.
var segunda_comparación = comparar_nums(11, 62, 83, 24);

// Hacemos una comparación con números negativos y números con coma.
var tercera_comparación = comparar_nums(2, 1.1, 50, -736);