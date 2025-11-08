def menuInicio():
    opciones = {
        "1": ("Ejecutar ejercicio 1", ejercicio1),
        "2": ("Ejecutar ejercicio 2", ejercicio2),
        "3": ("Ejecutar ejercicio 3", ejercicio3),
        "4": ("Ejecutar ejercicio 4", ejercicio4),
        "5": ("Ejecutar ejercicio 5", ejercicio5)
    }

    bucle = True
    while bucle:
        print("\n ***** MENU DE OPCIONES *****")
        for key, (texto, _) in opciones.items():
            print(f"{key}) {texto}")
        print("6) Salir")

        opcion = input("Seleccione una opción: ", )

        if opcion == "6":
            print("Saliendo del programa...")
            bucle = False
        elif opcion in opciones:
            _, funcion = opciones[opcion]
            print("\n")
            funcion()
        else:
            print("Opción no válida")

def ejercicio1():
    bucle = True
    while bucle:
        suma = 0
        n = input("Introduce un numero entero y que sea positivo: ")
        try:
            n = int(n)
            if n < 0:
                raise ValueError
        except ValueError:
            print("ENTRADA INCORRECTO: Introduce un numero entero y que sea positivo")
        else:
            for j in range(n+1):
                divisor = 1
                for i in range(1,j+1):
                    divisor *= i
                if j % 2 == 0:
                    suma += (j+1)/divisor
                else:
                    suma -= (j+1)/divisor

            print("La suma es:", suma)
            bucle = False

def ejercicio2():
    bucle = True
    while bucle:
        n = input("Introduce un numero entero y que sea positivo: ")
        try:
            n = int(n)
            if n < 0:
                raise ValueError
        except ValueError:
            print("ENTRADA ERRONEA: Introduce un numero entero y que sea positivo")
        else:
            esTrino = True
            s = str(n)
            if len(s) < 2:
                esTrino = False
            else:
                for i in range(len(s)-1):
                    if abs(int(s[i+1])-int(s[i])) != 3:
                        esTrino = False
                        break
        if esTrino:
            print(f"El número es trino")
        else:
            print("El número no es trino")
        bucle = False

#Algoritmo que comprueba cuantos 0 hay al final de un numero introducido
def ejercicio3():
    bucle = True
    while bucle:
        Ceros=0
        num=input("Introduce un numero: ")
        try:
            num=int(num)
        except ValueError:
            print("No se ha introducido un valor valido")
        else:
            num=str(num)
            for i in num:
                if i=="0":
                    Ceros+=1
                else:
                    Ceros=0
            print(f"El numero de ceros es de {Ceros}")
            bucle = False

def ejercicio4():
    while True:
        try: #El try comprueba que es un input valido, el value error se asegura que es un int y el if sale del try si es mayor de 3 cifras y positivo
            num = int(input("Introduce un número entero positivo de más de 3 cifras: "))
            if num > 0 and len(str(num)) > 3:
                break
            else:
                print("Número no valido, debe ser positivo y tener más de 3 cifras.")
        except ValueError:
            print("Numero no valido, introduce un número entero, sin letras ni decimales.")
    original=num
    steps=[]
    while num>=10:
        sumNum=0
        for i in range(len(str(num))):
            sumNum+=int(str(num)[i]) #Aqui hago esta conversion para conseguir el valor que necesito sin tener que crear una lista
        steps.append(sumNum)
        num=sumnum
    print(f"El numero sintetizado de {original} es {num}")
    print("Los pasos son: ")
    for j in steps:
        print(j,end=" ")

def ejercicio5():
    bucle = True
    while bucle:
        num=input("Introduce un numero: ")
        try:
            num=int(num)
        except ValueError:
            print("Introduce un numero valido")
        else:
            num=str(num)
            lista=list(num)
            CuadContig=False
            for i in range(len(lista)-1):
                a=int(lista[i])
                b=int(lista[i+1])
                if a==b**2 or b==a**2:
                    CuadContig=True
                    break
            if CuadContig==True:
                print(f"El numero {num} es cuadrado contiguo")
            else:
                print(f"El numero {num} no es cuadrado contiguo")
            bucle = False

if __name__ == "__main__":
    menuInicio()