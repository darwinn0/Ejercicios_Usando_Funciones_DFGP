#hacemos el llamado a las clases creadas.

import os
os.system('cls' if os.name== 'nt' else 'clear')

from EjerciciosTarea import Tarea

respuesta = Tarea(num=0, num1=0, num2=0, num3=0, suma=0, base=0, altura=0, area=0, tabla=0)

print("Ejercicio de la tarea 1")
respuesta.holaMundo()
print(" ")

print("Ejercicio de la tarea 2, Suma de dos numeros")
respuesta.sumar_dos_numeros()
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



