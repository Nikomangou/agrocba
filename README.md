# AgroCBA - Gestión de Inventario Agropecuario

AgroCBA es una aplicación monolítica de consola desarrollada en Python para gestionar el inventario de una unidad productiva agropecuaria del Centro de Biotecnología Agropecuaria (CBA). Permite la gestión completa de productos mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y el cálculo del valor total del inventario y guardar datos en un archivo JSON.

SENA - Centro de Biotecnología Agropecuaria (CBA Mosquera)
**Programa:** Técnico en Programación de Software
**Aprendiz:** Nicole Sthephanie Alonso Mayorga 

---

## 🛠️ Funcionalidades Principales

* **Gestión CRUD de Productos:** Registrar, consultar, buscar por código, actualizar y eliminar registros de forma interactiva.
* **Formatos Tabulares:** Salida en consola limpia y alineada mediante f-strings para una visualización clara de los datos.
* **Persistencia de Datos:** Guardado y carga automática desde el archivo local `inventario.json`.
* **Módulo de Reportes Adicionales:**
  * Cálculo del valor total monetario del inventario.
  * Conteo de unidades totales en stock.
  * Identificación de productos de mayor precio y mayor stock.
  * Alerta visual de bajo inventario (unidades `<= 5`).
* **Filtros y Ordenamiento:**
  * Búsqueda por categoría específica.
  * Ordenamiento alfabético de los productos por nombre.

## 📋 Estructura de Datos

Cada producto dentro del sistema cuenta con los siguientes campos:

* **Código:** Identificador único (ejemplo: `P001`).
* **Nombre:** Descripción breve del producto.
* **Categoría:** Clasificación del producto (ejemplo: *Granos*, *Lácteos*).
* **Cantidad:** Número de unidades disponibles (entero `>= 0`).
* **Precio:** Valor unitario en moneda local (`float > 0`).

## 🚀 Recursos Utilizados 

* **Python 3.8** o superior instalado.
* No requiere la instalación de librerías externas (utiliza librerías nativas como `json`).

### Ejecución del Proyecto

1. Clona el repositorio o descarga los archivos en tu equipo:
   ```bash
   git clone [https://github.com/Nikomangou/Nombre-De-Tu-Repositorio.git](https://github.com/Nikomangou/Nombre-De-Tu-Repositorio.git)