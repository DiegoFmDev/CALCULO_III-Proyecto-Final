class Polinomio:
    def __init__(self):
        # Inicializa el polinomio como un diccionario con exponentes como claves y coeficientes como valores
        self.terminos = {}

    def poner_termino(self, coef, exp):
        if exp in self.terminos:
            self.terminos[exp] += coef
        else:
            self.terminos[exp] = coef

    def mostrar(self):
        # Formatea y muestra el polinomio en la forma "Coef X^Grado"
        resultado = ""
        for exp in sorted(self.terminos.keys(), reverse=True):
            coef = self.terminos[exp]
            if coef != 0:
                resultado += f"{coef}X^{exp} + "
        return resultado[:-3] if resultado else "0"

    def evaluar(self, x):
        # Evalúa el polinomio en el valor x dado
        return sum(coef * (x ** exp) for exp, coef in self.terminos.items())

    def derivar(self):
        # Deriva el polinomio y devuelve un nuevo Polinomio con la derivada
        derivada = Polinomio()
        for exp, coef in self.terminos.items():
            if exp > 0:
                derivada.poner_termino(coef * exp, exp - 1)
        return derivada
