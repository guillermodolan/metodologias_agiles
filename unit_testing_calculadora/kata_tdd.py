# Ejercicio de TDD realizado en la clase de práctica del 27/08/2024


# En TDD primero escribimos los tests previo a  escribir la clase o la lógica a utilizar.
import unittest
import re

# Ejercicio TDD
# Puede tomar uno o dos números enteros, separados por coma. Un string vacío suma 0.


class KataTDD(unittest.TestCase):
    # Test 1: "Un string vacío suma 0"

    # Habiendo hecho el red step, escribimos la lógica para obtener un green test.
    def suma(self, texto):

        if texto != '':
            # Me aseguro que en el string solo haya dos números (es decir solo una coma) (Requerimiento 1)
            # nums = map(int, texto.split(",", maxsplit=1))

            # Construímos un caso más genérico, es decir, para más de dos números. (Requerimiento 2)
            # nums = map(int, texto.split(","))

            partes = re.split(r'[, \n]', texto.strip())
            nums = map(int, partes)
            return sum(nums)

        # Si viene vacío el string, retorna cero.
        return 0

    # Primero escribimos el test, previo a crear la lógica
    def test_string_vacio(self):
        self.assertEqual(self.suma(''), 0)

    def test_uno_mas_dos(self):
        self.assertEqual(self.suma('1,2'), 3)

    def test_cuatro_mas_dos(self):
        self.assertEqual(self.suma('4,2'), 6)

    def test_uno_mas_dos_mas_tres(self):
        self.assertEqual(self.suma('1,2,3'), 6)

    def test_multiples_numeros(self):
        self.assertEqual(self.suma('1,2,3,5,8,13'), 32)

    def test_numeros_y_saltos_de_linea(self):
        self.assertEqual(self.suma('1,2,4\n5,6'), 18)


if __name__ == "__main__":
    unittest.main()