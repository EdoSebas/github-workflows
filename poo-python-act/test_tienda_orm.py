from decimal import Decimal

import pytest

from tienda_orm import Tienda


@pytest.fixture
def tienda():
    return Tienda("sqlite:///:memory:")


def test_agregar_y_listar(tienda):
    tienda.agregar("Teclado", "100", "Tecnologia")
    productos = tienda.listar()
    assert len(productos) == 1
    assert productos[0].categoria.nombre == "Tecnologia"


def test_actualizar_precio(tienda):
    p = tienda.agregar("Mouse", "50", "Tecnologia")
    tienda.actualizar_precio(p.id, "80")
    assert tienda.listar()[0].precio == Decimal("80")


def test_eliminar(tienda):
    p = tienda.agregar("Mouse", "50", "Tecnologia")
    assert tienda.eliminar(p.id) is True
    assert tienda.listar() == []
