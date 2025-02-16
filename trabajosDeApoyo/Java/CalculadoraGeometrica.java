/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Java;

import java.util.Scanner;

/**
 *
 * @author damez
 */
public class CalculadoraGeometrica {
    
    public static  Scanner capturador = new Scanner (System.in);
    public static  double resultado = 0;
    public static  double l1 = 1.5;
    public static  double l2 = 0;
    public static  double l3 = 0;
    public static  double b = 0;
    public static  double h = 0;
    public static  double r = 0;
    public static  double PI = Math.PI;
    
    
    public static void main(String[] args) {
       boolean bucle = true;
        while ( bucle ) {
            System.out.println(" calculadora Geometrica ");
            System.out.println("""
                           1. area del retangulo
                           2. perimetro del retangulo
                           3. area del triangulo
                           4. perimetro del triangulo
                           5. area del circulo
                           6. perimetro del circulo
                           7. Salir del programa  """);
        
            int op = 0;
           
           
            while (true) {
                System.out.print("Ingrese una opcion (1-7): ");
                if (capturador.hasNextInt()) { // Verifica si es un número entero
                    op = capturador.nextInt();
                    capturador.nextLine(); // Limpiar el buffer
                    if (op >= 1 && op <= 7) { // Verificar rango válido
                         break; // Salir del bucle si la opción es válida
                 } else {
                    System.out.println("Opcion no valida. Por favor, ingrese un valor del 1 al 7.");
                }
            } else {
                System.out.println("Por favor, ingrese un número válido.");
                capturador.next(); // Limpiar el buffer
            }
        }
            
            
            switch (op) {
                case 1 -> {calcularAreaRetangulo();} 
                
                case 2 -> {calcularPerimetroRetangulo();}
                
                case 3 -> {calcularAreaTriangulo();}
                
                case 4 -> {calcularPerimetroTriangulo();}
                 
                 
                case 5 -> {AreaCiruclo();}
                
                case 6 -> {PerimetroCirculo();}
            
                case 7 -> {  
                    System.out.println(" Saliendo del programa....");
                    bucle = false; }
                default -> System.out.println(" Ingresa un numero del 1 al 7 ");
            }
            
               
    }
        capturador.close();
        }
        
   
    // calculos
    public static void calcularAreaRetangulo(){
                CalcularValoresRetangulo();
                resultado = l1*l2;
                System.out.println(" el area del rectangulo es = "+resultado);
    }

    public static void calcularPerimetroRetangulo(){
                 CalcularValoresRetangulo();
                 resultado = (l1+l2)*2;
                 System.out.println(" El perimetro del cuadrado es = "+resultado);
    }
    
    public static void calcularPerimetroTriangulo(){
                 CalcularValoresTriangulo();
                 resultado = l1 + l2 + l3;
                 System.out.println(" el perimetro del triangulo es = " + resultado );
    }
    
    public static void calcularAreaTriangulo() {
                CalcularValoresPerimetroTriangulo();
                resultado = (b*h)/2;
                 System.out.println(" el area del triangulo es = "+resultado);
    }
    
    public static void AreaCiruclo(){
                CalcularValoresCirculo();
                resultado = PI * Math.pow(r,2);
                System.out.println(" el radio del circulo es = "+ resultado);
    }
    
    public static void PerimetroCirculo(){
                CalcularValoresCirculo();
                resultado = 2 * PI * r;
                System.out.println("  el perimetro del radio es = "+resultado);
    
    
    
    }
    
    // Utils
    public static void CalcularValoresRetangulo(){
            System.out.println(" ingrese el lado 1 ");
            l1 = Double.parseDouble(capturador.nextLine());
            System.out.println(" ingrese el lado 2 ");
            l2 = Double.parseDouble(capturador.nextLine());
    }

    public static void CalcularValoresTriangulo(){
            System.out.println(" ingrese el lado 1 ");
            l1 = Double.parseDouble(capturador.nextLine());
            System.out.println(" ingrese el lado 2 ");
            l2 = Double.parseDouble(capturador.nextLine());
            System.out.println(" ingrese el lado 3 ");
            l3 = Double.parseDouble(capturador.nextLine());
    }
    
    public static void CalcularValoresPerimetroTriangulo(){
            System.out.println(" ingrese la base del triangulo ");
            b = Double.parseDouble(capturador.nextLine());
            System.out.println(" ingrese la altura del triangulo ");
            h = Double.parseDouble(capturador.nextLine());
    
    }
    
    public static void CalcularValoresCirculo(){
            System.out.println(" ingresa el radio del circulo ");
            r = Double.parseDouble(capturador.nextLine());
          
    }
    
}
