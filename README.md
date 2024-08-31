## Instalación

Este proyecto es una calculadora de polinomios que permite al usuario ingresar términos de polinomios, realizar operaciones como suma, resta y derivadas, y graficar el polinomio resultante. La interfaz gráfica está construida con Tkinter y se puede ejecutar fácilmente en cualquier entorno que soporte Python.

### Requisitos previos

Asegúrese de tener Python instalado en su sistema. Puede descargarlo desde [python.org](https://www.python.org/downloads/).

### Pasos

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/DiegoFmDev/CALCULO_III-Proyecto-Final.git
    cd mi_proyecto
    ```

2. **Configurar un entorno virtual:**

    En Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    En macOS/Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecute la aplicación:**

    ```bash
    Python main.py
    ```

## Uso

Una vez que la aplicación se esté ejecutando, podrá:

- **Agregar términos:** Ingrese términos polinomiales en el formato `ax^b` (por ejemplo, `2x^2`) y elija la operación (suma o resta).
- **Mostrar polinomio:** Ver el polinomio actual.
- **Derivar polinomio:** Calcula la derivada del polinomio actual.
- **Polinomio gráfico:** Traza el polinomio en un gráfico.
- **Términos claros:** Restablece el polinomio para empezar de nuevo.
