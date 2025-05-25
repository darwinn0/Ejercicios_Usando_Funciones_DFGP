# Vamos a poner todos los ejercicios de la tarea en una clase para despues llamarlos en un main.
import os
os.system('cls' if os.name== 'nt' else 'clear')

class Tarea:
    def __init__ (self,num, num1, num2, num3, suma, base, altura, area, tabla, r, diametro, nombre):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num = num
        self.suma = suma
        self.base = base
        self.altura = altura
        self.area = area
        self.tabla = tabla
        self.r = r
        self.diametro = diametro
        self.nombre = nombre

# Ejercicio 1, Hola Mundo
    def holaMundo(self):
        print( "Hola Mundo" )
    
# Ejercicio 2, Sumar dos numeros
    def sumarDosNumeros(self):
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
        print(" ")

print(" ---------- EJERCICIOS DE CLASE ---------- ")

class EjerciciosClase:
    def __init__ (self, Isv, cantidad, Descuento, TotalCompra, fNacimiento, anioActual, edad, tabla, a, b, r, diametro, nombre, reciduo, potencia, rx, ry,x ,y):

        self.Isv = Isv
        self.cantidad = cantidad
        self.Descuento = Descuento
        self.TotalCompra = TotalCompra
        self.fNacimiento = fNacimiento
        self.anioActual = anioActual
        self.edad = edad
        self.tabla = tabla
        self.a = a
        self.b = b
        self.r = r
        self.diametro = diametro
        self.nombre = nombre
        self.reciduo = reciduo
        self.potencia = potencia
        self.rx = rx
        self.ry = ry
        self.x = x
        self.y = y



#EJERCICIO CLASE 1
    def DescuentoMayor(self):
        self.Isv=0.15
        self.cantidad= int(input("Por favor ingrese la cantidad: "))
        if self.cantidad >= 10000:
            self.Descuento=0.25
        else:
            self.Descuento=0
        self.TotalCompra= self.cantidad - (self.cantidad * self.Descuento)
        self.TotalCompra= self.TotalCompra + (self.TotalCompra * self.Isv)
        print(f"El total de la compra es : {self.TotalCompra}")

#EJERCICIO CLASE 2
    def Edad(self):
        self.fNacimiento=int(input("Por favor ingrese la fecha de nacimiento: "))
        self.anioActual = 2025
        self.edad = self.anioActual - self.fNacimiento
        print (f"La edad que usted tiene es {self.edad}")
        if self.edad >=21:
            print(f"ya tiene {self.edad} años, ya eres mayor de edad.")
        else:
            if self.edad >= 18:
                print("ya eres cuidadano")
            print(f"ya tienes {self.edad} anios, eres menor de edad.")

#Ejercicio 3
    def OtraMultiplicar(self):
        self.tabla = int(input("Por favor ingrese la tabla a multiplicar: "))
        for i in range(1,11):
            print(f"{self.tabla} X {i} = {self.tabla*i}")

#Ejercicio 4
    def TablaConWhile(self):
        self.tabla=5
        i=1
        while i <= 10:
            print(f"{self.tabla} X {i} = {self.tabla*i}")
            i += 1

#Ejercicio 5
    def Operaciones(self):
        def suma(a,b):
            return a+b

        def resta(a,b):
            return a-b

        def multiplicacion(a,b):
            return a*b

        def division(a,b):
            return a/b

        def potencia(a,b):
            return a**b

        print(f"La suma es: {suma(3,4)}")
        print(f"La resta es {resta(5,4)}")
        print(f"La multiplicacion es {multiplicacion(2,2)}")
        print(f"La division es {division(10,2)}")
        print(F"La potencia es {potencia(2,3)}")

#Ejercicio 6
    def DescuentoFuncion(self):
        def descuento(cantidad):
            if cantidad >= 10000:
                self.Descuento=0.25
            else:
                self.Descuento=0
            return self.Descuento
            

        self.Isv=0.15

        self.cantidad= int(input("Por favor ingrese la cantidad: "))
        if self.cantidad >= 10000:
            self.descuento=0.25
        else:
            self.descuento=0
        self.TotalCompra= self.cantidad - (self.cantidad * self.descuento)
        self.TotalCompra= self.TotalCompra + (self.TotalCompra * self.Isv)
        print(f"El total de la compra es : {self.TotalCompra}")

# Ejercicio 7
    def Whileclase(self):
        i = 0
        while i <=10:
            i +=1
            print(i)


# Ejercicio 8
    def ForClase(self):
        for i in range(11):
            print(i)

        for i in range(1,11):
            print (f"2X{i}={2*i}")

# Ejercicio 9
    def SaludoFuncion (self):
        def saludo (nombre):
            print(f"Hola {nombre}!")

        def _PI():
            return 3.1416

        def suma(a,b):
            return a+b

        #Invocamos la funcion.
        saludo ("Darwin Guzman.")

        #Calcular el diametro del circulo.
        self.r=1
        self.diametro=2*_PI()*self.r
        print(f"Diametro: {self.diametro}")

        #Funcions suma
        print(f"Funcion suma: {suma(1,1)}")

# Ejercicio 10, Operacions arimetricas
    def OperacionesArimetricasClase (self):
        
        self.a=10
        self.b=5

        #suma 
        self.suma=self.a+self.b
        print("Suma = ", self.suma)

        #resta
        self.resta = self.a-self.b
        print("Resta = ", self.resta)

        #Multiplicacion
        self.multiplicaion= self.a*self.b
        print("Multiplicacion = ", self.multiplicaion)

        #Divicion
        self.divicion = self.a / self.b
        print("Divicion = ", self.divicion)

        # Ingreso de valores a variables
        self.x=int(input("x: "))
        self.y=int(input("y: "))

        #Potencia
        self.potencia=self.x**self.y
        print(f"{self.x}^{self.y}= ", self.potencia)

        #suma 
        self.suma = self.x+self.y
        print(f"{self.x}+{self.y}= ", self.suma)

        #operador de residuo
        self.reciduo=self.x%self.y
        print(f"{self.x}+{self.y}= ", self.reciduo)

        #raiz cuadrada
        self.rx=self.x**(1/2)
        self.ry=self.y**(1/2)
        print("La raiz cuadrada de x es: ", self.rx)
        print("La raiz cuadrada de y es: ", self.ry)
        
# Ejercicio 11, Hola mundo clae
    def ClaseHolaMundo(self):
        print("Hola Mundo, Ejercicio de clase.")
        