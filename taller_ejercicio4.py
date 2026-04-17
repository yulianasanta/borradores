def promedio_simple(lista_notas):
    return sum(lista_notas)/len(lista_notas)

def promedio_ponderado(lista_notas):
    n1= lista_notas[0] * 0.30
    n2 = lista_notas[1] * 0.30
    n3 = lista_notas[2] * 0.40
    return n1+n2+n3

def mayor_promedio(diccionario):
    nombre_m = "nombre"
    promedio_m = -1

    for nombre, lista in diccionario.items():
        promedio = promedio_ponderado(lista)
        if promedio > promedio_m:
            promedio_m = promedio
            nombre_m = nombre
    return nombre_m, promedio_m

def aprobados(diccionario):
    print("Lista de estudiantes aprobados")
    for nombre, lista in diccionario.items():
        promedio_general=promedio_ponderado(lista)
    if promedio_general >= 3.0:
        print(f"Estudiante {nombre} | promedio {promedio_general}")

def reporte_profesora(diccionario):
    for nombre, lista in diccionario.items():
        promedio_general = promedio_ponderado(lista)
        if promedio_general >= 3.0:
            print(f"{nombre} aprobó la clase de transformaciones con {promedio_general}.")
        else:
            print (f"{nombre} reprobó la clase de transformaciones con {promedio_general}.")

notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hermione":[5.0,5.0,5.0],
    "Draco":[4.5,4.2,5.0],
    "Nevil":[2.5,3.0,3.2]
    }

print("Resultados Individuales: ")
for nombre, lista in notas.items():
    simple=promedio_simple(lista)
    ponderado=promedio_ponderado(lista)
    print(f"El Estudiante {nombre} tiene un promedio simple de {simple} y un promedio ponderado de {ponderado}.")


mejor_n , mejor_p = mayor_promedio(notas)
print(f"El estudiante con mayor promedio es {mejor_n} con {mejor_p}")

print(aprobados(notas))

print(reporte_profesora(notas))