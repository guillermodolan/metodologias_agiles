# Primer actividad de práctica, realizada el 06/08/2024
# Clase para realizar Unit Testing

class Calculadora:
    numero1 = 0
    numero2 = 0

    @staticmethod
    def sumar():
        return Calculadora.numero1 + Calculadora.numero2

    @staticmethod
    def restar():
        return Calculadora.numero1 - Calculadora.numero2
