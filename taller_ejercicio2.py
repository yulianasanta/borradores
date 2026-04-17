def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

def multiplicacion (a,b):
    return a * b

def division (a,b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def exponente (a,b):
    if b==0:
        return 1
    resultado = 1
    for i in range(b):
        resultado = multiplicacion(resultado, a)
    return resultado if b > 0 else (1, resultado)

def raiz_cuadrada (a):
    if a<0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return a ** 0.5

def factorial (a):
    if a<0:
        return "Error: No se puede calcular el factorial de un número negativo."
    elif a==0 or a==1:
        return 1
    else:
        resultado = 1
        for i in range(2, a+1):
            resultado *= i
        return resultado 
    
def inversa (a):
    if a==0:
        return "Error: No se puede calcular la inversa de cero."
    return 1/a

def operacion(z):
    if z == 1:
        return suma(a, b)
    elif z == 2:
        return resta(a, b)
    elif z == 3:
        return multiplicacion(a, b)
    elif z == 4:
        return division(a, b)
    elif z == 5:
        return exponente(a, b)
    elif z == 6:
        return raiz_cuadrada(a)
    elif z == 7:
        return factorial(a)
    elif z == 8:
        return inversa(a)
    else:
        return "Error: Opción no válida. Por favor, elija un número del 1 al 8."

z = int(input("Ingrese el número de la operación que desea realizar (1-8): "))
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultado = operacion(z)
print("El resultado de la operación es:", resultado)