# Laboratorios de Python

**Aprendiz:** Juliana Baldion · **Ficha:** 3388087 · **Programa:** ADSO (SENA)

Repositorio personal que se usará durante los cuatro laboratorios de Python. Cada laboratorio está en su propia carpeta.

| Laboratorio | Tema | Carpeta | Programa principal |
|---|---|---|---|
| 01 | Primeros pasos: datos, operaciones y entrada de datos | `python-laboratorio-01/` | `cotizador_compra.py` |
| 02 | Decisiones, ciclos y colecciones | `laboratorio-02/` | `gestor_inventario.py` |

## Cómo ejecutar

Requiere Python 3. Entra a la carpeta del laboratorio y ejecuta el archivo:

```bash
cd python-laboratorio-01
python cotizador_compra.py
```

```bash
cd laboratorio-02
python gestor_inventario.py
```

Según el equipo, el comando puede ser `py` o `python3`.

---

## Laboratorio 01 — Primeros pasos con Python

### Contenido

| Práctica | Tema | Archivos |
|---|---|---|
| 1.1 | Entorno y primera ejecución | `hola_python.py`, `presentacion.py` |
| 1.2 | Variables y tipos de datos | `datos_basicos.py`, `perfil_aprendiz.py`, `inventario.py`, `error_variables.py`, `reto_variables.py` |
| 1.3 | Operadores y expresiones | `operadores.py`, `operaciones.py`, `conversion_tiempo.py`, `calculo_promedio.py`, `calculo_compra.py`, `calculo_salario.py`, `factura_simple.py` |
| 1.4 | Entrada de datos con `input()` | `saludo.py`, `tipo_entrada.py`, `datos_usuario.py`, `suma_interactiva.py`, `conversor_temperatura.py`, `salario_interactivo.py`, `depuracion.py`, `conversion_unidades.py` |
| 1.5 | Reto integrador | `cotizador_compra.py` |

### Cotizador de compra

Aplicación de consola que solicita: cliente, producto, precio unitario, cantidad, % de descuento, % de impuesto, costo de envío, vendedor y código de cotización. Calcula y muestra subtotal, descuento, base después del descuento, impuesto (sobre la base), envío y total final.

**Ejemplo.** Entradas: Laura, Teclado mecánico, 180000, 2, 10, 19 (envío 0).
Resultado: Subtotal $360000.0 · Descuento $36000.0 · Base $324000.0 · Impuesto $61560.0 · **TOTAL $385560.0**

| Precio | Cant. | Desc. % | Imp. % | Total esperado | Total obtenido |
|---|---|---|---|---|---|
| 100000 | 2 | 10 | 0 | 180000.0 | 180000.0 |
| 50000 | 3 | 0 | 0 | 150000.0 | 150000.0 |
| 80000 | 5 | 25 | 0 | 300000.0 | 300000.0 |
| 100000 | 1 | 0 | 19 | 119000.0 | 119000.0 |

---

## Laboratorio 02 — Decisiones, ciclos y colecciones

### Contenido

| Práctica | Tema | Archivos |
|---|---|---|
| 2.1 | Comparaciones y decisiones (`if`, `elif`, `else`) | `comparaciones.py`, `nota.py`, `disponibilidad.py`, `validar_edad.py`, `clasificar_numero.py`, `clasificar_nota.py`, `error_indentacion.py`, `costo_envio.py` |
| 2.2 | Condiciones compuestas (`and`, `or`, `not`) | `acceso_actividad.py`, `acceso_sala.py`, `rango_edad.py`, `validar_compra.py`, `evaluar_solicitud.py` |
| 2.3 | Ciclos `for` y `while` | `contador_for.py`, `tabla_multiplicar.py`, `sumar_numeros.py`, `promedio_notas.py`, `contador_while.py`, `hasta_cero.py`, `suma_interactiva.py`, `menu_repetitivo.py`, `control_ahorros.py` |
| 2.4 | Listas | `primera_lista.py`, `ciudades.py`, `invitados.py`, `lista_materias.py`, `sin_duplicados.py`, `operaciones_lista.py`, `calificaciones_lista.py`, `lista_tareas.py` |
| 2.5 | Tuplas | `primeras_tuplas.py`, `ubicaciones.py`, `categorias_tupla.py` |
| 2.6 | Conjuntos | `primer_conjunto.py`, `etiquetas.py`, `participantes.py`, `inscripciones_talleres.py` |
| 2.7 | Diccionarios y colecciones anidadas | `primer_diccionario.py`, `perfil_diccionario.py`, `actualizar_producto.py`, `catalogo_diccionarios.py`, `curso_anidado.py`, `catalogo_libros.py` |
| 2.8 | Comprensiones | `cuadrados.py`, `precios_con_impuesto.py`, `filtrar_numeros.py`, `normalizar_codigos.py`, `categorias_distintas.py`, `catalogo_codigo.py`, `informes_inventario.py`, `informe_comprensiones.py` |
| 2.9 | Reto integrador | `gestor_inventario.py`, `gestor_depuracion.py` |

### Gestor de inventario

Aplicación de consola con un menú que se repite hasta elegir `0`:

1. Registrar producto
2. Listar productos
3. Buscar por código
4. Actualizar existencias
5. Eliminar producto
6. Consultar productos sin stock
7. Resumen del inventario

Cada producto es un diccionario (`codigo`, `nombre`, `categoria`, `precio`, `cantidad`) y todos se guardan en una lista. Las categorías permitidas están en una tupla: `Periféricos`, `Componentes`, `Accesorios`. Los datos se mantienen mientras el programa está abierto.

**Reglas:** no se aceptan códigos repetidos ni textos vacíos, la categoría debe ser una de las permitidas, el precio debe ser mayor que cero y la cantidad no puede ser negativa.

### Comprobación numérica

Con P001 (85000 × 4, Periféricos), P002 (45000 × 0, Periféricos) y P003 (700000 × 2, Componentes):

| Dato | Esperado | Obtenido |
|---|---|---|
| Productos | 3 | 3 |
| Unidades | 6 | 6 |
| Valor del inventario | 1.740.000 | $1,740,000.0 |
| Categorías utilizadas | 2 | Periféricos, Componentes |
| Sin stock | P002 (Mouse) | Mouse |

`gestor_depuracion.py` es la copia con los cinco errores del reto de depuración provocados, explicados y corregidos.
