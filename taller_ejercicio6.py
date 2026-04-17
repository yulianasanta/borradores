def producto():
    productos={ 
        1:["Monster", 9500],
        2:["Chocorramo", 3300],
        2:["Oreo", 2400],
        4:["Agua", 1000],
        5:["Snickers",7100]
        }

    print("productos disponibles: ")
    for nombre, precio in productos.items():
        print(f"{nombre}-{precio}")

    eleccion = int(input("ingrese el numero del producto: "))

    if eleccion == 1:
        return "Monster", 9500
    if eleccion == 2:
        return "Chocorramo", 3300
    if eleccion == 3:
        return "Oreo", 2400
    if eleccion == 4:
        return "Agua", 1000
    if eleccion == 5:
        return "Snickers", 7100
    else:
        print("Opcion no valida.")

def maquina_dispensadora():
        nombre, precio = producto()

        dinero_ingresado = int(input(f"El precio es {precio}. Ingrese el dinero (billetes/monedas): "))

        if dinero_ingresado < precio:
            print(f"Dinero insuficiente. Falta ${precio-dinero_ingresado}")
            print("Transición fallida.")
            return
        
        
        cambio = dinero_ingresado - precio

        print(f"Producto entregado: {nombre}")

        if cambio > 0:
            print(f"Su devuelta es ${cambio}")
        else:
            print("No hay devuelta.")

        print("¡Gracias por su compra!")

maquina_dispensadora()