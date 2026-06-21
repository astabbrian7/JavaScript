package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite un numero entre 0 y 10: ");
        int calificacion = Integer.parseInt(entrada.nextLine());

        switch (calificacion) {

            case 10, 9 -> System.out.println("A");
            case 8 -> System.out.println("B");

            case 7 -> System.out.println("C");

            case 6 -> System.out.println("D");

            case 5, 4, 3, 2, 1, 0 -> System.out.println("F");
default ->  System.out.println("Fuera de rango");
        }
    }
}