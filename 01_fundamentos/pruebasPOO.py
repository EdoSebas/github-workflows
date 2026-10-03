import unittest
import sqlite3

# ============================
# 1. La clase
# ============================
class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    def aplicar_descuento(self, porcentaje):
        self._precio -= self._precio * (porcentaje / 100)

    def __str__(self):
        return f"{self.nombre} - ${self._precio}"

    def guardar(self, conexion):
        conexion.execute(
            "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
            (self.nombre, self._precio)
        )
        conexion.commit()


# ============================
# 2. Prueba unitaria
# ============================
class TestProducto(unittest.TestCase):

    def test_descuento(self):
        p = Producto("Camiseta", 100)
        p.aplicar_descuento(10)
        self.assertEqual(p.precio, 90)


# ============================
# 3. Prueba de integración
# ============================
class TestProductoBD(unittest.TestCase):

    def test_guardar_en_bd(self):
        conexion = sqlite3.connect(":memory:")
        conexion.execute("CREATE TABLE productos (nombre TEXT, precio REAL)")

        p = Producto("Zapatos", 200)
        p.guardar(conexion)

        resultado = conexion.execute("SELECT nombre, precio FROM productos").fetchone()
        self.assertEqual(resultado, ("Zapatos", 200))


# ============================
# Ejecutar todas las pruebas
# ============================
if __name__ == "__main__":
    unittest.main()