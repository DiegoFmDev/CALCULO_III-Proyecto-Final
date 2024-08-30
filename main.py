import tkinter as tk
from tkinter import messagebox
from polynomial import Polinomio
import matplotlib.pyplot as plt
import numpy as np

class PolynomialApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Polinomios")
        self.geometry("400x600")
        self.pol = Polinomio()
        self.create_widgets()

    def create_widgets(self):
        # Entrada de términos completos (coeficiente y exponente)
        tk.Label(self, text="Términos (ej: 1x^1 + 2x^2):").pack()
        self.coef_entry = tk.Entry(self)
        self.coef_entry.pack()

        # Menú desplegable para seleccionar la operación
        self.operacion_var = tk.StringVar(self)
        self.operacion_var.set("Sumar")  # Valor predeterminado

        tk.Label(self, text="Operación:").pack()
        tk.OptionMenu(self, self.operacion_var, "Sumar", "Restar").pack()

        # Botones para agregar término, mostrar polinomio, derivar y borrar
        tk.Button(self, text="Agregar Término", command=self.agregar_termino).pack()
        tk.Button(self, text="Mostrar Polinomio", command=self.mostrar_polinomio).pack()
        tk.Button(self, text="Derivar Polinomio", command=self.derivar_polinomio).pack()
        tk.Button(self, text="Borrar Términos", command=self.borrar_terminos).pack()
        tk.Button(self, text="Graficar Polinomio", command=self.graficar_polinomio).pack()

        # Área de texto para mostrar el resultado
        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.pack(pady=(20, 10))

    def agregar_termino(self):
        try:
            terminos = self.coef_entry.get().split('+')
            operacion = self.operacion_var.get()
            for termino in terminos:
                coef, exp = termino.split('x^')
                coef = int(coef.strip())
                exp = int(exp.strip())

                if operacion == "Restar":
                    coef = -coef
                    # falta mejroara para que la operacion sea a tod el polinomio y n ocada termino ejm -()

                self.pol.poner_termino(coef, exp)

            messagebox.showinfo("Éxito", "Términos agregados correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese los términos en el formato correcto, como '1x^1 + 2x^2'.")

    def mostrar_polinomio(self):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Polinomio: {self.pol.mostrar()}\n")

    def derivar_polinomio(self):
        derivada = self.pol.derivar()
        self.result_text.insert(tk.END, f"Derivada: {derivada.mostrar()}\n")

    def borrar_terminos(self):
        self.pol = Polinomio()  # Reinicia el polinomio
        self.result_text.delete(1.0, tk.END)
        messagebox.showinfo("Éxito", "Todos los términos han sido borrados.")

    def graficar_polinomio(self):
        x = np.linspace(-10, 10, 400)
        y = [self.pol.evaluar(xi) for xi in x]

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=self.pol.mostrar(), color="blue")        
        
        # Personalizar la cuadrícula    
        plt.grid(True, which='both')  # Mostrar grid
        plt.axhline(0, color='black', linewidth=0.8)  # Línea horizontal en y=0
        plt.axvline(0, color='black', linewidth=0.8)  # Línea vertical en x=0


        plt.title("Gráfico del Polinomio")
        plt.xlabel("X")
        plt.ylabel("f(X)")
        # plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    app = PolynomialApp()
    app.mainloop()
