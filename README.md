# AgroCBA - Gestión de Inventario Agropecuario

AgroCBA es una aplicación monolítica de consola desarrollada en Python para gestionar el inventario de una unidad productiva agropecuaria del Centro de Biotecnología Agropecuaria (CBA). Permite la gestión completa de productos mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y el cálculo del valor total del inventario.

SENA - Centro de Biotecnología Agropecuaria (CBA Mosquera)
**Programa:** Técnico en Programación de Software
**Aprendiz:** Nicole Sthephanie Alonso Mayorga 

## Funcionalidades
- **Registrar producto:** Permite guardar productos validando código único, texto no vacío para nombre/categoría, cantidad >= 0 y precio > 0.
- **Consultar productos:** Lista todos los registros almacenados.
- **Buscar producto:** Localiza y muestra la información detallada por código.
- **Actualizar producto:** Modifica nombre, categoría, cantidad o precio de un producto existente.
- **Eliminar producto:** Remueve productos previa confirmación.
- **Valor del inventario:** Calcula el total acumulado ($\text{cantidad} \times \text{precio}$).

## Tecnologías Utilizadas
- Python 3.x
- Git (Control de versiones)

## Instrucciones de Ejecución
1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:
   ```bash
   python main.py