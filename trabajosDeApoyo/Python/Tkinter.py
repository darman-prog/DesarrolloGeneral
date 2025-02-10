import re
from tkinter import *
nucleo = Tk()
nucleo.title(" Calculadora Suprema ")

#variables
i = 0

#texto
InputTx = Entry(nucleo, font= "Calibri 20")
InputTx.grid(row=0 , column=0,columnspan=4, padx=5 ,pady = 5)


#funciones
def click_boton(valor):
    global i
    InputTx.insert(i,valor)
    i += 1

def borrar():
    InputTx.delete(0,END)
    

def  operaciones():
    operacion = InputTx.get()
    try:
        operacion = operacion.replace("x","*")

        operacion = re.sub(r"(\d+)%",r"(\1/100)",operacion)

        resultado = eval(operacion)

        InputTx.delete(0,END)
        InputTx.insert(0,str(resultado))

    except ZeroDivisionError:
            InputTx.delete(0,END)
            InputTx.insert(0,"Error: Division por cero ")
    except Exception as e:
            InputTx.delete(0,END)
            InputTx.insert(0,"Error")
    
    
    
    

#botones
boton1 = Button(nucleo, text= "1" , width= 5, height= 2 , command= lambda: click_boton(1))
boton2 = Button(nucleo, text= "2" , width= 5, height= 2 , command= lambda: click_boton(2))
boton3 = Button(nucleo, text= "3" , width= 5, height= 2 , command= lambda: click_boton(3))
boton4 = Button(nucleo, text= "4" , width= 5, height= 2 , command= lambda: click_boton(4))
boton5 = Button(nucleo, text= "5" , width= 5, height= 2 , command= lambda: click_boton(5))
boton6 = Button(nucleo, text= "6" , width= 5, height= 2 , command= lambda: click_boton(6))
boton7 = Button(nucleo, text= "7" , width= 5, height= 2 , command= lambda: click_boton(7))
boton8 = Button(nucleo, text= "8" , width= 5, height= 2 , command= lambda: click_boton(8))
boton9 = Button(nucleo, text= "9" , width= 5, height= 2 , command= lambda: click_boton(9))
boton0 = Button(nucleo, text= "0" , width= 5, height= 2 , command= lambda: click_boton(0))

botonBorrar = Button(nucleo, text= "AC" , width= 5, height= 2 , command= lambda: borrar())
botonParentesis1 = Button(nucleo, text= "(" , width= 5, height= 2 , command= lambda: click_boton("("))
botonParentesis2 = Button(nucleo, text= ")" , width= 5, height= 2 , command= lambda: click_boton(")"))
botonPunto = Button(nucleo, text= "." , width= 5, height= 2 , command= lambda: click_boton("."))

botonPorciento = Button(nucleo, text="%",width=5,height=2 , command= lambda: click_boton("%"))
botonDiv = Button(nucleo, text= "/" , width= 5, height= 2 , command= lambda: click_boton("/"))
botonSum = Button(nucleo, text= "+" , width= 5, height= 2 , command= lambda: click_boton("+"))
botonMen = Button(nucleo, text= "-" , width= 5, height= 2 , command= lambda: click_boton("-"))
botonMul = Button(nucleo, text= "x" , width= 5, height= 2 , command= lambda: click_boton("x"))
botonIgual = Button(nucleo, text= "=" , width= 5, height= 2 , command= lambda: operaciones() )



#visualizacion de botones
boton1.grid(row = 4, column=0,padx=5,pady=5)
boton2.grid(row = 4, column=1,padx=5,pady=5)
boton3.grid(row = 4, column=2,padx=5,pady=5)
boton4.grid(row = 4, column=3,padx=5,pady=5)
boton5.grid(row = 5, column=0,padx=5,pady=5)
boton6.grid(row = 5, column=1,padx=5,pady=5)
boton7.grid(row = 5, column=2,padx=5,pady=5)
boton8.grid(row = 5, column=3,padx=5,pady=5)
boton9.grid(row = 6, column=0,padx=5,pady=5)
boton0.grid(row = 6, column=1,padx=5,pady=5)
botonSum.grid(row = 6, column=2,padx=5,pady=5)
botonMen.grid(row=6, column=3, pady=5 , padx= 5)
botonMul.grid(row=7, column=2, pady=5,padx=5 )
botonDiv.grid(row=7, column=3, pady=5,padx=5 )
botonIgual.grid(row=8, column= 3, pady = 5 ,padx = 5)
botonBorrar.grid(row=8 ,column=2 , padx=5,pady=5)
botonParentesis1.grid(row=7, column=0, pady=5,padx=5 )
botonParentesis2.grid(row=7, column=1, pady=5,padx=5 )
botonPunto.grid(row=8, column=1 , pady=5,padx=5 )
botonPorciento.grid(row=8,column = 0 , pady=5,padx=5)

nucleo.mainloop()