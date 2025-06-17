from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# --- Schema Base ---
# Este schema contiene los campos comunes que se usan tanto para la creación como para la lectura.
# Así evitamos repetir código.
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None # Optional significa que puede ser None
    price: float
    cost: Optional[float] = None
    sku: Optional[str] = None
    quantity: int = 0

# --- Schema para Creación ---
# Este schema se usará cuando se reciba una petición para crear un nuevo producto.
# Hereda todos los campos de ProductBase.
class ProductCreate(ProductBase):
    pass # No necesita campos adicionales por ahora.

# --- Schema para Lectura ---
# Este es el schema que se usará para devolver un producto desde la API.
# Hereda de ProductBase y añade los campos que son generados por la base de datos.
class Product(ProductBase):
    id: int
    created_at: datetime

    # Configuración para que Pydantic pueda leer los datos desde un modelo de SQLAlchemy.
    # Es una instrucción para que el modelo Pydantic sea compatible con el ORM.
    class Config:
        from_attributes = True # Anteriormente conocido como orm_mode