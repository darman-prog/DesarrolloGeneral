package Java;

import java.util.Scanner;

public class CalculadoraArimetica {
  public static void main(String[] args) {
    Scanner  entrada = new Scanner(System.in);
    Calculos calculos = new Calculos();
    boolean  bucle = true;|
    double resultado = 0;


    while (bucle) {
      
      System.out.println(" Bienvenido a calculadora Arimetica \n 1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.Division \n 5.potencia \n 0.Salir");
      
      int Eleccion = entrada.nextInt();
      
      if (Eleccion == 0) {
        System.out.println(" Saliendo del programa.... ");
        bucle = false;
        continue;
      }
      
      System.out.println(" Ingresa el primer numero: ");
      double x = entrada.nextDouble();
      System.out.println(" Ingresa el segundo numero: ");
      double y = entrada.nextDouble();


      switch (Eleccion) {
        case 1:
          resultado = calculos.Suma(x,y);
          break;
        case 2:
          resultado = calculos.Resta(x, y);
          break;
        case 3:
          resultado = calculos.Multiplicacion(x, y);
          break;
        case 4:
          resultado = calculos.Division(x, y);
          break;
        case 5:
          resultado = calculos.Potencia(x, y);
          break;
        default:
          break;
    }
      System.out.println(" tu resultado es = "+resultado);
      
  }
  entrada.close();
}

static public class  Calculos{
    public double Suma(double x , double y){
      return x + y;
    }
    public double Resta(double x , double y){
      return x - y;
    }

    public double Multiplicacion(double x , double y){
      return x * y;
    }

    public double Division(double x, double y){
      if (x != 0 || y != 0) {
        return x / y;
      } else {
        System.out.println(" no se puede dividir por cero ");
        return 0;
      }
    }

    public double Potencia(double x, double y){
      return Math.pow(x,y);
    }
  }

}
