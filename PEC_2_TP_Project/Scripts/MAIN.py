def menuInicio():
    bucle = True
    while bucle:
        print("*****MENU DE OPCIONES****+")
        print("1) Ejecutar Ejercicio 1")
        print("2) Ejecutar Ejercicio 2")
        print("6) Salir")
        inputTecla = input("Introduzca que quiere realizar: ")
        if inputTecla == "1":
            ejercicio1()
        elif inputTecla == "2":
            ejercicio2()
        elif inputTecla == "6":
            bucle = False
            print("Saliendo")
        

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

if __name__ == "__main__":
    menuInicio()