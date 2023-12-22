import os
# Configuración Base de datos:

# Modo de obtener las variables. Mejorable mediante pydantic BaseSettings de pydantic
str_cnn = os.environ.get('MONGODB_CONNECTION_STRING')
db_name = os.environ.get('MONGODB_DATABASE_NAME')

SCHEME = os.environ.get('SCHEME_CRYPTO')
MIN_ROUNDS = os.environ.get('MIN_ROUNDS_CRYPTO')
MAX_ROUNDS = os.environ.get('MAX_ROUNDS_CRYPTO')

# variables necesarias para trabajar con JWT
TOKEN_VALIDATION_TIME = 14
