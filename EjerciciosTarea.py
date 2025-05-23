# Vamos a poner todos los ejercicios de la tarea en una clase para despues llamarlos en un main.
import os
os.system('cls' if os.name== 'nt' else 'clear')

class Tarea:
    def __init__ (self,num, num1, num2, num3, suma, base, altura, area, tabla):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num = num
        self.suma = suma
        self.base = base
        self.altura = altura
        self.area = area
        self.tabla = tabla

# Ejercicio 1, Hola Mundo
    def holaMundo(self):
        print( "Hola Mundo" )
    
# Ejercicio 2, Sumar dos numeros
    def sumar_dos_numeros(self):
        self.num1 = int(input("Ingrese el primer numero: "))
        self.num2 = int(input("Ingrese el segundo numero: "))
        self.suma = self.num1 + self.num2
        print(f"La suma de los numeros ingresados es {self.suma}")

# Ejercicio 3, Calcular el area de un rectangulo
    def areaRectangulo(self):   
        self.base=int(input("Por favor ingrese la base del rectangulo:"))
        self.altura=int(input("Por favor ingrese la altura del rectangulo:"))
        self.area=self.base*self.altura
        print(f"El area del rectangulo es {self.area}")

# Ejercicio 4, va decir si es positivo o negativo o cero.
    def positivoNegativo(self):
        self.Num = int(input("Ingrese un numero: "))
        if self.Num > 0:
            print(f"El numero {self.Num} es positivo.")
        elif self.Num < 0:
            print(f"El numero {self.Num} es negarivo.")
        else:
            print(f"El numero ingresaso es cero.")

# Ejercicio 5, Numero es par o impar.
    def parImpar(self):
        self.num=int(input("Por favor ingrese un numero entero: "))
        if self.num%2==0:
            print(F"El numero {self.num} es par.")
        else:
            print(f"El numero {self.num} es impar.")

# Ejercicio 6, Mayor de tres numeros
    def mayorTresNumeros(self):
        self.num1=int(input("Por favor ingrese el primer numero: "))
        self.num2=int(input("Por favor ingrese el segundo numero: "))
        self.num3=int(input("Por favor ingrese el tercer numero: "))
        if self.num1>self.num2 and self.num1>self.num3:
            print(f"El numero mayor es {self.num1}.")
        elif self.num2>self.num1 and self.num2>self.num3:
            print(f"El numero mayor es {self.num2}.")
        elif self.num3>self.num1 and self.num3>self.num2:
            print(f"El numero mayor es {self.num3}.")
        else:
            print("Los numeros son iguales.")

# Ejercicio 7, Cuenta del 1 al 10 con un ciclo for
    def cicloFor(self):
        for i in range(1, 11):
            print(i)

#Ejercicio 8, Tabla de multiplicar.
    def tablaMultiplicar(self):
        self.tabla=int(input("Por favor ingrese un numero entero: "))
        print(f"Tabla de multiplicar del {self.tabla}: ")
        for i in range(1, 11):
            print(f"{self.tabla} x {i} = {self.tabla*i}")

# Ejercicio 9, Sumar los primeros n numeros.
    def sumaNumeros(self):
        self.num=int(input("Por favor ingrese un numero entero: ")) 
        self.suma=0
        for i in range(1, self.num+1):
            self.suma+=i
        print(f"La suma de los numeros del 1 al {self.num} es: {self.suma}.")

# Ejercicio 10, Dibujo de asteriscos.
    def dibujoAsteriscos(self):
        self.num=int(input("Por favor ingrese un numero entero: "))
        for i in range(self.num):
            print("*", end="")
        print()