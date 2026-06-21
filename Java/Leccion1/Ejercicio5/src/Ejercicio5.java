import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        float nota1, nota2, nota3, suma;

        System.out.println("Ingrese la primera calificacion:");
        nota1 = entrada.nextFloat();

        System.out.println("Ingrese la segunda calificacion:");
        nota2 = entrada.nextFloat();

        System.out.println("Ingrese la tercera calificacion:");
        nota3 = entrada.nextFloat();

        suma = nota1 + nota2 + nota3;

        System.out.println("La suma de las calificaciones es: " + suma);
    }
}
    
