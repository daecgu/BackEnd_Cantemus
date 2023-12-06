import glob

from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
# cargar las variables de entorno del archivo .env
load_dotenv()
from app.api.v1.endpoints.users import router as api_router
from app.api.v1.endpoints.canciones import router as canciones_router
from app.db.db_config import get_database

app = FastAPI()
# Conectarse a la base de datos.
get_database()

# Implementación de CORS
origins = [
    "http://localhost:3000",  # Si el frontend se ejecuta en localhost con puerto 3000
    "http://127.0.0.1:3000",  # Si el frontend se ejecuta en localhost con puerto 3000
    "https://tufrontend.com",  # Reemplazar con el dominio de producción de tu frontend
]

# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

# Incluir los routers
app.include_router(api_router)
app.include_router(canciones_router)

# Configurar conexión a la base de datos (esto podría estar en otro módulo importado aquí)
# Por ejemplo, utilizando una función de inicialización que usted defina en `app/db/db_config.py`
"""
docker run -d --name mi-backend -p 8000:8000 mi-backend-fastapi
docker start mi-backend
"""

# def crear_cancion(texto):
#     from app.api.v1.endpoints.helpers import generate_id, crear_o_aumentar_contador
#     from app.utils.procesador_canciones import ProcesadorCanciones
#     p = ProcesadorCanciones("",
#                             texto)
#     cancion = p.obtener_objeto_bbdd_cancion()
#     cancion.id_cancion = generate_id(crear_o_aumentar_contador("canciones"))
#     cancion.save()
#     print({"message": "Cancion Creada", "id_cancion": cancion.id_cancion})
#
# ruta = '/home/decheverri/PycharmProjects/BackEnd-cantemus/Canciones/Latin/*.txt'
#
# listado = glob.glob(ruta)
#
# for each in listado:
#     crear_cancion(each)

