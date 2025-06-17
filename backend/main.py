from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from typing import List
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# Importaciones de nuestros módulos locales
from . import models, schemas, crud
from .database import engine, SessionLocal

# 1. Creación de Tablas (Se ejecuta una vez al inicio)
models.Base.metadata.create_all(bind=engine)

# 2. Inicialización de la App
app = FastAPI()

# 3. Configuración de Middlewares (CORS)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Dependencias
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. Rutas de la API (Todas las rutas de API juntas)
@app.get("/api/productos", response_model=List[schemas.Product])
def get_all_products(db: Session = Depends(get_db)):
    products = crud.get_products(db=db)
    return products

@app.post("/api/productos", response_model=schemas.Product, status_code=201)
def create_new_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

# 6. Montaje de Archivos Estáticos (Al final, antes de la ruta raíz)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FRONTEND_DIR = os.path.join(PROJECT_ROOT, 'frontend')

app.mount("/css", StaticFiles(directory=os.path.join(FRONTEND_DIR, "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join(FRONTEND_DIR, "js")), name="js")
app.mount("/images", StaticFiles(directory=os.path.join(FRONTEND_DIR, "images")), name="images")

# 7. Ruta Raíz (La última de todas, como "catch-all")
@app.get("/")
async def read_root():
    # Esta línea DEBE tener 4 espacios al principio.
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    # Esta línea también DEBE tener 4 espacios al principio.
    return FileResponse(index_path)