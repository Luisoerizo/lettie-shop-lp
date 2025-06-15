from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

# Se define la clase Product, que hereda de Base.
# SQLAlchemy usará esta clase para crear una tabla llamada "products" en la base de datos.
class Product(Base):
    __tablename__ = "products"

    # Definición de las columnas de la tabla.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    cost = Column(Float)
    sku = Column(String, unique=True, index=True)
    quantity = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())