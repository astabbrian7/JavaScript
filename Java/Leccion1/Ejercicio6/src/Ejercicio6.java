import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        float guillermo, luis, juan, total;

        System.out.println("Ingrese la cantidad de dinero de Guillermo:");
        guillermo = entrada.nextFloat();

        luis = guillermo / 2;
        juan = (guillermo + luis) / 2;

        total = guillermo + luis + juan;

        System.out.println("Guillermo tiene: " + guillermo);
        System.out.println("Luis tiene: " + luis);
        System.out.println("Juan tiene: " + juan);

        System.out.println("El total de dinero entre los tres es: " + total);
    }
}
  
