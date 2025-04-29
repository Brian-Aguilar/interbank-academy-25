# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:

El reto consiste en desarrollar una aplicación de línea de comandos (CLI) que lea y procese un archivo CSV con datos de transacciones bancarias. Su propósito es automatizar el análisis financiero mediante la generación de un reporte que incluya el balance final, la transacción de mayor monto y el conteo de transacciones por tipo (Crédito y Débito), facilitando así la gestión y comprensión de movimientos financieros.

## Instrucciones de Ejecución:
`WSL en Windows 10 | Ubuntu/Debian o Fedora`
```bash
python3 main.py
```
`Windows`
```bash
python main.py
```

## Enfoque y Solución:

Este programa implementa una solución modular para procesar y analizar transacciones bancarias almacenadas en un archivo CSV. El diseño se basa en tres componentes principales: una clase `Transaccion` que actúa como modelo de datos para mapear cada fila del CSV; una clase `Proceso` que encapsula la lógica de carga, análisis y resumen de las transacciones; y un script principal (`main.py`) que instancia el proceso y muestra el reporte en consola. La clase `Proceso` realiza la lectura manual del archivo sin librerías externas como `pandas`, utilizando estructuras básicas para mantener claridad y control del flujo. Se emplea la clase `Decimal` para asegurar precisión en los cálculos monetarios. Durante la carga, se determina simultáneamente la transacción de mayor monto, el conteo de transacciones por tipo, y la suma total por categoría, lo cual optimiza el rendimiento al evitar múltiples pasadas sobre los datos. En resumen, el diseño apuesta por simplicidad, claridad y eficiencia sin depender de bibliotecas avanzadas.

## Estructura del Proyecto:

Está organizado de manera clara para facilitar su comprensión y mantenimiento. El archivo principal `main.py` ejecuta la aplicación y genera el reporte de transacciones. Dentro de la carpeta `models/` se define la estructura de los datos con la clase Transaccion, mientras que en `utils/` (que también podría llamarse `services/`) se encuentra la lógica principal en la clase Proceso, que carga, procesa y analiza las transacciones. El archivo `data.csv` contiene los datos de entrada que se procesarán, y el `README.md` ofrece una guía básica sobre el proyecto y su uso. Finalmente, el .gitignore especifica qué archivos deben excluirse del control de versiones, manteniendo el repositorio limpio.

```text
interbank-academy-25/
├── main.py
├── models/
│   ├── __init__.py
│   └── transacciones.py
├── utils/  # También se puede nombrar como service/
│   ├── __init__.py
│   └── proceso.py
├── data.csv # También se puede ubicar dentro de una carpeta data/
├── README.md
├── .gitignore
```