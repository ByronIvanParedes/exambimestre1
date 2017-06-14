# -*- coding: utf-8 -*-
"""
@author: Byron
"""

from tkinter import *
from turtle import *
import math
import turtle

def areaCuadrado(val1):
    respuesta = 0
    respuesta = val1*val1
    return respuesta

def areaTriangulo(val1,val2):
    respuesta = 0
    respuesta = (val1*val2)/2
    return respuesta

def areaPentagono(lado,radio):
    apotema = math.sqrt((radio*radio)-(lado/2)**2)
    print(apotema)
    respuesta = 0
    respuesta = (5*lado*apotema)/2
    return respuesta

def triangulo(lados):
    lados = lados + 200 #LE PUSE +200 PARA QUE EL DIBUJO SALGA GRANDE
    turtle.pencolor('green')
    turtle.left(305)
    
    for x in range (3):
        turtle.forward(lados)
        turtle.left(235)
    turtle.hideturtle()
    turtle.exitonclick()

def triangulo2(base,altura):
    base = base + 200 #LE PUSE +200 PARA QUE EL DIBUJO SALGA GRANDE
    altura = altura +200
    
    lado = math.sqrt((base**2)+(altura**2))
    turtle.pencolor('green')
    turtle.forward(base)
    turtle.left(180)
    turtle.forward(base/2)
    turtle.left(-90)
    turtle.forward(altura)
    turtle.left(60)
    turtle.forward(lado)
    turtle.left(45)
    
    turtle.hideturtle()
    turtle.exitonclick()
    
def pentagono(lados,longitud):
    longitud = longitud+200 #LE PUSE +200 PARA QUE EL DIBUJO SALGA GRANDE
    
    Angulo = ((lados-2)*180)/lados
    turtle.pencolor('red')
    turtle.left(35)
    for x in range (lados):
        turtle.forward(longitud)
        turtle.left(Angulo+180)
    turtle.hideturtle()
    turtle.exitonclick()

def cuadrado(lados):
    lados = lados + 200 #LE PUSE +200 PARA QUE EL DIBUJO SALGA GRANDE
    turtle.pencolor('blue')
    for x in range (4):
        turtle.forward(lados)
        turtle.left(90)
    turtle.hideturtle()
    turtle.exitonclick()  
def mensaje():
    msg = Message(frame, text = "Este problema no lo resolvi")
    msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    
def main_line():
        print("")
        print("*************Figuras para calcular área dependiendo sus lados:***************")
        print("3. Triangulo")
        print("4. Cuadrado")
        print("5. Pentagono")
        print("")
        y = int(input("Ingrese Valor:"))
        
        if y <= 2 or y >=6:
            print("")
            print("El valor no es valido")
            print("")
        if y == 4:
                val1 = int(input("Ingresa la base: "))
                print("El area del cuadrado es de: ")
                print(areaCuadrado(val1))
                cuadrado(val1)
                
        if y == 3:
                base = int(input("ingresa la base: "))
                altura = int(input("ingresa la altura: "))
                print("El area del triangulo es de: ")
                print(areaTriangulo(base,altura))
                triangulo(base)
        if y == 5:
                lado = int(input("ingresa la longitud lado: "))
                radio = int(input("ingresa la longitud radio: "))
                print("El area del pentagono es de: ")
                print(areaPentagono(lado,radio))
                pentagono(y,lado)
            
ventana = Tk()
ventana.title("EXAMEN 1B PROGRAMACION")
ventana.geometry("640x480")

frame=Frame(ventana)
frame.grid(column=0,row=4,padx=(250,90),pady=(90,250))
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=1)

ventana.configure(bg = 'green')



Label(ventana,fg="black", font= ("arial", 17,"bold"),text="EXAMEN PROGRAMACION").grid(column=0,row=3)


b1=Button(frame,fg="green", font= ("arial", 12,"bold"),text='AREAS',width=10,command=main_line)
b1.grid(column=1,row=4)


b2=Button(frame,fg="green", font= ("arial", 12,"bold"),text='EJERCICIO 2',width=10,command=mensaje)
b2.grid(column=1,row=6)


ventana.mainloop()


