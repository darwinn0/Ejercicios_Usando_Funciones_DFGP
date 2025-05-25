#hacemos el llamado a las clases creadas.

import os
os.system('cls' if os.name== 'nt' else 'clear')

from EjerciciosTarea import Tarea
from EjerciciosTarea import EjerciciosClase

respuesta = Tarea(num=0, num1=0, num2=0, num3=0, suma=0, base=0, altura=0, area=0, tabla=0, r=0, diametro=0, nombre=0)


print("Ejercicio de la tarea 1")
respuesta.holaMundo()
print(" ")

print("Ejercicio de la tarea 2, Suma de dos numeros")
respuesta.sumarDosNumeros()
print(" ")

print("Ejercicio de la tarea 3, caldular area de un rectangulo.")
respuesta.areaRectangulo()
print(" ")

print("Ejercicio de la tarea 4, dice si el numero ingresado es positivo negativo o cero.")
respuesta.positivoNegativo()
print(" ")

print("Ejercicio de la tarea 5, Va decir si el numero ingresado es par o impar.")
respuesta.parImpar()
print(" ")

print("Ejercicio de la tarea 6, Ingresa 3 numeros y dice cual es al mayor.")
respuesta.mayorTresNumeros()
print(" ")

systemPause = input("Presione enter para continuar...")

print("Ejercicio de la tarea 7, Cuenta del 1 al 10 con ciclo for.")
respuesta.cicloFor()
print(" ")

print("Ejercicio de la tarea 8, Tabla de multiplicar.")
respuesta.tablaMultiplicar()
print(" ")

print("Ejercicio de la tarea 9, Suma los primeros N numeros .")
respuesta.sumaNumeros()
print(" ")

print("Ejercicio de la tarea 10, Dibuja asteriscos.")
respuesta.dibujoAsteriscos()
print(" ")



respuesta2 = EjerciciosClase( Isv=0, cantidad=0, Descuento=0, TotalCompra=0, fNacimiento=0, anioActual=0, edad=0, tabla=0, a=0, b=0, r=0, diametro=0, nombre=0, reciduo=0, potencia=0, rx=0, ry=0,x=0 ,y=0)

print("========== EJERCICIOS DE CLASE ==========")
print(" ")

print("Ejercicio clase 1, calcula el ISV cuando la compra es mayor a 10000.")
respuesta2.DescuentoMayor()
print(" ")

print("Calcula la edad de una persona con la fecha de nacimiento.")
respuesta2.Edad()
print(" ")

print("Ejercicio clase 3, Tabla de multiplicar con ciclo for.")
respuesta2.OtraMultiplicar()
print(" ")

print("Ejercicio clase 4, Tabla de multiplicar con ciclo while.")
respuesta2.TablaConWhile()
print(" ")  

print("Ejercicio clase 5, Operaciones Arimetricas basicas.")
respuesta2.Operaciones()
print(" ")

print("Ejercicio clase 6, Descuento cuando la compra es mayor a 10000 pero con funcio.")
respuesta2.DescuentoFuncion()
print(" ")

print("Ejercicio clase 7, Imprime numeros hasta el 11.")
respuesta2.Whileclase()
print(" ")

print("Ejercicio clase 8, Ciclo for que imprime numeros hasta el 10 y hace la tabla del 2")
respuesta2.ForClase()
print(" ")

print("Ejercicio clase 9, Va imprimir saludos y calcular un diametro y va hacer una suma. ")
respuesta2.SaludoFuncion()
print(" ")

print("Ejercicio clase 10, Va imprimir las operaciones basicas hechas en clase. ")
respuesta2.OperacionesArimetricasClase()
print(" ")

print("Ejercicio clase 11, Va imprimir Hola Mundo Ejercicio clase.")
respuesta2.ClaseHolaMundo()