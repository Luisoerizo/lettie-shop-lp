from sqlalchemy.orm import Session

from . import models, schemas

# --- Funciones CRUD para Productos ---

def get_products(db: Session, skip: int = 0, limit: int = 100):
    """
    Función para leer una lista de productos de la base de datos.

    Args:
        db (Session): La sesión de la base de datos, inyectada por FastAPI.
        skip (int): El número de registros a saltar (para paginación).
        limit (int): El número máximo de registros a devolver (para paginación).

    Returns:
        Una lista de objetos de modelo de producto de SQLAlchemy.
    """
    # db.query(models.Product): Inicia una consulta sobre la tabla de productos.
    # .offset(skip).limit(limit): Aplica la paginación.
    # .all(): Ejecuta la consulta y devuelve todos los resultados.
    return db.query(models.Product).offset(skip).limit(limit).all()

# --- Aquí añadiremos más funciones CRUD en el futuro (getProduct, createProduct, etc.) ---

# ... (la función get_products permanece arriba) ...

def create_product(db: Session, product: schemas.ProductCreate):
    """
    Función para crear un nuevo producto en la base de datos.

    Args:
        db (Session): La sesión de la base de datos.
        product (schemas.ProductCreate): El objeto Pydantic con los datos del producto a crear.

    Returns:
        El objeto de modelo de producto de SQLAlchemy que acaba de ser creado.
    """
    # 1. Se convierte el schema Pydantic a un diccionario.
    # 2. Se usa el ** para desempaquetar el diccionario y pasar sus claves y valores
    #    como argumentos al crear una instancia de nuestro modelo SQLAlchemy.
    db_product = models.Product(**product.model_dump())

    # 3. Se añade la nueva instancia de producto a la sesión de la base de datos.
    #    Esto lo prepara para ser guardado.
    db.add(db_product)

    # 4. Se confirman los cambios. Esto guarda el producto en la base de datos.
    db.commit()

    # 5. Se refresca la instancia. Esto actualiza el objeto db_product con los
    #    valores generados por la base de datos (como el nuevo 'id' y 'created_at').
    db.refresh(db_product)

    # 6. Se devuelve el objeto recién creado y actualizado.
    return db_product