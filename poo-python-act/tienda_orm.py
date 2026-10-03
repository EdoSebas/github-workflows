import os
from decimal import Decimal

from dotenv import load_dotenv
from sqlalchemy import ForeignKey, Numeric, String, create_engine, select
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

load_dotenv()


class Base(DeclarativeBase):
    pass


class Categoria(Base):
    __tablename__ = "categorias"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), unique=True)
    productos: Mapped[list["Producto"]] = relationship(back_populates="categoria")


class Producto(Base):
    __tablename__ = "productos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    precio: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    categoria: Mapped[Categoria] = relationship(back_populates="productos")

    def __repr__(self):
        return f"Producto({self.id}, {self.nombre}, {self.precio}, {self.categoria.nombre})"


class Tienda:
    """CRUD de productos. Recibe una URL para poder usar otra BD en pruebas."""

    def __init__(self, url=None):
        url = url or URL.create(
            "mysql+pymysql",
            username=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=int(os.getenv("DB_PORT", "3306")),
            database=os.getenv("DB_NAME", "tienda_poo"),
        )
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        self.s = Session(engine)

    def agregar(self, nombre, precio, categoria):
        cat = self.s.scalar(select(Categoria).where(Categoria.nombre == categoria)) or Categoria(nombre=categoria)
        p = Producto(nombre=nombre, precio=Decimal(precio), categoria=cat)
        self.s.add(p)
        self.s.commit()
        return p

    def listar(self):
        return list(self.s.scalars(select(Producto)))

    def actualizar_precio(self, id, precio):
        p = self.s.get(Producto, id)
        if p:
            p.precio = Decimal(precio)
            self.s.commit()
        return p

    def eliminar(self, id):
        p = self.s.get(Producto, id)
        if p:
            self.s.delete(p)
            self.s.commit()
        return p is not None


if __name__ == "__main__":
    t = Tienda()
    t.agregar("Teclado", "120000", "Tecnologia")
    t.agregar("Mouse", "60000", "Tecnologia")
    print(t.listar())
    t.actualizar_precio(1, "110000")
    t.eliminar(2)
    print(t.listar())
