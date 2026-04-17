"""
Ejercicio 1: Análisis de una lista de temperaturas

Este ejercicio consiste en aplicar los conceptos vistod en clase de funciones para 
analizar una lista de temperaturas que se toma cada hora por un dia. 
En este código se implementan tres funciones: promedio, extremos y dias_sobre_promedio.

prompt:

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
15/04/2026

"""
def promedio(lista):
    """
    """
    if not lista:
        return "Error: Se debe proporcionar una lista no vacía."
    
    suma_promedio = sum(lista)
    return suma_promedio / len(lista)
    """

    """ 
def extremos(lista):
    """_summary_

    Args:
        lista (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not lista:
        return "Error: Se debe proporcionar una lista no vacía."
    
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

def dias_sobre_promedio(lista):
    """_summary_

    Args:
        lista (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not lista:
        return "Error: Se debe proporcionar una lista no vacía."
    
    promedio_valor = promedio(lista)
    dias_sobre = sum(1 for valor in lista if valor > promedio_valor)
    return dias_sobre

# Ejemplo de uso
temperaturas = []
print("Promedio de temperaturas:", promedio(temperaturas))
print("Extremos:", extremos(temperaturas))
print("Días sobre el promedio:", dias_sobre_promedio(temperaturas))