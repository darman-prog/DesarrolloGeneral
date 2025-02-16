/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package calculadoraimc;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author damez
 */
public class CalculadoraIMC {

    
    
    public static float bajo = 18.5f;
    public static float normal = 24.9f;
    public static float obeso = 30.0f;
    public static float SobrePeso = 25f;
    public static Scanner calculo = new Scanner(System.in);
    public static float estatura = 0;
    public static float peso = 0;
    
    public static void main(String[] args) {
            
            
        System.out.println(" Bienvenido a calculadroa de IMC");

             while (true) {
                boolean validacion = false;
                
                while (!validacion){
                    try{
                        System.out.print(" Ingresa tu estatura = ");
                        estatura = calculo.nextFloat();
                          if (estatura > 10 && estatura < 100 ){
                                    estatura = estatura / 10;
                          }else if(estatura > 100){
                                estatura = estatura / 100;
                }
                        if (estatura > 0){
                        validacion = true;
                        } else {
                            System.out.println("la estatura debe ser en decimal ejemplo: 1,75");
                        }
                   } catch (InputMismatchException e) {
                        System.out.println(" Error entrada no valida ");
                        calculo.next();
                   }
            }
            
            validacion = false;
            while (!validacion){
                    try{
                        System.out.print(" Ingresa tu Peso");
                            peso = calculo.nextFloat();
                            if (peso > 0){
                                validacion = true;
                        } else {
                            System.out.println("Error el peso debe ser un valor numerico o numerico positivo");
                        }
                   } catch (InputMismatchException e) {
                        System.out.println(" Error entrada no valida ");
                        calculo.next();

               }
                   }
               
                CalculoImc();
            

                System.out.println(" 1.continuar 2.Salir ");
                Scanner eleccion = new Scanner(System.in);
                int opcion = eleccion.nextInt();
                if (opcion == 2){
                    break;
                }
        }
        
        
        
          } 
        
        public static void CalculoImc(){
            float operacion = peso / (estatura * estatura);
            if ( operacion >= obeso  ) {
             System.out.println(" Tu indice de masa corporal es = " + operacion);
             System.out.println(" Segun tu indice de masa corporal estas en peso obeso");
            }else if ( operacion >= SobrePeso ){
                System.out.println(" Tu indice de masa corporal es = " + operacion);
                System.out.println(" Segun tu indice de masa corporal estas en peso sobrepeso ");
            }else if ( operacion > bajo && operacion <= normal ){
                System.out.println(" Tu indice de masa corporal es = " + operacion);
                System.out.println(" Segun tu indice de masa corporal estas en peso normal ");
            }else if ( operacion < bajo ){
                System.out.printf(" Tu indice de masa corporal es = " + operacion);
                System.out.printf(" Segun tu indice de masa corporal estas en peso bajo ");
            } 
       
        }
        }
        
        
        
        
        
        

        
        
        
    
    

