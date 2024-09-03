# Ejercicio de TDD realizado en la clase de práctica del 03/09/2024

import unittest

class Juego():

    pinostirados = []

    @staticmethod
    def Limpiar():
       Juego.pinostirados = []

    @staticmethod
    def Tirar(cantpinos):
        Juego.pinostirados.append(cantpinos)

    @staticmethod
    def Score():
        puntos = 0
        pos = 1
        while pos < len(Juego.pinostirados):
          puntos += Juego.pinostirados[pos]
          if (pos % 2 == 0) and (Juego.pinostirados[pos-1] + Juego.pinostirados[pos] == 10):
             puntos += Juego.pinostirados[pos+1]
          pos += 1
        return puntos

class BowlingTest(unittest.TestCase):

    # Test #1
    def testperdedor(self):
        Juego.Limpiar()
        Juego.Tirar(0)
        self.assertEqual(Juego.Score(), 0)

    # Test #2
    def testtirauno(self):
        Juego.Limpiar()
        for i in range(21):
            Juego.Tirar(1)
        self.assertEqual(Juego.Score(), 20)

    # Test #3
    def testprimer_spare(self):
      Juego.Limpiar()
      Juego.Tirar(1)
      Juego.Tirar(9)
      for i in range(19):
          Juego.Tirar(1)
      self.assertEqual(Juego.Score(), 29)

if __name__ == "__main":
  unittest.main()