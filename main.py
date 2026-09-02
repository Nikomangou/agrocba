inventario = []

def obtener_producto_por_codigo(codigo):
    for prod in inventario:
        if prod['codigo'] == codigo:
            return prod
    return None

def registrar_producto():
    print("\n--- Registrar Producto ---")
    codigo = input("Ingrese el código: ").strip()
    if not codigo:
        print("Error: El código no puede estar vacío.")
        return
    if obtener_producto_por_codigo(codigo):
        print("Error: Ya existe un producto con ese código.")
        return

    nombre = input("Ingrese el nombre: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    categoria = input("Ingrese la categoría: ").strip()
    if not categoria:
        print("Error: La categoría no puede estar vacía.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad < 0:
            print("Error: La cantidad debe ser mayor o igual a 0.")
            return
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        return

    try:
        precio = float(input("Ingrese el precio: "))
        if precio <= 0:
            print("Error: El precio debe ser mayor que 0.")
            return
    except ValueError:
        print("Error: El precio debe ser un número válido.")
        return

    nuevo_producto = {
        'codigo': codigo,
        'nombre': nombre,
        'categoria': categoria,
        'cantidad': cantidad,
        'precio': precio
    }
    inventario.append(nuevo_producto)
    print("Producto registrado exitosamente.")

def consultar_productos():
    print("\n--- Lista de Productos ---")
    if not inventario:
        print("No existen productos registrados.")
        return
    for prod in inventario:
        print(f"Código: {prod['codigo']} | Nombre: {prod['nombre']} | Categoría: {prod['categoria']} | Cantidad: {prod['cantidad']} | Precio: ${prod['precio']}")

def buscar_producto():
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese el código a buscar: ").strip()
    prod = obtener_producto_por_codigo(codigo)
    if prod:
        print(f"Encontrado: {prod['nombre']} - Categoría: {prod['categoria']} - Stock: {prod['cantidad']} - Precio: ${prod['precio']}")
    else:
        print("Producto no encontrado.")

def actualizar_producto():
    print("\n--- Actualizar Producto ---")
    codigo = input("Código del producto: ").strip()
    prod = obtener_producto_por_codigo(codigo)
    if prod:
        nuevo_nombre = input(f"Nuevo nombre (actual: {prod['nombre']}): ").strip()
        if nuevo_nombre:
            prod['nombre'] = nuevo_nombre

        nueva_cat = input(f"Nueva categoría (actual: {prod['categoria']}): ").strip()
        if nueva_cat:
            prod['categoria'] = nueva_cat

        print("Producto actualizado exitosamente.")
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    print("\n--- Eliminar Producto ---")
    codigo = input("Código del producto a eliminar: ").strip()
    prod = obtener_producto_por_codigo(codigo)
    if prod:
        confirmar = input(f"¿Desea eliminar {prod['nombre']}? (s/n): ").lower()
        if confirmar == 's':
            inventario.remove(prod)
            print("Producto eliminado exitosamente.")
    else:
        print("Producto no encontrado.")

def calcular_inventario():
    print("\n--- Valor Total del Inventario ---")
    total = sum(p['cantidad'] * p['precio'] for p in inventario)
    print(f"El valor total del inventario es: ${total:.2f}")

def mostrar_menu():
    print("\n==============================")
    print("       SISTEMA AGROCBA        ")
    print("==============================")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Mostrar valor total del inventario")
    print("7. Salir")
    print("==============================")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            calcular_inventario()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()