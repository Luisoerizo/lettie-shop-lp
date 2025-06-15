from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos PostgreSQL.
# Formato: "postgresql://USER:PASSWORD@HOST:PORT/DATABASE_NAME"
# Estos son los datos que definimos en docker-compose.yml y que acordamos registrar.
SQLALCHEMY_DATABASE_URL = "postgresql://lettie_user:lettie_password@localhost:5432/lettie_shop_db"

# El "engine" es el punto de entrada principal para SQLAlchemy.
# Gestiona las conexiones a la base de datos.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cada instancia de SessionLocal será una sesión de base de datos.
# Por ahora, solo necesitamos definir la clase que creará estas sesiones.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Usaremos esta clase Base para que todos nuestros modelos de base de datos
# (las clases que definen las tablas) hereden de ella.
Base = declarative_base()