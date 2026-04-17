# 1. Definicion de Funciones
def agregar_producto(diccionario, nombre, cantidad, precio):
    """Agrega un producto o actualiza sus valores si ya existe."""
    diccionario[nombre] = {
        "cantidad": cantidad, 
        "precio": precio
    }
    print(f"Se agrego {nombre} al inventario")

def eliminar_producto(diccionario, nombre):
    """Elimina un producto del diccionario si existe."""
    if nombre in diccionario:
        diccionario.pop(nombre)
        print("Producto eliminado:", nombre)
    else:
        print("Error: El producto no existe en el inventario.")

def calcular_valor_total(diccionario):
    """Suma el costo total (cantidad * precio) de todos los productos."""
    total = 0
    for datos in diccionario.values():
        total += datos["cantidad"] * datos["precio"]
    return total

def mostrar_inventario(diccionario):
    """Imprime el contenido actual del inventario."""
    print("--- LISTA DE INVENTARIO ---")
    if not diccionario:
        print("El inventario esta vacio.")
    else:
        for nombre, datos in diccionario.items():
            print(f"Producto: {nombre} | Cantidad: {datos['cantidad']} | Precio: {datos['precio']}")
    print("---------------------------")

# 2. Programa Principal con Menu Interactivo
def ejecutar_sistema():
    inventario_sistema = {}
    
    while True:
        print("SISTEMA DE INVENTARIO")
        print("1. Agregar o actualizar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario y valor total")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion (1-4): ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            # Convertimos las entradas a numeros para poder operar con ellas
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(inventario_sistema, nombre, cantidad, precio)
            
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario_sistema, nombre)
            
        elif opcion == "3":
            mostrar_inventario(inventario_sistema)
            total = calcular_valor_total(inventario_sistema)
            print(f"Valor total acumulado: {total:.2f}")
            
        elif opcion == "4":
            print("Finalizando programa.")
            break
        else:
            print("Opcion no valida, intente de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    ejecutar_sistema()