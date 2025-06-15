from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

# ---- Configuración ----
# Define la ruta al directorio frontend.
# 'os.path.dirname(__file__)' obtiene el directorio actual (backend).
# '..' sube un nivel al directorio raíz del proyecto (tienda-app).
# Se une con 'frontend' para obtener la ruta completa.
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')


# ---- Inicialización de la App ----
app = FastAPI()


# ---- Montaje de Archivos Estáticos ----
# Se "montan" los directorios estáticos. Cualquier petición que empiece con /css, /js, o /images
# será buscada en los directorios correspondientes dentro de /frontend.

app.mount("/css", StaticFiles(directory=os.path.join(FRONTEND_DIR, "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join(FRONTEND_DIR, "js")), name="js")
app.mount("/images", StaticFiles(directory=os.path.join(FRONTEND_DIR, "images")), name="images")


# ---- Ruta Principal ----
# Se define el endpoint para la ruta raíz ("/").
# Cuando un usuario visite la página principal, se ejecutará esta función.
@app.get("/")
async def read_root():
    """
    Esta función sirve el archivo index.html como respuesta principal.
    FileResponse es una forma eficiente de enviar un archivo al navegador.
    """
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))