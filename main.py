
productos = [
    ["TV 32", 60, 200000],
    ["Ventilador", 45, 150000],
    ["Microondas", 80, 300000]
]

while True:
    print("*" * 20)
    print("Menu de Opciones\n")
    print("1. Agregar Producto")
    print("2. Modificacion")
    print("3. Eliminar")
    print("4. Mostrar Todo")
    print("0. Salir")
    print("*" * 20)

    opcion = input("Ingresa una opcion: ")
    opcion = int(opcion)

    if opcion == 0:
        print("Adios!")
        break
    elif opcion == 1:
        print("Alta de Producto")

        nombre_producto = input("Nombre del producto: ")
        cantidad = int(input("Ingrese cantidad: "))
        precio = float(input("Ingrese Precio: $"))

        producto = [nombre_producto, cantidad, precio]
        productos.append(producto)


    elif opcion == 2:
        print("Modificar")
    elif opcion == 3:
        print("Eliminar")
    elif opcion == 4:
        print("Listado")
        if len(productos) == 0:
            print("No hay productos Agregados")
        else:
            # print(productos)
            for producto in productos:
                print(f"{producto[0].ljust(30)}{str(producto[1]).ljust(10)}{producto[2]}")
    else:
        print("Opcion Invalida")

print("Fin")