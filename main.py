from fastapi import FastAPI
from dotenv import load_dotenv
# cargar las variables de entorno del archivo .env
load_dotenv()
from app.api.v1.endpoints.users import router as api_router
from app.api.v1.endpoints.canciones import router as canciones_router
from app.db.db_config import get_database

app = FastAPI()
# Conectarse a la base de datos.
get_database()
# Incluir los routers
app.include_router(api_router)
app.include_router(canciones_router)

# Configurar conexión a la base de datos (esto podría estar en otro módulo importado aquí)
# Por ejemplo, utilizando una función de inicialización que usted defina en `app/db/db_config.py`
