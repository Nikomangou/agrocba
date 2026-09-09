import json

inventario = []

def imprimir_tabla_productos(lista_prod):
    """Imprime lista de productos alineada con guiones sin bordes verticales."""
    print(f"{'Codigo':<10}{'Nombre':<20}{'Categoria':<15}{'Cantidad':<10}{'Precio':<10}")
    print("-" * 65)
    for prod in lista_prod:
        print(f"{prod['codigo']:<10}{prod['nombre']:<20}{prod['categoria']:<15}{prod['cantidad']:<10}{prod['precio']:<10}")

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
    print("\n--- Consultar Productos ---")
    if not inventario:
        print("No existen productos registrados.")
        return
    imprimir_tabla_productos(inventario)

def buscar_producto():
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese el código a buscar: ").strip()
    prod = obtener_producto_por_codigo(codigo)
    if prod:
        imprimir_tabla_productos([prod])
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

        try:
            cant_input = input(f"Nueva cantidad (actual: {prod['cantidad']}): ").strip()
            if cant_input:
                cant_val = int(cant_input)
                if cant_val >= 0:
                    prod['cantidad'] = cant_val
                else:
                    print("Cantidad no válida. Se conserva la anterior.")
        except ValueError:
            print("Entrada inválida. Se conserva la cantidad anterior.")

        try:
            precio_input = input(f"Nuevo precio (actual: ${prod['precio']}): ").strip()
            if precio_input:
                precio_val = float(precio_input)
                if precio_val > 0:
                    prod['precio'] = precio_val
                else:
                    print("Precio no válido. Se conserva el anterior.")
        except ValueError:
            print("Entrada inválida. Se conserva el precio anterior.")

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

# --- RETOS ADICIONALES ---

def reportes_adicionales():
    print("\n--- REPORTES Y RETOS ADICIONALES ---")
    if not inventario:
        print("No hay productos registrados.")
        return

    total_unidades = sum(p['cantidad'] for p in inventario)
    print(f"* Cantidad total de unidades en stock: {total_unidades}")

    prod_mayor_precio = max(inventario, key=lambda x: x['precio'])
    print(f"* Producto de mayor precio: {prod_mayor_precio['nombre']} (${prod_mayor_precio['precio']:.2f})")

    prod_mayor_stock = max(inventario, key=lambda x: x['cantidad'])
    print(f"* Producto con mayor stock: {prod_mayor_stock['nombre']} ({prod_mayor_stock['cantidad']} unidades)")

    bajo_stock = [p for p in inventario if p['cantidad'] <= 5]
    print("\n--- Productos con bajo inventario (<= 5) ---")
    if bajo_stock:
        print(f"{'Codigo':<10}{'Nombre':<20}{'Cantidad':<10}")
        print("-" * 40)
        for p in bajo_stock:
            print(f"{p['codigo']:<10}{p['nombre']:<20}{p['cantidad']:<10}")
    else:
        print("Todos los productos tienen buen stock (> 5 unidades).")

def consultar_por_categoria():
    print("\n--- Consultar por Categoría ---")
    if not inventario:
        print("No existen productos registrados.")
        return
    cat_buscar = input("Ingrese la categoría a filtrar: ").strip().lower()
    coincidencias = [p for p in inventario if p['categoria'].lower() == cat_buscar]
    
    if coincidencias:
        print(f"\nProductos en la categoría '{cat_buscar}':")
        imprimir_tabla_productos(coincidencias)
    else:
        print(f"No se encontraron productos en la categoría '{cat_buscar}'.")

def ordenar_alfabeticamente():
    print("\n--- Productos Ordenados Alfabéticamente ---")
    if not inventario:
        print("No existen productos registrados.")
        return
    inventario_ordenado = sorted(inventario, key=lambda x: x['nombre'].lower())
    imprimir_tabla_productos(inventario_ordenado)

def guardar_datos_json():
    try:
        with open("inventario.json", "w", encoding="utf-8") as archivo:
            json.dump(inventario, archivo, indent=4, ensure_ascii=False)
        print("Datos guardados exitosamente en 'inventario.json'.")
    except Exception as e:
        print(f"Error al guardar datos: {e}")

def cargar_datos_json():
    global inventario
    try:
        with open("inventario.json", "r", encoding="utf-8") as archivo:
            inventario = json.load(archivo)
        print("Datos cargados correctamente desde 'inventario.json'.")
    except FileNotFoundError:
        inventario = []

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
    print("7. Ver Reportes (Stock, Precios, Bajo inventario)")
    print("8. Consultar por categoría")
    print("9. Ordenar productos alfabéticamente")
    print("10. Guardar datos en JSON")
    print("11. Salir")
    print("==============================")

def main():
    cargar_datos_json()
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
            reportes_adicionales()
        elif opcion == "8":
            consultar_por_categoria()
        elif opcion == "9":
            ordenar_alfabeticamente()
        elif opcion == "10":
            guardar_datos_json()
        elif opcion == "11":
            guardar_datos_json()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()